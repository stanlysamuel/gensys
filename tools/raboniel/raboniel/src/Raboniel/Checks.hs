{-# LANGUAGE LambdaCase #-}
{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE OverloadedStrings #-}

{-# LANGUAGE TupleSections #-}
{-# LANGUAGE BangPatterns #-}
module Raboniel.Checks where

import Raboniel.Expression
    ( negStateToText,
      negTransitionToText,
      negateAP,
      weakestPrecondition,
      APLiteral,
      State,
      Transition(..),
      Update (Update),
      VarName, freeVariables )
import Raboniel.Z3Expression
    ( SMTSynth, prime, litToAST, updToAST, simplifyState, toSMTVar, filterNew, simplifyFormula, removeComplexFormulas )
import Raboniel.Context ( getStateInvariant, getInputVars, stripTypePrefix )
import Raboniel.SMTparser


import Z3.Monad (
    MonadZ3,
    AST,
    Symbol,
    mkAnd,
    checkAssumptions,
    Result(..),
    getUnsatCore,
    mkEq,
    mkIntVar,
    mkNot,
    mkStringSymbol,
    Z3,
    mkRealVar,
    mkQuantifierEliminationTactic,
    toApp,
    mkForallConst,
    mkExistsConst,
    applyTactic,
    mkGoal,
    goalAssert,
    getApplyResultSubgoal,
    getGoalFormulas, astToString, mkAndInverterGraphTactic, andThenTactic )
import Debug.Trace ( trace )
import Data.Maybe ( catMaybes, fromJust )
import Data.List ( elemIndex, find )
import Data.Map (Map)
import qualified Data.Map as Map
import qualified Data.Set as Set
import Data.Text ( Text )
import Control.Monad ( when, filterM, (<=<) )
import Control.Monad.IO.Class ( MonadIO(liftIO) )
import Control.Monad.Trans.Reader

stateConsistent :: State VarName -> SMTSynth Bool
stateConsistent state = do
    props <- mapM litToAST state
    r <- checkAssumptions props
    case r of
        Sat -> return True
        Unsat -> return False
        Undef -> error ("SMT result unknown: "++show props)



-- Nothing if consitent otherwise the unsat core
stateInconsistent :: State VarName -> SMTSynth (Maybe [APLiteral VarName])
stateInconsistent state = do
    props <- mapM litToAST state
    let mapping = zip props state
    r <- checkAssumptions props
    case r of
        Sat -> return Nothing
        Undef -> error ("SMT result unknown: "++show props)
        Unsat -> do
            core <- getUnsatCore
            let aps = map snd . filter (\x -> fst x `elem` core) $ mapping
            return $ Just aps

transitionConsistent :: Transition VarName -> SMTSynth Bool
transitionConsistent (Transition pre upd post) = do
    pre' <- mapM litToAST pre
    post' <- mapM (litToAST . fmap prime) post
    upd' <- mapM updToAST upd
    r <- checkAssumptions (pre' ++ post' ++ upd')
    case r of
        Sat -> return True
        Unsat -> return False
        Undef -> error ("SMT result unknown: "++show (pre' ++ post' ++ upd'))


transitionInconsistent :: Transition VarName -> SMTSynth (Maybe (Transition VarName))
transitionInconsistent (Transition pre upd post) = do
    pre' <- mapM litToAST pre
    let pre_mapping = zip pre' pre
    post' <- mapM (litToAST . fmap prime) post
    let post_mapping = zip post' post
    upd' <- mapM updToAST upd
    let upd_mapping = zip upd' upd
    r <- checkAssumptions (pre' ++ post' ++ upd')
    case r of
        Sat -> return Nothing
        Undef -> error ("SMT result unknown: "++show (pre' ++ post' ++ upd'))
        Unsat -> do
            core <- getUnsatCore
            let pre'' = map snd . filter (\x -> fst x `elem` core) $ pre_mapping
            let post'' = map snd . filter (\x -> fst x `elem` core) $ post_mapping
            let upd'' = map snd . filter (\x -> fst x `elem` core) $ upd_mapping
            return $ Just (Transition pre'' upd'' post'')

transSplit :: Transition VarName -> SMTSynth (Maybe [(Transition VarName, APLiteral VarName)])
transSplit t@(Transition _ _ post) = do
    inputs <- Set.fromList . map stripTypePrefix <$> getInputVars 
    let vs = Set.fromList (freeVariables =<< post)
    if Set.disjoint inputs vs then 
        transitionSplit t
    else
        transitionSplitWithInputs t

-- Works only if there are not inputs mentioned in the state.
transitionSplit :: Transition VarName -> SMTSynth (Maybe [(Transition VarName, APLiteral VarName)])
transitionSplit  (Transition pre upd post) = do
    pre' <- mapM litToAST pre
    upd' <- mapM updToAST upd
    post' <- mapM (litToAST . fmap prime) post
    neg_post <- mkNot =<< mkAnd post'
    r <- checkAssumptions (pre' ++ upd' ++ [neg_post])
    case r of
        Unsat -> return Nothing
        Undef -> error ("SMT result unknown: "++show (pre' ++ upd' ++ [neg_post]))
        Sat -> do
            -- wps' <- simplifyState wps
            Just . catMaybes <$> mapM (refinesPre pre') wps

    where
    wps = map (weakestPrecondition upd) post
    refinesPre pre' ap = do
        ap' <- litToAST . negateAP $ ap
        r <- checkAssumptions (ap':pre')  -- check that ap 'splits' the state pre (pre /\ ap <=/=> pre)
        case r of
            Unsat -> return Nothing
            Undef -> error ("SMT result unknown: "++show (ap':pre'))
            Sat -> do
                r2 <- fmap (,ap) <$> transitionInconsistent (Transition (negateAP ap:pre) upd post)
                case r2 of
                    Nothing -> (liftIO . print) (Transition (negateAP ap:pre) upd post) >> return Nothing
                    Just _ -> return r2
    

transitionSplitWithInputs :: Transition VarName -> SMTSynth (Maybe [(Transition VarName, APLiteral VarName)])
transitionSplitWithInputs (Transition pre upd post) = do
    pre' <- mapM litToAST pre
    upd' <- mapM updToAST upd
    post' <- mapM (litToAST . fmap prime) post
    neg_post <- mkNot =<< mkAnd post'

    finputs <- mapM ((toApp <=< toSMTVar) . prime . stripTypePrefix) =<< getInputVars
    x <- mkForallConst [] finputs =<< mkAnd (pre' ++ upd' ++ [neg_post])
    r <- checkAssumptions [x]
    case r of
        Unsat -> return Nothing
        Undef -> error ("SMT result unknown: "++show x)
        Sat -> do
            nps <- findNewPredicates finputs pre'
            Just . catMaybes <$> mapM (refinesPre pre') nps 
            
    where
    wp = map (weakestPrecondition upd' . fmap prime) post
    upd' = map (\(Update v e) -> Update (fmap prime v) e) upd

    findNewPredicates finputs pre' = do
        wp' <- mapM litToAST wp
        f <- mkExistsConst [] finputs =<< mkAnd (pre' ++ wp')
        qe <- mkQuantifierEliminationTactic 
        -- aig <- mkAndInverterGraphTactic 
        -- tac <- andThenTactic qe aig
        g <- mkGoal True True False
        goalAssert g f
        a <- applyTactic qe g
        ps <- getGoalFormulas =<< getApplyResultSubgoal a 0 -- there should be only one subgoal
        new <- filterNew pre ps
        newSimpl <- mapM (simplifyFormula <=< parseFormula) new
        removeComplexFormulas newSimpl

    refinesPre pre' ap = do
        ap' <- litToAST . negateAP $ ap
        r <- checkAssumptions (ap':pre')  -- check that ap 'splits' the state pre (pre /\ ap <=/=> pre)
        case r of
            Unsat -> return Nothing
            Undef -> error ("SMT result unknown: "++show (ap':pre'))
            Sat -> do
                r2 <- fmap (,ap) <$> transitionInconsistent (Transition (negateAP ap:pre) upd post)
                case r2 of
                    Nothing -> (liftIO . print) (Transition (negateAP ap:pre) upd post) >> return Nothing
                    Just _ -> return r2



filterUninteresstingTransitions :: [State VarName] -> [Transition VarName] -> SMTSynth [Transition VarName]
filterUninteresstingTransitions states transitions = do
    isBadState' <- isBadState
    return $ filter (not . startsInBadState isBadState') transitions
    where
    startsInBadState isBadState (Transition s _ _) =
        isBadState Map.! s

    isBadState = Map.fromList . zip states <$> mapM checkBadState states

    checkBadState s = do
        s' <- mapM litToAST s
        inv' <- mapM litToAST =<< getStateInvariant
        r <- checkAssumptions (s' ++ inv')
        case r of
            Sat -> return False
            Unsat -> return True
            Undef -> error ("SMT result unknown: "++show (s' ++ inv'))


checkStateConsistency :: [State VarName] -> SMTSynth [State VarName]
checkStateConsistency states = catMaybes <$> mapM stateInconsistent states

checkTransConsistency :: [Transition VarName] -> SMTSynth [Transition VarName]
checkTransConsistency trans = catMaybes <$> mapM transitionInconsistent trans

checkTransSplit :: [Transition VarName] -> SMTSynth [Transition VarName]
checkTransSplit trans = do
    ts <- catMaybes <$> mapM transSplit trans
    return (map fst . concat $ ts)


checkCounterStratConsistency :: ([State VarName], [(State VarName, [Update VarName], State VarName)]) -> SMTSynth [Text]
checkCounterStratConsistency (states, trans) = do
    liftIO . putStr $ "#States:"
    liftIO . print $ length states
    liftIO . putStr $ "#Trans:"
    liftIO . print $ length trans
    newAssumptions <- checkCounterStratConsistency'
    return . Set.toList . Set.fromList $ newAssumptions
    where
    checkCounterStratConsistency' = do
        trans'' <- trans'
        -- liftIO $ putStrLn "Starting consistency checks."
        stateCEs <- checkStateConsistency states
        -- liftIO $ putStrLn "States checks complete."
        if stateCEs /= [] then return (map negStateToText stateCEs) else do
            transCEs <- checkTransConsistency trans''
            -- liftIO $ putStrLn "Transition checks complete."
            if transCEs /= [] then return (map negTransitionToText transCEs) else do
                splits <- checkTransSplit trans''
                liftIO . putStrLn $ "Learned "<> (show . length) splits <> " new predicates (includes duplicates)."
                return (map negTransitionToText splits)
    trans' = filterUninteresstingTransitions states . map (\case (a,u,b) -> Transition a u b) $ trans
