# Generated from gsl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gslParser import gslParser
else:
    from gslParser import gslParser

# This class defines a complete listener for a parse tree produced by gslParser.
class gslListener(ParseTreeListener):

    # Enter a parse tree produced by gslParser#prog.
    def enterProg(self, ctx:gslParser.ProgContext):
        pass

    # Exit a parse tree produced by gslParser#prog.
    def exitProg(self, ctx:gslParser.ProgContext):
        pass


    # Enter a parse tree produced by gslParser#expr1.
    def enterExpr1(self, ctx:gslParser.Expr1Context):
        pass

    # Exit a parse tree produced by gslParser#expr1.
    def exitExpr1(self, ctx:gslParser.Expr1Context):
        pass


    # Enter a parse tree produced by gslParser#expr2.
    def enterExpr2(self, ctx:gslParser.Expr2Context):
        pass

    # Exit a parse tree produced by gslParser#expr2.
    def exitExpr2(self, ctx:gslParser.Expr2Context):
        pass


    # Enter a parse tree produced by gslParser#type.
    def enterType(self, ctx:gslParser.TypeContext):
        pass

    # Exit a parse tree produced by gslParser#type.
    def exitType(self, ctx:gslParser.TypeContext):
        pass



del gslParser