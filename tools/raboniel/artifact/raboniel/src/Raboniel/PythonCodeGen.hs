{-# LANGUAGE LambdaCase #-}
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE TupleSections #-}
{-# LANGUAGE ScopedTypeVariables #-}

module Raboniel.PythonCodeGen where

import Data.Text (Text)
import Data.Text.Lazy.Builder (Builder, fromString, toLazyText)
import Data.Text.Lazy (toStrict)
import Numeric ( showFFloat )
import Data.List (intersperse)

import Raboniel.Expression
import Raboniel.KISSparser (MState(..))
import Raboniel.Context ( StateSimplificationMode(..), Synth, getStateVars, getInputVars, getSimplify )


bExprToPython :: BExpr VarName -> Builder
bExprToPython = \case
    Eq e1 e2 -> iExprToPython e1 <> " == " <> iExprToPython e2
    Le e1 e2 -> iExprToPython e1 <> " <= " <> iExprToPython e2
    Ge e1 e2 -> iExprToPython e1 <> " >= " <> iExprToPython e2
    Lt e1 e2 -> iExprToPython e1 <> " < "  <> iExprToPython e2
    Gt e1 e2 -> iExprToPython e1 <> " > "  <> iExprToPython e2

iExprToPython :: IntExpr VarName -> Builder
iExprToPython = \case
    Var i -> fromString i
    VarR i -> "r_" <> fromString i
    Const c -> fromString (show c)
    ConstR c -> fromString (showFFloat Nothing c "")
    Add e1 e2 -> "(" <> iExprToPython e1 <> " + " <> iExprToPython e2 <> ")"
    Sub e1 e2 -> "(" <> iExprToPython e1 <> " - " <> iExprToPython e2 <> ")"
    Mul e1 e2 -> "(" <> iExprToPython e1 <> " * " <> iExprToPython e2 <> ")"
    Div e1 e2 -> "(" <> iExprToPython e1 <> " / " <> iExprToPython e2 <> ")"
    Mod e1 e2 -> "(" <> iExprToPython e1 <> " % " <> iExprToPython e2 <> ")"

aPToPython :: APLiteral VarName -> Builder
aPToPython = \case
    Positive e -> bExprToPython e
    Negative e -> "not (" <> bExprToPython e <> ")"


stateToPython :: State VarName -> Builder
stateToPython = mconcat . intersperse " && " . map aPToPython

updateToPython :: Update VarName -> Builder
updateToPython (Update x e) = case x of
    VarInt v -> fromString v <> "_prime" <> " = " <> iExprToPython e <> "\n"
    VarReal v -> "r_" <> fromString v <> "_prime" <> " = " <> iExprToPython e <> "\n"

transitionToPython :: (MState, [State String], [Update String], MState) -> Builder
transitionToPython (s0, ps, us, s1) = condition <> nextState <> updates <> "\n"
    where
    condition = "    if state == " <> mStateToPython s0 <> " and (" <> psT' <> "):\n"
    psT' = mconcat . intersperse " or " $ psT
    psT = map (("("<>) . (<>")") . mconcat . intersperse " and " . map aPToPython) ps
    nextState = "      state_prime = " <> mStateToPython s1 <> "\n"
    updates = mconcat . map (("      "<>) . updateToPython) $ us


mStateToPython :: MState -> Builder
mStateToPython (MState i) = fromString . show $ i

toPythonFunction :: [(MState, [State String], [Update String], MState)] -> Synth Builder
toPythonFunction trans = do
    stateVars <- getStateVars
    inputVars <- getInputVars
    -- "def run(init, inputs):\n  state = 0\n"
    let initialization = mconcat . map (\s -> "  "<>fromString s<>" = init['"<>fromString s<>"']\n") $ stateVars
    let readInputs = mconcat . map (\s -> "    "<>fromString s<>" = _input['"<>fromString s<>"']\n") $ inputVars
    let update = "    state = state_prime\n" <> (mconcat . map (\s -> "    "<>fromString s<>" = "<>fromString s<>"_prime\n")) stateVars
    let yield = "    yield {"<>(mconcat.intersperse ", ".map (\s -> "'"<>fromString s<>"':"<>fromString s) $ stateVars)<>"}\n"
    let loop = "  for _input in inputs:\n" <> readInputs <> (mconcat . map transitionToPython) trans <> update <> yield
    return $ "def run(init, inputs):\n  state = 0\n" <> initialization <> loop

toPython :: [(MState, [State String], [Update String], MState)] -> Synth Builder
toPython trans = do
    run <- toPythonFunction trans
    return $ "import json\n"<>
             "import readline\n\n"<>
             run<>"\n\n"<>
             "def main():\n"<>
             "  def readInputs():\n"<>
             "    while True:\n"<>
             "      raw = input(\"inputs: \")\n"<>
             "      if raw == \"exit\":\n"<>
             "        break\n"<>
             "      yield json.loads(raw)\n\n"<>
             "  inputs = readInputs()\n"<>
             "  raw = input(\"initial state: \")\n"<>
             "  init = json.loads(raw)\n"<>
             "  outputs = run(init, inputs)\n"<>
             "  for o in outputs:\n"<>
             "    print(\"state: \", o)\n"<>
             "    print(\"-----\")\n\n"<>
             "if __name__ == \"__main__\":\n"<>
             "    main()\n\n"
