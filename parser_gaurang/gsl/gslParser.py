# Generated from gsl.g4 by ANTLR 4.10.1
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
        4,1,11,38,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,34,8,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,3,
        1,0,3,4,1,0,5,6,1,0,7,8,37,0,11,1,0,0,0,2,24,1,0,0,0,4,33,1,0,0,
        0,6,35,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,
        0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,15,3,4,2,0,15,1,1,
        0,0,0,16,17,3,6,3,0,17,18,5,9,0,0,18,19,5,1,0,0,19,25,1,0,0,0,20,
        21,3,6,3,0,21,22,5,9,0,0,22,23,5,1,0,0,23,25,1,0,0,0,24,16,1,0,0,
        0,24,20,1,0,0,0,25,3,1,0,0,0,26,27,5,9,0,0,27,28,5,2,0,0,28,34,5,
        9,0,0,29,30,7,0,0,0,30,34,5,10,0,0,31,32,7,1,0,0,32,34,5,10,0,0,
        33,26,1,0,0,0,33,29,1,0,0,0,33,31,1,0,0,0,34,5,1,0,0,0,35,36,7,2,
        0,0,36,7,1,0,0,0,3,11,24,33
    ]

class gslParser ( Parser ):

    grammarFileName = "gsl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "':='", "'+'", "'-'", "'*'", "'/'", 
                     "'Int'", "'Real'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "INT", "WS" ]

    RULE_prog = 0
    RULE_expr1 = 1
    RULE_expr2 = 2
    RULE_type = 3

    ruleNames =  [ "prog", "expr1", "expr2", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    IDENTIFIER=9
    INT=10
    WS=11

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

        def expr2(self):
            return self.getTypedRuleContext(gslParser.Expr2Context,0)


        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gslParser.Expr1Context)
            else:
                return self.getTypedRuleContext(gslParser.Expr1Context,i)


        def getRuleIndex(self):
            return gslParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = gslParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gslParser.T__6 or _la==gslParser.T__7:
                self.state = 8
                self.expr1()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.expr2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(gslParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(gslParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return gslParser.RULE_expr1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr1" ):
                listener.enterExpr1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr1" ):
                listener.exitExpr1(self)




    def expr1(self):

        localctx = gslParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr1)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.type_()
                self.state = 17
                self.match(gslParser.IDENTIFIER)
                self.state = 18
                self.match(gslParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.type_()
                self.state = 21
                self.match(gslParser.IDENTIFIER)
                self.state = 22
                self.match(gslParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(gslParser.IDENTIFIER)
            else:
                return self.getToken(gslParser.IDENTIFIER, i)

        def INT(self):
            return self.getToken(gslParser.INT, 0)

        def getRuleIndex(self):
            return gslParser.RULE_expr2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr2" ):
                listener.enterExpr2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr2" ):
                listener.exitExpr2(self)




    def expr2(self):

        localctx = gslParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [gslParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(gslParser.IDENTIFIER)
                self.state = 27
                self.match(gslParser.T__1)
                self.state = 28
                self.match(gslParser.IDENTIFIER)
                pass
            elif token in [gslParser.T__2, gslParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                _la = self._input.LA(1)
                if not(_la==gslParser.T__2 or _la==gslParser.T__3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.match(gslParser.INT)
                pass
            elif token in [gslParser.T__4, gslParser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                _la = self._input.LA(1)
                if not(_la==gslParser.T__4 or _la==gslParser.T__5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 32
                self.match(gslParser.INT)
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


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gslParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = gslParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            _la = self._input.LA(1)
            if not(_la==gslParser.T__6 or _la==gslParser.T__7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





