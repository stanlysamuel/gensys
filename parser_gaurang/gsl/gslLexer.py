# Generated from gsl.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\6\b)\n")
        buf.write("\b\r\b\16\b*\3\t\6\t.\n\t\r\t\16\t/\3\n\6\n\63\n\n\r\n")
        buf.write("\16\n\64\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\3\2\5\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\2:\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\3\25\3\2\2\2\5\27\3\2\2\2\7\32\3\2\2\2\t")
        buf.write("\34\3\2\2\2\13\36\3\2\2\2\r\"\3\2\2\2\17(\3\2\2\2\21-")
        buf.write("\3\2\2\2\23\62\3\2\2\2\25\26\7=\2\2\26\4\3\2\2\2\27\30")
        buf.write("\7<\2\2\30\31\7?\2\2\31\6\3\2\2\2\32\33\7-\2\2\33\b\3")
        buf.write("\2\2\2\34\35\7/\2\2\35\n\3\2\2\2\36\37\7K\2\2\37 \7p\2")
        buf.write("\2 !\7v\2\2!\f\3\2\2\2\"#\7T\2\2#$\7g\2\2$%\7c\2\2%&\7")
        buf.write("n\2\2&\16\3\2\2\2\')\t\2\2\2(\'\3\2\2\2)*\3\2\2\2*(\3")
        buf.write("\2\2\2*+\3\2\2\2+\20\3\2\2\2,.\t\3\2\2-,\3\2\2\2./\3\2")
        buf.write("\2\2/-\3\2\2\2/\60\3\2\2\2\60\22\3\2\2\2\61\63\t\4\2\2")
        buf.write("\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2")
        buf.write("\2\65\66\3\2\2\2\66\67\b\n\2\2\67\24\3\2\2\2\6\2*/\64")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class gslLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    IDENTIFIER = 7
    NUM = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':='", "'+'", "'-'", "'Int'", "'Real'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "IDENTIFIER", 
                  "NUM", "WS" ]

    grammarFileName = "gsl.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


