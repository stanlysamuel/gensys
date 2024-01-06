{-# LANGUAGE LambdaCase #-}
{-# LANGUAGE TupleSections #-}
{-# LANGUAGE GeneralizedNewtypeDeriving #-}

module Raboniel.Z3Expression where

import Z3.Monad
    ( MonadZ3,
      AST,
      Result(Undef, Sat, Unsat),
      checkAssumptions,
      evalZ3,
      mkAdd,
      mkAnd,
      mkDiv,
      mkEq,
      mkGe,
      mkGt,
      mkIntVar,
      mkInteger,
      mkLe,
      mkLt,
      mkMul,
      mkNot,
      mkRealNum,
      mkRealVar,
      mkStringSymbol,
      mkSub,
      mkXor,
      mkOr,
      Z3 )
import Control.Monad.Trans.Reader
import Control.Monad.IO.Class ( MonadIO(liftIO) )
import Data.List ( elemIndex, find )
import Control.Monad ( (<=<), msum, filterM )
import qualified Data.Set as Set

import Raboniel.Expression (VarName, IntExpr(..), BExpr(..), APLiteral(..), Update(..), State, getVarLabel, negateAP)
import Raboniel.Context

data Z3ExtendedContext = Z3ExtendedContext {
    toSMTVar_ :: VarName -> AST,
    synthContext_ :: Context
}

-- type SMT = ReaderT Z3ExtendedContext Z3

newtype SMTSynth a = SMTSynth { _unSMTSynth :: ReaderT Z3ExtendedContext Z3 a }
    deriving (Functor, Applicative, Monad, MonadIO, MonadFail, MonadZ3)

instance MonadSynth SMTSynth where
  getContext = SMTSynth $ asks synthContext_

evalSMTSynth :: SMTSynth a -> Synth a
evalSMTSynth smtSynth = do
    ctx <- getContext 
    symNames <- getVars 
    let io = evalExtZ3 ctx symNames (_unSMTSynth smtSynth)
    liftIO io
    where
    evalExtZ3 ctx symNames smt = evalZ3 $ do
        toSMTVar'' <- createSMTVars symNames
        runReaderT smt (Z3ExtendedContext toSMTVar'' ctx)


toSMTVar :: VarName -> SMTSynth AST
toSMTVar v = do
    ectx <- SMTSynth ask
    return $ toSMTVar_ ectx v

-- evalSMT :: [VarName] -> SMT a -> IO a
-- evalSMT symNames smt = evalZ3 $ do
--     toSMTVar'' <- createSMTVars symNames
--     runReaderT smt (Z3ExtendedContext toSMTVar'')


createSMTVars :: MonadZ3 z3 => [VarName] -> z3 (VarName -> AST)
createSMTVars symNames = do
    symsAssocList <- traverse mkSMTVar names
    return $ f symNames symsAssocList
    where
    f symNames symsAssocList symName = case find (\x -> fst x == symName) symsAssocList of
            Just (_,n) -> n
            Nothing -> error ("Variable name not found: "++symName)
    mkSMTVar = \case
        'r':'_':name -> (name,) <$> (mkRealVar =<< mkStringSymbol name)
        name -> (name,) <$> (mkIntVar =<< mkStringSymbol name)
    names = symNames ++ map prime symNames


prime :: VarName -> VarName
prime s = s++"$prime"


iExprToAST :: IntExpr VarName -> SMTSynth AST
iExprToAST = \case 
    Var i -> toSMTVar i
    VarR r -> toSMTVar r
    Const c -> mkInteger c
    ConstR c -> mkRealNum c
    Add e1 e2 -> mkAdd =<< sequence [iExprToAST e1, iExprToAST e2]
    Sub e1 e2 -> mkSub =<< sequence [iExprToAST e1, iExprToAST e2]
    Mul e1 e2 -> mkMul =<< sequence [iExprToAST e1, iExprToAST e2]
    Div e1 e2 -> do e1' <- iExprToAST e1
                    e2' <- iExprToAST e2
                    mkDiv e1' e2'
    Mod e1 e2 -> do e1' <- iExprToAST e1
                    e2' <- iExprToAST e2
                    mkDiv e1' e2'
    
bExprToAST :: BExpr VarName -> SMTSynth AST
bExprToAST = \case
    Eq e1 e2  -> do e1' <- iExprToAST e1
                    e2' <- iExprToAST e2
                    mkEq e1' e2'
    Le e1 e2 -> do e1' <- iExprToAST e1
                   e2' <- iExprToAST e2
                   mkLe e1' e2'
    Ge e1 e2 -> do e1' <- iExprToAST e1
                   e2' <- iExprToAST e2
                   mkGe e1' e2'
    Lt e1 e2 -> do e1' <- iExprToAST e1
                   e2' <- iExprToAST e2
                   mkLt e1' e2'
    Gt e1 e2 -> do e1' <- iExprToAST e1
                   e2' <- iExprToAST e2
                   mkGt e1' e2'

litToAST :: APLiteral VarName -> SMTSynth AST
litToAST = \case
    Positive e -> bExprToAST e
    Negative e -> mkNot =<< bExprToAST e

updToAST :: Update VarName -> SMTSynth AST
updToAST (Update x e) = do 
        x' <- toSMTVar . prime . getVarLabel $ x
        e' <- iExprToAST e
        mkEq x' e'

stateToAST :: State VarName -> SMTSynth AST
stateToAST = mkAnd <=< mapM litToAST



simplifyState :: State VarName -> SMTSynth (State VarName)
simplifyState = run []
    where
    run required [] = return required
    run required ut@(ap:untested) = do
        old <- mkAnd =<< mapM litToAST (required ++ ut)
        new <- mkAnd =<< mapM litToAST (required ++ untested)
        eqTest <- mkXor old new
        r <- checkAssumptions [eqTest]
        case r of
            Sat -> run (ap:required) untested -- not equal
            Unsat -> run required untested    -- equal
            Undef -> error ("SMT result unknown: "++show eqTest)

simplifyDisjunction :: [State  VarName] -> SMTSynth [State VarName]
simplifyDisjunction = run []
    where
    run required [] = return required
    run required ut@(ap:untested) = do
        old <- mkOr =<< mapM stateToAST (required ++ ut)
        new <- mkOr =<< mapM stateToAST (required ++ untested)
        eqTest <- mkXor old new
        r <- checkAssumptions [eqTest]
        case r of
            Sat -> run (ap:required) untested -- not equal
            Unsat -> run required untested    -- equal
            Undef -> error ("SMT result unknown: "++show eqTest)


simplifyFormula :: [[APLiteral VarName]] -> SMTSynth [[APLiteral VarName]]
simplifyFormula f = do
    -- liftIO . print $ f
    l <- equalsToLiteral literals f
    case l of
        Just l' -> return [[l']]
        Nothing -> do
            fs <- mapM simplifyState f
            simplifyDisjunction fs
    where
    literals = Set.toList . Set.fromList . concat $ f


-- This is a transformation that sacrifices termination in many cases and should be removed at some point.
-- For now only warn when information is discarded!
-- Removing formulas leads to false claims of unrealizable. Changed to an error.
removeComplexFormulas :: [[[APLiteral VarName]]] -> SMTSynth [APLiteral VarName]
removeComplexFormulas fs =
    concat <$> mapM isSimple fs
    where
    isSimple [[a]] = return [a]
    isSimple f = do 
        -- liftIO . putStr $ "Complex Formula will be ignored: "
        -- liftIO . print $ f
        error "QE lead to an unexpectedly complex result, aborting..."
        -- return []



equalsToLiteral :: [APLiteral VarName] -> [[APLiteral VarName]] -> SMTSynth (Maybe (APLiteral VarName))
equalsToLiteral literals f = firstJusts <$> mapM eq literals
    where
    -- literals = Set.toList . Set.fromList . concat $ f
    eq l = do
        f' <-  mkOr =<< mapM stateToAST f
        l' <- litToAST l
        eqTest <- mkXor f' l'
        r <- checkAssumptions [eqTest]
        case r of
            Sat   -> return Nothing  -- not equal
            Unsat -> return $ Just l -- equal
            Undef -> error ("SMT result unknown: "++show eqTest)

filterNew :: [APLiteral VarName] -> [AST] -> SMTSynth [AST]
filterNew existing = filterM notExists
    where
    existing' = existing ++ map negateAP existing
    notExists a = do
        es <- mapM (eq a) existing'
        return . not . or $ es
    eq a e = do
        e' <- litToAST e
        eqTest <- mkXor a e'
        r <- checkAssumptions [eqTest]
        case r of
            Sat   -> return False -- not equal
            Unsat -> return True  -- equal
            Undef -> error ("SMT result unknown: "++show eqTest)

firstJusts :: [Maybe a] -> Maybe a
firstJusts = msum