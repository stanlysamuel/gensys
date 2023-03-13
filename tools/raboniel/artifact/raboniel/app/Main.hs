{-# LANGUAGE DataKinds          #-}
{-# LANGUAGE DeriveGeneric      #-}
{-# LANGUAGE FlexibleInstances  #-}
{-# LANGUAGE OverloadedStrings  #-}
{-# LANGUAGE StandaloneDeriving #-}
{-# LANGUAGE TypeOperators      #-}
{-# LANGUAGE DeriveDataTypeable #-}
{-# LANGUAGE LambdaCase #-}

module Main where

import System.Environment
import Data.List.NonEmpty ( NonEmpty(..) )
import Type.Reflection ( Typeable )

import Options.Generic
    ( Generic,
      unwrapRecord,
      type (:::),
      type (<!>),
      type (<?>),
      ParseField,
      ParseFields,
      ParseRecord,
      Unwrapped,
      Wrapped )

import Raboniel.Synthesis (synthesize, callCmd)
import Raboniel.Context
    ( Config(Config),
      DeleteTmpFiles,
      MinimizationMode,
      StateSimplificationMode,
      OutputFormatMode)
import qualified Raboniel.Context as Ctx


data Minimize = Always | Never | System
  deriving (Eq, Show, Read, Generic)

instance ParseField Minimize
instance ParseRecord Minimize
instance ParseFields Minimize

data KeepTmp = All | TSL | None
  deriving (Eq, Show, Read, Generic)

instance ParseField KeepTmp
instance ParseRecord KeepTmp
instance ParseFields KeepTmp

data OutputFormat = PseudoCode | Python
  deriving (Eq, Show, Read, Generic)

instance ParseField OutputFormat
instance ParseRecord OutputFormat
instance ParseFields OutputFormat

data CLIOptions w = CLIOptions {
  minimize :: w ::: Minimize <?> "Minimize machine states (Always | Never | System) default: System" <!> "System",
  keep :: w ::: KeepTmp <?> "Keep temporary files (All | TSL | None) default: None" <!> "None",
  simplify :: w ::: Bool <?> "Simplify the final system.",
  noStateExpansion :: w ::: Bool <?> "Do not expand non determinism in states.",
  output :: w ::: OutputFormat <?> "Output format (Python | PseudoCode) default: Python" <!> "Python",
  spec :: w ::: FilePath <?> "TSL specification file"
} deriving (Generic)

instance ParseRecord (CLIOptions Wrapped)
deriving instance Show (CLIOptions Unwrapped)

toConfig :: CLIOptions Unwrapped -> (Config, FilePath)
toConfig o = (Config (toMinimizationMode.minimize $ o) (simplify o) (noStateExpansion o) (toDeleteTmpFiles.keep $ o) (toOutputMode.output $ o) , spec o)

toDeleteTmpFiles :: KeepTmp -> DeleteTmpFiles
toDeleteTmpFiles = \case
  None -> Ctx.DeleteAll 
  TSL -> Ctx.KeepTSL
  All -> Ctx.KeepAll 

toMinimizationMode :: Minimize -> MinimizationMode
toMinimizationMode = \case
  Always -> Ctx.MinimizeAlways 
  Never -> Ctx.MinimizeNever
  System -> Ctx.MinimizeSystem

toStateSimplificationMode :: Bool -> StateSimplificationMode
toStateSimplificationMode = \case
  True -> Ctx.EliminateUneccessaryParts
  False -> Ctx.NoSimplification 

toOutputMode :: OutputFormat -> OutputFormatMode 
toOutputMode = \case
  Python -> Ctx.PythonFormat 
  PseudoCode -> Ctx.PseudoCodeFormat 

main :: IO ()
main = do
    x <- unwrapRecord "Raboniel synthesis tool"
    let (config, specFile) = toConfig x
    synthesize config specFile
