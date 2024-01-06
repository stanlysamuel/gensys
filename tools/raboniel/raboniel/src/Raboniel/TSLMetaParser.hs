{-# LANGUAGE OverloadedStrings #-}

module Raboniel.TSLMetaParser (parseTSLAnnotations, parseStateInvariant, parseStateInvariants) where

import Prelude hiding ( lines )
import Text.Megaparsec
import Text.Megaparsec.Char
    ( alphaNumChar, char, letterChar, space1, string, digitChar )
import Text.Megaparsec.Char.Lexer (space, skipLineComment, skipBlockComment, lexeme)
import Data.Text (Text, pack, lines, strip, isPrefixOf, isInfixOf)
import Data.Void
import Text.Read (readMaybe)
import Data.Char (toUpper)
import Data.Functor ( ($>) )
import Data.Bifunctor ( first )
import Data.List (find)
import qualified Data.Set as Set
import Data.Maybe ( fromMaybe )

import Raboniel.Expression

type Parser = Parsec Void Text

lexeme' = lexeme sc
    where
    sc :: Parser ()
    sc = space space1 (skipLineComment "//") (skipBlockComment "/*" "*/")


intParser :: Parser (IntExpr String)
intParser =
      (lexeme' "(" >> intParser <* lexeme' ")" )
  <|> lexeme' ("r_"  >> VarR <$> identParser)
  <|> lexeme' ("i"   >> (Const <$> number) <* "()")
  <|> lexeme' ("im"   >> (Const . (*(-1)) <$> number) <* "()")
  <|> lexeme' ("r"   >> (ConstR <$> number) <* "()"
  <|> lexeme' ("rm"   >> (ConstR . (*(-1)) <$> number) <* "()"))
  <|> (lexeme' "add" >> (Add <$> intParser <*> intParser))
  <|> (lexeme' "sub" >> (Sub <$> intParser <*> intParser))
  <|> (lexeme' "mul" >> (Mul <$> intParser <*> intParser))
  <|> (lexeme' "div" >> (Div <$> intParser <*> intParser))
  <|> (lexeme' "mod" >> (Mod <$> intParser <*> intParser))
  <|> lexeme' (Var <$> identParser)

  where
  number :: Read i => Parser i
  number = do
    s <- some (digitChar <|> char '.')
    case readMaybe s of
      Just i -> return i
      Nothing -> failure Nothing Set.empty --TODO better error handling


predicateParser :: Parser (BExpr String)
predicateParser =
      (lexeme' "eq" >> (Eq <$> intParser <*> intParser))
  <|> (lexeme' "le" >> (Le <$> intParser <*> intParser))
  <|> (lexeme' "ge" >> (Ge <$> intParser <*> intParser))
  <|> (lexeme' "lt" >> (Lt <$> intParser <*> intParser))
  <|> (lexeme' "gt" >> (Gt <$> intParser <*> intParser))


identParser :: Parser String
identParser = lexeme' $ some char'
    where
    char' = alphaNumChar <|> char '_' <|> char '@' <|> char '\'' <|> char '.'

invariantParser :: Parser (APLiteral String)
invariantParser =
         Negative <$> (lexeme' "!" >> lexeme' "(" >> predicateParser <* lexeme' ")" <* lexeme' ";")
    <|> (Positive <$> (predicateParser <* lexeme' ";"))

parseStateInvariant :: Text -> Either Text (APLiteral String)
parseStateInvariant line =
    first (pack . errorBundlePretty) $ runParser invariantParser "" line

parseStateInvariants :: [Text] -> Either Text [APLiteral String]
parseStateInvariants = mapM parseStateInvariant

comma = lexeme' $ char ','

stateVariablesParser :: Parser [String]
stateVariablesParser = lexeme' "//-- State:" >> sepBy1 identParser comma

inputVariablesParser :: Parser [String]
inputVariablesParser = lexeme' "//-- Inputs:" >> sepBy1 identParser comma

parseStateVariables :: Text -> Either Text [String]
parseStateVariables line = first (pack . errorBundlePretty) $ runParser stateVariablesParser "" line

parseInputVariables :: Text -> Either Text [String]
parseInputVariables line = first (pack . errorBundlePretty) $ runParser inputVariablesParser "" line

-- isStateLine = 

maybeToRight :: b -> Maybe a -> Either b a
maybeToRight _ (Just x) = Right x
maybeToRight y Nothing  = Left y


parseTSLAnnotations :: Text -> Either Text ([String], [String], [APLiteral String])
parseTSLAnnotations file = do
    stateLine <- maybeToRight "No state annotation found!" stateLine'
    stateVars <- parseStateVariables stateLine
    inputVars <- case inputLine' of
        Just inputLine -> parseInputVariables inputLine
        Nothing -> Right []
    invs <- parseStateInvariants invariantLines
    return (stateVars, inputVars, invs)
    where
    stateLine' = find (isPrefixOf "//-- State:") lines'
    inputLine' = find (isPrefixOf "//-- Inputs:") lines'
    invariantLines = filter (isInfixOf "/* INV */") lines'
    lines' = map strip . lines $ file

