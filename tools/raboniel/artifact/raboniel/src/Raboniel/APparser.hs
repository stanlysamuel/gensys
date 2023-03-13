{-# LANGUAGE LambdaCase #-}
{-# LANGUAGE OverloadedStrings #-}

module Raboniel.APparser where



import Text.Megaparsec
import Text.Megaparsec.Char
import Data.Text (Text)
import Data.Void
import Text.Read (readMaybe)
import Data.Char (toUpper)
import Data.Functor ( ($>) )
import qualified Data.Set as Set

import Raboniel.Expression

type Parser = Parsec Void Text



parseUpdate :: Parser (Update String)
parseUpdate =
      (string "u0r26" >> Update <$> (VarReal <$> identParser) <*> intParser)
  <|> (string "u0"    >> Update <$> (VarInt  <$> identParser) <*> intParser)


intParser :: Parser (IntExpr String)
intParser =
      (string "0f1dim"  >> (Const . (*(-1)) <$> number)      <* string "1b")
  <|> (string "0f1di"   >> (Const  <$> number)               <* string "1b")
  <|> (string "0f1drm"  >> (ConstR . (*(-1)) <$> number)     <* string "1b")
  <|> (string "0f1dr"   >> (ConstR <$> number)               <* string "1b")
  <|> (string "0f1dadd" >> (Add <$> intParser <*> intParser) <* string "1b")
  <|> (string "0f1dsub" >> (Sub <$> intParser <*> intParser) <* string "1b")
  <|> (string "0f1dmul" >> (Mul <$> intParser <*> intParser) <* string "1b")
  <|> (string "0f1ddiv" >> (Div <$> intParser <*> intParser) <* string "1b")
  <|> (string "0f1dmod" >> (Mod <$> intParser <*> intParser) <* string "1b")
  <|> (string "0r26"    >> VarR <$> identParser)
  <|> (string "0"       >> Var  <$> identParser)

  where
  number :: Read i => Parser i
  number = do
    s <- identParser
    case readMaybe s of
      Just i -> return i
      Nothing -> failure Nothing Set.empty --TODO better error handling


predicateParser
  :: Parser (BExpr String)

predicateParser =
      (string "p0p0eq"  >> (Eq  <$> intParser <*> intParser))
  <|> (string "p0p0le" >> (Le <$> intParser <*> intParser))
  <|> (string "p0p0ge" >> (Ge <$> intParser <*> intParser))
  <|> (string "p0p0lt" >> (Lt <$> intParser <*> intParser))
  <|> (string "p0p0gt" >> (Gt <$> intParser <*> intParser))


identParser :: Parser String
identParser = some identCharParser <* endOfIdentifier
    where
    endOfIdentifier = lookAhead (string " " <|> string "0" <|> string "1" <|> eol)
    identCharParser =
          string "23" $> '0'
      <|> string "24" $> '1'
      <|> string "25" $> '2'
      <|> string "26" $> '_'
      <|> string "27" $> '@'
      <|> string "28" $> '\''
      <|> string "29" $> '.'
      <|> char '2' *> (toUpper <$> alphaNumChar)
      <|> char '3'
      <|> char '4'
      <|> char '5'
      <|> char '6'
      <|> char '7'
      <|> char '8'
      <|> char '9'
      <|> letterChar
