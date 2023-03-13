{-# LANGUAGE LambdaCase #-}
{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE OverloadedStrings #-}

{-# LANGUAGE DeriveFunctor #-}
{-# LANGUAGE DeriveFoldable #-}
module Raboniel.Expression where

import Data.Foldable ( find, toList )
import Data.Maybe ( fromMaybe )
import Z3.Monad (MonadZ3, AST, mkIntVar, Symbol, mkInteger, mkAdd, mkSub, mkMul, mkDiv, mkMod, mkNot, mkEq, substitute, mkLe, mkLt, mkGe, mkGt, mkRealVar, mkRealNum, Logic (QF_ABV))

import Data.Set (Set)
import qualified Data.Set as Set
import Data.Text (Text)
import Data.Text.Lazy.Builder (Builder, fromString, toLazyText)
import Data.Text.Lazy (toStrict)
import Data.List (intersperse)
import Numeric ( showFFloat )

type VarName = String

data IntExpr a =
    Var a |
    VarR a |
    Const Integer |
    ConstR Double |
    Add (IntExpr a) (IntExpr a) |
    Sub (IntExpr a) (IntExpr a) |
    Mul (IntExpr a) (IntExpr a) |
    Div (IntExpr a) (IntExpr a) |
    Mod (IntExpr a) (IntExpr a)
    deriving (Show, Eq, Functor, Foldable, Ord)

data BExpr a =
    Eq (IntExpr a) (IntExpr a) |
    Le (IntExpr a) (IntExpr a) |
    Ge (IntExpr a) (IntExpr a) |
    Lt (IntExpr a) (IntExpr a) |
    Gt (IntExpr a) (IntExpr a)
    deriving (Show, Eq, Functor, Foldable, Ord)

data Variable a =
    VarInt a |
    VarReal a
    deriving (Show, Eq, Functor, Ord)


getVarLabel :: Variable a -> a
getVarLabel = \case
    VarInt x -> x
    VarReal x -> x

data Update a = Update (Variable a) (IntExpr a)
    deriving (Show, Eq, Ord)

data APLiteral a = Positive (BExpr a) |
                   Negative (BExpr a)
                   deriving (Show, Eq, Functor, Foldable, Ord)

type State a = [APLiteral a]

data Transition a = Transition (State a) [Update a] (State a)
    deriving (Show, Eq, Ord)

negateAP :: APLiteral a -> APLiteral a
negateAP = \case 
    Positive e -> Negative e
    Negative e -> Positive e

substituteInt :: (a -> IntExpr b) -> IntExpr a -> IntExpr b
substituteInt f = \case
    Var i -> f i
    VarR i -> f i
    Const c -> Const c
    ConstR c -> ConstR c
    Add e1 e2 -> Add (substituteInt f e1) (substituteInt f e2)
    Sub e1 e2 -> Sub (substituteInt f e1) (substituteInt f e2)
    Mul e1 e2 -> Mul (substituteInt f e1) (substituteInt f e2)
    Div e1 e2 -> Div (substituteInt f e1) (substituteInt f e2)
    Mod e1 e2 -> Mod (substituteInt f e1) (substituteInt f e2)

substituteB :: (a -> IntExpr b) -> BExpr a -> BExpr b
substituteB f = \case
    Eq e1 e2 -> Eq (substituteInt f e1) (substituteInt f e2)
    Le e1 e2 -> Le (substituteInt f e1) (substituteInt f e2)
    Ge e1 e2 -> Ge (substituteInt f e1) (substituteInt f e2)
    Lt e1 e2 -> Lt (substituteInt f e1) (substituteInt f e2)
    Gt e1 e2 -> Gt (substituteInt f e1) (substituteInt f e2)

weakestPrecondition :: Eq a => [Update a] -> APLiteral a -> APLiteral a
weakestPrecondition us = \case
    Positive e -> Positive (substituteB f e)
    Negative e -> Negative (substituteB f e)
    where
    f i = let u = find (\case Update x _-> i==getVarLabel x) us in
        maybe (Var i) (\case Update _ e -> e) u


bExprToTextBuilder :: BExpr VarName -> Builder
bExprToTextBuilder = \case
    Eq e1 e2 -> "eq "  <> iExprToTextBuilder e1 <> " " <> iExprToTextBuilder e2
    Le e1 e2 -> "le " <> iExprToTextBuilder e1 <> " " <> iExprToTextBuilder e2
    Ge e1 e2 -> "ge " <> iExprToTextBuilder e1 <> " " <> iExprToTextBuilder e2
    Lt e1 e2 -> "lt " <> iExprToTextBuilder e1 <> " " <> iExprToTextBuilder e2
    Gt e1 e2 -> "gt " <> iExprToTextBuilder e1 <> " " <> iExprToTextBuilder e2

iExprToTextBuilder :: IntExpr VarName -> Builder
iExprToTextBuilder = \case
    Var i -> fromString i
    VarR i -> "r_" <> fromString i
    Const c | c>=0  -> "i" <> fromString (show c) <> "()"
    Const c | c<0   -> "im" <> fromString (show $ c*(-1)) <> "()"
    ConstR c | c>=0 -> "r" <> fromString (showFFloat Nothing c "") <> "()"
    ConstR c | c<0  -> "rm" <> fromString (showFFloat Nothing (c*(-1)) "") <> "()"
    Add e1 e2 -> "(add " <> iExprToTextBuilder e1 <> " " <> iExprToTextBuilder e2 <> ")"
    Sub e1 e2 -> "(sub " <> iExprToTextBuilder e1 <> " " <> iExprToTextBuilder e2 <> ")"
    Mul e1 e2 -> "(mul " <> iExprToTextBuilder e1 <> " " <> iExprToTextBuilder e2 <> ")"
    Div e1 e2 -> "(div " <> iExprToTextBuilder e1 <> " " <> iExprToTextBuilder e2 <> ")"
    Mod e1 e2 -> "(mod " <> iExprToTextBuilder e1 <> " " <> iExprToTextBuilder e2 <> ")"

aPToTextBuilder :: APLiteral VarName -> Builder
aPToTextBuilder = \case
    Positive e -> bExprToTextBuilder e
    Negative e -> "!(" <> bExprToTextBuilder e <> ")"

stateToTextBuilder :: State VarName -> Builder
stateToTextBuilder = mconcat . intersperse " && " . map aPToTextBuilder

updateToTextBuilder :: Update VarName -> Builder
updateToTextBuilder (Update x e) = case x of
    VarInt v -> "[ " <> fromString v <> " <- " <> iExprToTextBuilder e <> " ]"
    VarReal v -> "[ r_" <> fromString v <> " <- " <> iExprToTextBuilder e <> " ]"
     

transitionToTextBuilder :: Transition VarName -> Builder
transitionToTextBuilder (Transition s1 u s2) = 
    stateToTextBuilder s1 <> " && " <> (mconcat . intersperse " && " . map updateToTextBuilder $ u) <>
    " -> X " <> stateToTextBuilder s2 <> ";"

negTransitionToTextBuilder :: Transition VarName -> Builder
negTransitionToTextBuilder (Transition [] u s2) = 
    (mconcat . intersperse " && " . map updateToTextBuilder $ u) <>
    " -> X !(" <> stateToTextBuilder s2 <> ");"
negTransitionToTextBuilder (Transition s1 u s2) = 
    stateToTextBuilder s1 <> " && " <> (mconcat . intersperse " && " . map updateToTextBuilder $ u) <>
    " -> X !(" <> stateToTextBuilder s2 <> ");"

transitionToText :: Transition VarName -> Text
transitionToText = toStrict . toLazyText . transitionToTextBuilder

negTransitionToText :: Transition VarName -> Text
negTransitionToText = toStrict . toLazyText . negTransitionToTextBuilder

stateToText :: State VarName -> Text
stateToText = toStrict . toLazyText . stateToTextBuilder

negStateToText :: State VarName -> Text
negStateToText s = toStrict . toLazyText $ "!(" <> stateToTextBuilder s <> ");"

aPToText :: APLiteral VarName -> Text
aPToText = toStrict . toLazyText . aPToTextBuilder

freeVariables :: APLiteral VarName -> [VarName]
freeVariables = toList
