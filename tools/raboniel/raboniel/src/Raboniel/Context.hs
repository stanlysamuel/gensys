{-# LANGUAGE GeneralizedNewtypeDeriving #-}


module Raboniel.Context where

import Control.Monad.Trans.Reader
import Control.Monad.IO.Class ( MonadIO(liftIO) )
import Control.Monad ( when ) 
import Data.IORef
import Raboniel.Expression

data MinimizationMode = MinimizeAlways | MinimizeNever | MinimizeSystem
  deriving (Eq,Show)
data DeleteTmpFiles = DeleteAll | KeepAll | KeepTSL
  deriving (Eq,Show)

data StateSimplificationMode = NoSimplification | EliminateUneccessaryParts
  deriving (Eq,Show)

data OutputFormatMode = PseudoCodeFormat | PythonFormat
  deriving (Eq,Show)

data Context = Context {
  prefix_ :: String,
  stateVars_ :: [VarName],
  inputVars_ :: [VarName],
  stateInvariant_ :: [APLiteral VarName],
  initialNumberOfPredicates_ :: IORef Int,
  config_ :: Config
}

data Config = Config {
  minimizationMode :: MinimizationMode,
  -- stateSimplificationMode :: StateSimplificationMode,
  simplifyProgram :: Bool,
  noStateExpansion :: Bool,
  deleteTmpFiles :: DeleteTmpFiles,
  outputFormat :: OutputFormatMode
} deriving (Eq,Show)


class (Applicative m, Monad m, MonadIO m) => MonadSynth m where
  getContext :: m Context

instance MonadSynth Synth where
  getContext = Synth ask

newtype Synth a = Synth { _unSynth :: ReaderT Context IO a }
    deriving (Functor, Applicative, Monad, MonadIO, MonadFail)

instance MonadSynth m => MonadSynth (ReaderT r m) where
  getContext = ReaderT $ const getContext

runSynth :: Context -> Synth a -> IO a
runSynth ctx s = runReaderT (_unSynth s) ctx


tslFile :: MonadSynth m => Int -> m FilePath
tslFile iteration = do
  ctx <- getContext
  let prefix = prefix_ ctx
  return $ prefix++"_R"++show iteration++".tsl"

kissFile :: MonadSynth m => Int -> m FilePath
kissFile iteration = do
  ctx <- getContext
  let prefix = prefix_ ctx
  return $ prefix++"_R"++show iteration++".kiss"

tlsfFile :: MonadSynth m => Int -> m FilePath
tlsfFile iteration = do
  ctx <- getContext
  let prefix = prefix_ ctx
  return $ prefix++"_R"++show iteration++".tlsf"

pcodeFile :: MonadSynth m => m FilePath
pcodeFile = do
  ctx <- getContext
  let prefix = prefix_ ctx
  return $ prefix ++ ".pcode"

pyFile :: MonadSynth m => m FilePath
pyFile = do
  ctx <- getContext
  let prefix = prefix_ ctx
  return $ prefix ++ ".py"

getStateVars :: MonadSynth m => m [VarName]
getStateVars = stateVars_ <$> getContext

getInputVars :: MonadSynth m => m [VarName]
getInputVars = inputVars_ <$> getContext

getVars :: MonadSynth m => m [VarName]
getVars = (++) <$> getStateVars <*> getInputVars

stripTypePrefix :: VarName -> VarName
stripTypePrefix ('r':'_':name) = name
stripTypePrefix name = name

getStateInvariant :: MonadSynth m => m [APLiteral VarName]
getStateInvariant = stateInvariant_ <$> getContext


getMinimizationMode :: MonadSynth m => m MinimizationMode
getMinimizationMode = minimizationMode . config_ <$> getContext

getDeleteTmpFiles :: MonadSynth m => m DeleteTmpFiles
getDeleteTmpFiles = deleteTmpFiles . config_ <$> getContext

getSimplify :: MonadSynth m => m Bool
getSimplify = simplifyProgram . config_ <$> getContext

getStateExpansion :: MonadSynth m => m Bool
getStateExpansion = not . noStateExpansion . config_ <$> getContext

getOutputFormat :: MonadSynth m => m OutputFormatMode
getOutputFormat = outputFormat . config_ <$> getContext

getInitialNumberOfPredicates :: MonadSynth m => m Int
getInitialNumberOfPredicates = do
  ref <- initialNumberOfPredicates_ <$> getContext
  liftIO $ readIORef ref

setInitialNumberOfPredicates :: MonadSynth m => Int -> m ()
setInitialNumberOfPredicates n = do
  ref <- initialNumberOfPredicates_ <$> getContext
  liftIO $ writeIORef ref n

setInitialNumberOfPredicatesIfEmpty :: MonadSynth m => Int -> m ()
setInitialNumberOfPredicatesIfEmpty n = do
  ref <- initialNumberOfPredicates_ <$> getContext
  value <- liftIO $ readIORef ref
  when (value==(-1)) $ liftIO $ writeIORef ref n