{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE RecordWildCards #-}
{-# LANGUAGE LambdaCase #-}
{-# LANGUAGE BangPatterns #-}

module Raboniel.Synthesis where

import Prelude hiding (putStr, putStrLn, readFile, unlines, writeFile )
import Data.Text.IO ( putStr, putStrLn, readFile, writeFile )

import Data.Text (Text, isInfixOf, pack, unlines)

import System.Process                 ( readProcessWithExitCode )
import System.Directory ( copyFile, removeFile )
import System.Exit                    ( ExitCode )
import Data.List.NonEmpty ( NonEmpty(..) )
import Data.List (sort)
import Control.Monad.Trans.Reader
import Control.Monad.IO.Class ( MonadIO(liftIO) )
import Control.Monad ( when, guard ) 
import Control.DeepSeq (force)
import Data.IORef

import Z3.Monad ( evalZ3 )
import Raboniel.KISSparser ( MooreKISS (MooreKISS), parseMooreKISSfromFile, parseMealyKISSfromFile, preProcessMealy, postProcessMoore, MealyKISS (MealyKISS), numberOfPredicatesMoore, numberOfPredicatesMealy )
import Raboniel.Checks

import Raboniel.Expression
import Raboniel.TSLMetaParser
import Raboniel.CodeGeneration
import Raboniel.Z3Expression (evalSMTSynth)
import Raboniel.Context

data SynthMode = Minimize | NoMinimization
synthPath = "./synth.sh"
synthPathMini = "./synth_mini.sh"
checkTslPath = "./check.sh"

callCmd :: MonadIO io => NonEmpty String -> io (ExitCode, String, String)
callCmd (cmd :| args) = liftIO $ readProcessWithExitCode cmd args stdIn
  where stdIn = ""

checkTSL :: String -> IO Bool
checkTSL fileName = do
    (_,out,err) <- callCmd $ "bash" :| [checkTslPath,fileName]
    let out' = pack out
    if "invalid" `isInfixOf` out' then do
      putStrLn out'
      putStrLn . pack $ err
      return False
    else if "valid" `isInfixOf` out' then
      return True
    else
      error "Error when checking TSL file."

callSynth :: SynthMode -> String -> Synth Bool
callSynth mode fileName = do
  (_,out,_) <- callCmd $ "bash" :| [synthPath',fileName]
  let out' = pack out
  if "UNREALIZABLE" `isInfixOf` out' then
    return False
  else if "REALIZABLE" `isInfixOf` out' then
    return True
  else
    error ("Error in synthesis of file: "++fileName)
  where
  synthPath' = case mode of
    Minimize -> synthPathMini
    NoMinimization -> synthPath

synth :: SynthMode -> Int -> Synth Bool
synth mode iteration = do
  prefix <- prefix_ <$> getContext
  callSynth mode (prefix++"_R"++show iteration)

readTSLAnnotations :: FilePath -> IO (Either Text ([VarName], [VarName], [APLiteral VarName]))
readTSLAnnotations file = do
    tsl <- readFile file
    return $ parseTSLAnnotations tsl


createNextSpecFile :: Int -> [Text] -> Synth ()
createNextSpecFile iteration newAssumptions = do
  oldFile <- tslFile iteration
  newFile <- tslFile (iteration+1)
  oldSpec <- liftIO $ readFile oldFile
  let newSpec = oldSpec <> "\nalways assume {\n" <> unlines (map ("  "<>) newAssumptions) <> "}\n"
  liftIO $ writeFile newFile newSpec


cleanUpTmpFiles :: Int -> Synth ()
cleanUpTmpFiles iteration = do
  deleteTmpFiles <- getDeleteTmpFiles
  case deleteTmpFiles of
    DeleteAll -> do
      liftIO . removeFile =<< tslFile iteration
      deleteKissAndTLSF
    KeepTSL ->
      deleteKissAndTLSF
    KeepAll -> return ()
  where
  deleteKissAndTLSF = do
    liftIO . removeFile =<< kissFile iteration
    liftIO . removeFile =<< tlsfFile iteration

logFinalSystemStats :: Int -> MealyKISS -> Synth ()
logFinalSystemStats counter (MealyKISS lastState _ predicates _) = do
  liftIO . putStrLn $ "--------------------------------"
  ctx <- getContext
  let prefix = prefix_ ctx
  liftIO . putStrLn $ "Synthesis Stats ("<>pack prefix<>"):"
  liftIO . putStrLn $ "Result: realizable"
  miniMode <- getMinimizationMode
  let refinements = if miniMode == MinimizeSystem then counter-1 else counter
  liftIO . putStrLn $ "#Refinements: " <> (pack.show $ refinements)
  liftIO . putStrLn $ "#System states: " <> (pack.show.toInteger $ lastState+1)
  let numPredicates = length predicates
  initialNumPredicates <- getInitialNumberOfPredicates
  liftIO . putStrLn $ "#Predicates learned: " <> (pack.show $ numPredicates-initialNumPredicates)

logUnrealizableStats :: Int -> MooreKISS -> Synth ()
logUnrealizableStats counter (MooreKISS lastState predicates _ _) = do
  liftIO . putStrLn $ "--------------------------------"
  ctx <- getContext
  let prefix = prefix_ ctx
  liftIO . putStrLn $ "Synthesis Stats ("<>pack prefix<>"):"
  liftIO . putStrLn $ "Result: unrealizable"
  miniMode <- getMinimizationMode
  liftIO . putStrLn $ "#Refinements: " <> (pack.show $ counter)
  let numPredicates = length predicates
  initialNumPredicates <- getInitialNumberOfPredicates
  liftIO . putStrLn $ "#Predicates learned: " <> (pack.show $ numPredicates-initialNumPredicates)


runSynthLoop :: Synth ()
runSynthLoop =
  run 0
  where
  run !counter = do
    liftIO . putStrLn $ "Starting Iteration "<>pack (show counter)
    mode <- (\case MinimizeAlways -> Minimize; _ -> NoMinimization) <$> getMinimizationMode 
    synthResult <- synth mode counter
    if synthResult then do
      liftIO . putStrLn $ "Synthesis successful!"
      generateFinalProgram counter
    else do
      kf <- kissFile counter
      parseResult <- liftIO $ parseMooreKISSfromFile kf
      case parseResult of
        Left t -> do
          liftIO . putStrLn $ "Unexpected parse error in a kiss file:"
          liftIO . putStrLn $ t
        Right m -> do
            setInitialNumberOfPredicatesIfEmpty (numberOfPredicatesMoore m)
            m' <- postProcessMoore m
            assumptions <- evalSMTSynth $
                checkCounterStratConsistency m'
            if null assumptions then do
              cleanUpTmpFiles counter
              liftIO . putStrLn $ "Unrealizable!"
              logUnrealizableStats counter m
            else do
              createNextSpecFile counter assumptions
              cleanUpTmpFiles counter
              run (counter+1)

generateFinalProgram :: Int -> Synth()
generateFinalProgram counter = do
  miniMode <- getMinimizationMode
  if miniMode == MinimizeSystem then do
    minimizeSystem counter
    cleanUpTmpFiles counter
    generateProgram (counter+1)
    cleanUpTmpFiles (counter+1)
  else do
    generateProgram counter
    cleanUpTmpFiles counter

generateProgram :: Int -> Synth()
generateProgram counter = do
  kf <- kissFile counter
  parseResult <- liftIO $ parseMealyKISSfromFile kf
  case parseResult of
    Left e -> do
      liftIO . putStrLn $ "Unexpected parse error in a kiss file:"
      liftIO . putStrLn $ e
    Right m -> do
      setInitialNumberOfPredicatesIfEmpty (numberOfPredicatesMealy m)
      logFinalSystemStats counter m
      let trans = preProcessMealy m
      outputFormat <- getOutputFormat 
      case outputFormat of
        PythonFormat     -> do
          program <- generatePython trans
          fileName <- pyFile
          liftIO $ writeFile fileName program
          liftIO . putStrLn $ "The system can be found in " <> pack fileName
        PseudoCodeFormat -> do
          program <- generateVerbosePseudoCode trans
          fileName <- pcodeFile
          liftIO $ writeFile fileName program
          liftIO . putStrLn $ "The system can be found in " <> pack fileName

minimizeSystem :: Int -> Synth()
minimizeSystem counter = do
  liftIO . putStrLn $ "Minimizing system states."
  createNextSpecFile counter ["true"]
  synth Minimize (counter+1)
  return ()


synthesize :: Config -> FilePath  -> IO ()
synthesize config tslFile = do
  valid <- checkTSL tslFile
  guard valid
  let prefix = reverse . drop 4 . reverse $ tslFile
  copyFile tslFile (prefix ++"_R0.tsl")
  as <- readTSLAnnotations tslFile
  case as of
    Left e -> do
      putStrLn "Parsing annotations failed:"
      putStrLn e
    Right (stateVars, inputVars, stateInvariant) -> do
      initNumP <- newIORef (-1 :: Int)
      runSynth (Context prefix stateVars inputVars stateInvariant initNumP config) runSynthLoop
