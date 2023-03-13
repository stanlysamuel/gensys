{-# LANGUAGE OverloadedStrings #-}

module Raboniel.SMTparser where

import Prelude hiding ( lines, lex, putStrLn )
import Data.Text.IO ( putStrLn )
import Text.Megaparsec
import Text.Megaparsec.Char
    ( alphaNumChar, char, letterChar, space1, space, string, digitChar, numberChar )
import Text.Megaparsec.Char.Lexer (skipLineComment, skipBlockComment, lexeme)
import qualified Text.Megaparsec.Char.Lexer as Lexer
import Data.Text (Text, pack, lines, strip, isPrefixOf, isInfixOf)
import Data.Void
import Text.Read (readMaybe)
import Data.Char (toUpper)
import Data.Functor ( ($>) )
import Data.Bifunctor ( first )
import Data.List (find)
import qualified Data.Set as Set
import Data.Maybe ( fromMaybe )
import Control.Monad.IO.Class ( MonadIO(liftIO) )
import Z3.Monad ( AST, astToString )

import Raboniel.Expression
import Raboniel.Z3Expression

type Parser = Parsec Void Text

-- lex = lexeme sc
--     where
--     sc :: Parser ()
--     sc = Lexer.space space1 empty empty

listToAST :: (a -> a -> a) -> [a] -> a
listToAST node xs = foldr node (head xs) (tail xs)


intParser :: Parser (IntExpr VarName)
intParser = 
    --   ("(- " >> (Sub <$> (intParser <* " ") <*> intParser)) <* ")"
  ("(- " >> (Const . (*(-1)) <$> number)) <* ")"
  -- <|> ("(+ " >> (Add <$> (intParser <* " ") <*> intParser)) <* ")"
  <|> ("(+ " >> (listToAST Add <$> sepBy1 intParser (char ' '))) <* ")"
  -- <|> ("(* " >> (Mul <$> (intParser <* " ") <*> intParser)) <* ")"
  <|> ("(* " >> (listToAST Mul <$> sepBy1 intParser (char ' '))) <* ")"
  <|> ("(div " >> (Div <$> (intParser <* " ") <*> intParser)) <* ")"
  <|> ("(mod " >> (Mod <$> (intParser <* " ") <*> intParser)) <* ")"
  <|> (Const <$> number)
  <|> (Var <$> identParser)

  where
  number :: Read i => Parser i
  number = do
    s <- some (digitChar <|> char '.')
    case readMaybe s of
      Just i -> return i
      Nothing -> failure Nothing Set.empty --TODO better error handling

identParser :: Parser VarName
identParser = some char' -- <* "!" <* numberChar
    where
    char' = alphaNumChar <|> char '_' <|> char '@' <|> char '\'' <|> char '.'

predicateParser :: Parser (BExpr VarName)
predicateParser = 
      ("(= "  >> (Eq <$> (intParser <* " ") <*> intParser) <* ")")
  <|> ("(<= " >> (Le <$> (intParser <* " ") <*> intParser) <* ")")
  <|> ("(>= " >> (Ge <$> (intParser <* " ") <*> intParser) <* ")")
  <|> ("(< "  >> (Lt <$> (intParser <* " ") <*> intParser) <* ")")
  <|> ("(> "  >> (Gt <$> (intParser <* " ") <*> intParser) <* ")")

formulaParser :: Parser [[APLiteral VarName]]
formulaParser = "(or " *> sepBy1 conjunctionParser space1 <* ")"
                <|> pure <$> conjunctionParser

conjunctionParser :: Parser [APLiteral VarName]
conjunctionParser = "(and " *> sepBy1 apParser space1 <* ")"
                    <|> pure <$> apParser

apParser :: Parser (APLiteral VarName)
apParser = ("(not " *> (Negative <$> predicateParser) <*  ")")
           <|> Positive <$> predicateParser

parseFormula :: AST -> SMTSynth [[APLiteral VarName]]
parseFormula f = do
    f' <- pack <$> astToString f
    -- liftIO . putStrLn $ f'
    let pr = first errorBundlePretty $ runParser formulaParser "" f'
    case pr of
        Left e -> error e -- This parses a string generated from Z3 if it goes wrong there is a bug in the parser.
        Right f'' -> return f''