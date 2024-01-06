{-# LANGUAGE LambdaCase #-}
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE TupleSections #-}
{-# LANGUAGE ScopedTypeVariables #-}

module Raboniel.CodeGeneration where

import Data.Text (Text)
import Data.Text.Lazy.Builder (Builder, fromString, toLazyText)
import Data.Text.Lazy (toStrict)
import Data.List (intersperse, sort)
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Maybe (catMaybes)

import Raboniel.Expression
import Raboniel.Z3Expression ( simplifyState, simplifyDisjunction, evalSMTSynth )
import Raboniel.KISSparser (MState(..))
import Raboniel.Context ( StateSimplificationMode(..), Synth, getStateVars, getInputVars, getSimplify )
import Raboniel.PythonCodeGen( toPython )

simplifyTransitions :: [(MState, State String, [Update String], MState)] 
                       -> Synth [(MState, State String, [Update String], MState)]
simplifyTransitions =
    evalSMTSynth . mapM simplifyTrans
    where 
    simplifyTrans (m1, s, us, m2) = (m1,,us,m2) <$> simplifyState s


mergeTransitions :: [(MState, State String, [Update String], MState)]
                    -> [(MState, [State String], [Update String], MState)]
mergeTransitions ts = 
    toTransitions . Map.toList $ Map.fromListWith (++) keyValuePairs
    where
    toTransitions = map (\((s1,us,s2),oss) -> (s1,oss,us,s2))
    keyValuePairs = map (\(s1, os, us, s2) -> ((s1,us,s2),[os])) sortedUpdates
    sortedUpdates = map (\(s1, os, us::[Update String], s2) -> (s1,os,sort us,s2)) ts

simplify :: [(MState, State String, [Update String], MState)]
            -> Synth [(MState, [State String], [Update String], MState)]
simplify ts = do
    simplify <- getSimplify
    if simplify then do
        trans <- simplifyTransitions ts
        let trans' = mergeTransitions trans
        evalSMTSynth $ catMaybes <$> mapM simplifyTrans trans'
    else
        return . map(\(s1, os, us, s2) -> (s1, [os], us, s2)) $ ts
    where
    simplifyTrans (s1, os, us, s2) = do
        os' <- simplifyDisjunction os
        if null os' then
            return Nothing
        else
            return . Just . (s1,,us,s2) $ os'



generateVerbosePseudoCode :: [(MState, State String, [Update String], MState)]
                             -> Synth Text
generateVerbosePseudoCode trans = do
    trans' <- simplify trans
    toVerbosePseudoCode trans'


generatePython :: [(MState, State String, [Update String], MState)]
                  -> Synth Text
generatePython trans = do
    trans' <- simplify trans
    py <- toPython trans'
    return . toStrict . toLazyText $ py


toVerbosePseudoCode :: [(MState, [State String], [Update String], MState)] -> Synth Text
toVerbosePseudoCode trans = do
    stateVars <- getStateVars
    inputVars <- getInputVars
    let ins = mconcat . intersperse ", " $ map fromString inputVars
    let states = mconcat . intersperse ", " $ map fromString stateVars
    let header = "State: " <> states <> "\n" <> "Inputs: " <> ins <> "\n\n"
    let initialization = "Initialization:\n    [state <- s0()]\n\n"
    let trans' = mconcat . map transitionToVerbosePseudoCode $ trans
    return . toStrict . toLazyText $ header <> initialization <> "LOOP:\n" <> trans'


transitionToVerbosePseudoCode :: (MState, [State String], [Update String], MState) -> Builder
transitionToVerbosePseudoCode (s0, ps, us, s1) = condition <> "\n" <> nextState <> updates <> "\n\n"
    where
    condition = "  case: eq state " <> mStateToText s0 <> " &&\n        (\n" <> psT' <> "\n        )"
    psT' = mconcat . intersperse " ||\n\n" $ psT
    psT = map (mconcat . intersperse " &&\n" . map (("          "<>) . aPToTextBuilder)) ps
    nextState = "  then: [ state <- " <> mStateToText s1 <> " ]\n"
    updates = mconcat . intersperse "\n" . map (("        "<>) . updateToTextBuilder) $ us


mStateToText :: MState -> Builder
mStateToText (MState i) = "s" <> (fromString . show $ i) <> "()"
