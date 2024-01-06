{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE GeneralizedNewtypeDeriving #-}
{-# LANGUAGE TupleSections #-}
{-# LANGUAGE LambdaCase #-}

module Raboniel.KISSparser where

import Prelude hiding ( readFile, putStrLn )

import Text.Megaparsec hiding (State)
import Text.Megaparsec.Char
import Text.Megaparsec.Char.Lexer ( decimal )
import Data.Text (Text, pack)
import Data.Text.IO ( readFile, putStrLn )
import Data.Void
import Data.Bifunctor ( first )
import Data.List (nub)

import Data.Map (Map)
import qualified Data.Map as Map
import Data.Set (Set)
import qualified Data.Set as Set
import Control.Monad ( when, filterM )
import Control.Monad.IO.Class ( MonadIO(liftIO) ) 

import Debug.Trace ( trace )

import Raboniel.APparser
import Raboniel.Expression
import Raboniel.Context

data Flag = F0 | F1 | D
    deriving (Show, Eq, Ord)

data Trans = Trans [Flag] MState MState [[Flag]]
    deriving Show

data MooreKISS = MooreKISS MState [BExpr String] [Update String] [Trans]
    deriving Show

data MealyKISS = MealyKISS MState [Update String] [BExpr String] [Trans]
    deriving Show

newtype MState = MState Int
    deriving ( Num, Enum, Real, Integral, Show, Eq, Ord )

numberOfPredicatesMoore :: MooreKISS -> Int
numberOfPredicatesMoore (MooreKISS _ preds _ _) = length preds

numberOfPredicatesMealy :: MealyKISS -> Int
numberOfPredicatesMealy (MealyKISS _ _ preds _) = length preds


parseFlag :: Parser Flag
parseFlag =
    (char '0' >> return F0) <|>
    (char '1' >> return F1) <|>
    (char '-' >> return D)

parseFlags :: Parser [Flag]
parseFlags = some parseFlag

parseFlagDisjunction :: Parser [[Flag]]
parseFlagDisjunction = sepBy1 parseFlags (string " + ")

parseState :: Parser MState
parseState = char 'S' >> decimal

parseTrans :: Parser Trans
parseTrans = do
    upds <- parseFlags
    char ' '
    s0 <- parseState
    char ' '
    s1 <- parseState
    char ' '
    out <- parseFlagDisjunction
    eol
    return $ Trans upds s0 s1 out

parseMooreKISS :: Parser MooreKISS
parseMooreKISS = do
    string ".inputs "
    inputs <- sepBy1 parseUpdate (char ' ')
    eol
    string ".outputs "
    outputs <- sepBy1 predicateParser (char ' ')
    eol
    string ".i " >> decimal >> eol
    string ".o " >> decimal >> eol
    string ".p " >> decimal >> eol
    lastState <- MState . subtract 1 <$> (string ".s " >> decimal <* eol)
    string ".r S" >> decimal >> eol
    transitions <- some parseTrans
    eof
    return $ MooreKISS lastState outputs inputs transitions

parseMooreKISSfromFile :: FilePath -> IO (Either Text MooreKISS)
parseMooreKISSfromFile file = do
    input <- readFile file
    return . first (pack . errorBundlePretty) $ runParser parseMooreKISS file input


parseMealyKISS :: Parser MealyKISS
parseMealyKISS = do
    string ".inputs "
    inputs <- sepBy1 predicateParser (char ' ')
    eol
    string ".outputs "
    outputs <- sepBy1  parseUpdate (char ' ')
    eol
    string ".i " >> decimal >> eol
    string ".o " >> decimal >> eol
    string ".p " >> decimal >> eol
    lastState <- MState . subtract 1 <$> (string ".s " >> decimal <* eol)
    string ".r S" >> decimal >> eol
    transitions <- some parseTrans
    eof
    return $ MealyKISS lastState outputs inputs transitions

parseMealyKISSfromFile :: FilePath -> IO (Either Text MealyKISS)
parseMealyKISSfromFile file = do
    input <- readFile file
    return . first (pack . errorBundlePretty) $ runParser parseMealyKISS file input


decodeOutput :: [BExpr String] -> [Flag] -> State String
decodeOutput bs = concat . zipWith decode bs
    where
    decode e F0 = [Negative e]
    decode e F1 = [Positive e]
    decode e D  = []

decodeUpdates :: [Update String] -> [Flag] -> [Update String]
decodeUpdates us fs = concat $ zipWith decode us fs
    where
    decode u F0 = []
    decode u F1 = [u]
    decode u D  = [] 


expand :: [Flag] -> [[Flag]]
expand [] = [[]]
expand (F0:fs) = (F0:) <$> expand fs
expand (F1:fs) = (F1:) <$> expand fs
expand (D:fs) = let expanded = expand fs in ((F0:) <$> expanded) ++ ((F1:) <$> expanded)

determinize :: [Flag] -> [[Flag]]
determinize fs = [map det fs]
    where
    det F0 = F0
    det F1 = F1
    det D  = F0

stateOutputs :: [Trans] -> Map MState [[Flag]]
stateOutputs trans = (>>=expand) <$> m'
    where
    m' = foldr f Map.empty trans
    f (Trans _ s _ flags) m = Map.insert s flags m

stateOutputsNoExpand :: [Trans] -> Map MState [[Flag]]
stateOutputsNoExpand trans = (>>=determinize) <$> m'
    where
    m' = foldr f Map.empty trans
    f (Trans _ s _ flags) m = Map.insert s flags m


uniqueStateOutputs :: [BExpr String] -> Map MState [[Flag]] -> [State String]
uniqueStateOutputs exprs m = 
    decodeOutput exprs <$> Set.toList uniqueFlagOutputs
    where
    uniqueFlagOutputs = Set.fromList . concat . Map.elems $ m


uniqueTransitions :: [BExpr String] ->
                     [Update String] ->
                     [([Flag], [Flag], [Flag])] -> [(State String, [Update String], State String)]
uniqueTransitions exprs upds trans = decode <$> trans'
    where
    decode (a,u,b) = (decodeOutput' a, decodeUpdates' u, decodeOutput' b)
    decodeUpdates' = decodeUpdates upds
    decodeOutput' = decodeOutput exprs
    trans' = Set.toList . Set.fromList $ trans

expandStatesInTrans :: Map MState [[Flag]] -> Trans -> [([Flag], [Flag], [Flag])]
expandStatesInTrans m  (Trans fs s0 s1 _) = [(x, fs, y) | x <- s0', y <- s1' ]
    where
    s0' = m Map.! s0
    s1' = m Map.! s1

expandTransition :: Trans -> [Trans]
expandTransition (Trans fs s0 s1 stateFlags) = map (\fs' -> Trans fs' s0 s1 stateFlags) . expand $ fs

noTrapStates :: [Trans] -> [MState]
noTrapStates filteredTrans = Set.toList . Set.fromList $ 0 : map (\case Trans _ _ s _ -> s) withoutSelfLoops
    where
    withoutSelfLoops = filter (\case Trans _ s0 s1 _ -> s0 /= s1) filteredTrans

filterConsistentUpdates :: MooreKISS -> Synth [Trans]
filterConsistentUpdates (MooreKISS lastState outputs inputs transitions) = do
    -- liftIO . putStrLn . pack $ ("#trans: " ++ show (length transitions))
    -- liftIO . putStrLn . pack $ ("#plausible: " ++ show (length plausibleTransitions))
    filterM goodTransition (expandTransition =<< plausibleTransitions)
    where
    plausibleTransitions = filter plausible transitions
    goodTransition (Trans upds _ _ _) = do
        stateVariables <- map (\case 'r':'_':v -> v; v -> v) <$> getStateVars
        return $ all (\x -> countUpdates x == 1) stateVariables
        where
        upds' = decodeUpdates inputs upds
        countUpdates var = length . filter (\case Update v _ -> getVarLabel v == var) $ upds'

    plausible (Trans upds _ _ _) =
        (length updatedVariables) == length (nub updatedVariables)
        where
        upds' = decodeUpdates inputs upds
        updatedVariables = map (\case Update v _ -> getVarLabel v) upds'


postProcessMoore ::  MooreKISS -> Synth ([State String], [(State String, [Update String], State String)])
postProcessMoore m@(MooreKISS lastState outputs inputs transitions) = do
    assertStateVarsAndUpdateCompatibility inputs
    -- remove transitions which assume inconsitent updates
    goodTransitions <- filterConsistentUpdates m
    -- liftIO . putStrLn . pack $ ("#goodTrans: " ++ show (length goodTransitions))
    -- liftIO . putStrLn . pack $ ("#goodTrans: " ++ show goodTransitions)
    let notTrapStates = noTrapStates goodTransitions
    let notTrapTrans = filter (\case Trans _ s _ _ -> s `elem` notTrapStates) goodTransitions
    -- let stateOut = stateOutputs notTrapTrans
    -- let stateOut = stateOutputsNoExpand notTrapTrans
    doStateExpansion <- getStateExpansion
    let stateOut = if doStateExpansion then stateOutputs notTrapTrans else stateOutputsNoExpand notTrapTrans
    let expandedTrans = expandStatesInTrans stateOut =<< notTrapTrans
    -- liftIO . putStrLn . pack $ ("#expandedTrans: " ++ show (length expandedTrans))
    let uniqueTrans = uniqueTransitions outputs inputs expandedTrans
    let uniqueStates = uniqueStateOutputs outputs stateOut
    return (uniqueStates, uniqueTrans)

assertStateVarsAndUpdateCompatibility :: [Update String] -> Synth ()
assertStateVarsAndUpdateCompatibility upds = do
    stateVariables <- map (\case 'r':'_':v -> v; v -> v) <$> getStateVars
    let updatedVariables = map (\case Update v _ -> getVarLabel v) upds
    let stateVariablesS = Set.fromList stateVariables
    let updatedVariablesS = Set.fromList updatedVariables

    let unusedVars = stateVariablesS Set.\\ updatedVariablesS
    let undeclaredVars = updatedVariablesS Set.\\ stateVariablesS
    when (not.null $ unusedVars) $
        errorWithoutStackTrace ("Variables are declared, but no updates exist: "++show (Set.toList unusedVars))
    when (not.null $ undeclaredVars) $
        errorWithoutStackTrace ("Variables are updated, but not declared: "++show (Set.toList undeclaredVars))
    return ()


preProcessMealy :: MealyKISS -> [(MState, State String, [Update String], MState)]
preProcessMealy m@(MealyKISS lastState outputs inputs transitions) = 
    map decode transitions
    where
    decode (Trans fs s0 s1 us) = (s0, decodeOutput inputs fs, decodeUpdates outputs (head us), s1)
    -- unambiguousTrans = 
    --     map (\case Trans fs s0 s1 [u] -> (s0, fs, u, s1)) .
    --     filter (\case Trans _ _ _ [u] -> D `notElem` u; _ -> False) $ transitions
        -- TODO: There can be multiple valid outputs for a single transition!
        --       instead of discarding these one of them needs to be selected arbitrarily.
        --       I don't think Dash can ever occur on the output side