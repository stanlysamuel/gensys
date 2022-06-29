# Generated from con.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .conParser import conParser
else:
    from conParser import conParser

# This class defines a complete listener for a parse tree produced by conParser.
class conListener(ParseTreeListener):

    # Enter a parse tree produced by conParser#prog.
    def enterProg(self, ctx:conParser.ProgContext):
        pass

    # Exit a parse tree produced by conParser#prog.
    def exitProg(self, ctx:conParser.ProgContext):
        pass


    # Enter a parse tree produced by conParser#expr.
    def enterExpr(self, ctx:conParser.ExprContext):
        pass

    # Exit a parse tree produced by conParser#expr.
    def exitExpr(self, ctx:conParser.ExprContext):
        pass



del conParser