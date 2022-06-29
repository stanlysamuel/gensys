# Generated from con.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,45,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,4,
        5,30,8,5,11,5,12,5,31,1,6,4,6,35,8,6,11,6,12,6,36,1,7,4,7,40,8,7,
        11,7,12,7,41,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,
        0,3,4,0,48,57,65,90,95,95,97,122,1,0,48,57,3,0,9,10,13,13,32,32,
        47,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,
        11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,20,1,0,0,0,5,
        22,1,0,0,0,7,24,1,0,0,0,9,26,1,0,0,0,11,29,1,0,0,0,13,34,1,0,0,0,
        15,39,1,0,0,0,17,18,5,58,0,0,18,19,5,61,0,0,19,2,1,0,0,0,20,21,5,
        43,0,0,21,4,1,0,0,0,22,23,5,45,0,0,23,6,1,0,0,0,24,25,5,42,0,0,25,
        8,1,0,0,0,26,27,5,47,0,0,27,10,1,0,0,0,28,30,7,0,0,0,29,28,1,0,0,
        0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,12,1,0,0,0,33,35,
        7,1,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,
        37,14,1,0,0,0,38,40,7,2,0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,
        0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,6,7,0,0,44,16,1,0,0,0,4,
        0,31,36,41,1,6,0,0
    ]

class conLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    IDENTIFIER = 6
    INT = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "IDENTIFIER", 
                  "INT", "WS" ]

    grammarFileName = "con.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


