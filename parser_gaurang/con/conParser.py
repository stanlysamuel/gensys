# Generated from con.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,16,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        14,8,1,1,1,0,0,2,0,2,0,2,1,0,2,3,1,0,4,5,15,0,4,1,0,0,0,2,13,1,0,
        0,0,4,5,3,2,1,0,5,1,1,0,0,0,6,7,5,6,0,0,7,8,5,1,0,0,8,14,5,6,0,0,
        9,10,7,0,0,0,10,14,5,7,0,0,11,12,7,1,0,0,12,14,5,7,0,0,13,6,1,0,
        0,0,13,9,1,0,0,0,13,11,1,0,0,0,14,3,1,0,0,0,1,13
    ]

class conParser ( Parser ):

    grammarFileName = "con.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER", "INT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    IDENTIFIER=6
    INT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(conParser.ExprContext,0)


        def getRuleIndex(self):
            return conParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = conParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(conParser.IDENTIFIER)
            else:
                return self.getToken(conParser.IDENTIFIER, i)

        def INT(self):
            return self.getToken(conParser.INT, 0)

        def getRuleIndex(self):
            return conParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = conParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [conParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(conParser.IDENTIFIER)
                self.state = 7
                self.match(conParser.T__0)
                self.state = 8
                self.match(conParser.IDENTIFIER)
                pass
            elif token in [conParser.T__1, conParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                _la = self._input.LA(1)
                if not(_la==conParser.T__1 or _la==conParser.T__2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 10
                self.match(conParser.INT)
                pass
            elif token in [conParser.T__3, conParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 11
                _la = self._input.LA(1)
                if not(_la==conParser.T__3 or _la==conParser.T__4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 12
                self.match(conParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





