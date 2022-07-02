# Generated from gsl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gslParser import gslParser
else:
    from gslParser import gslParser

# This class defines a complete generic visitor for a parse tree produced by gslParser.

class gslVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gslParser#prog.
    def visitProg(self, ctx:gslParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#expr1.
    def visitExpr1(self, ctx:gslParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#expr2.
    def visitExpr2(self, ctx:gslParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#type.
    def visitType(self, ctx:gslParser.TypeContext):
        return self.visitChildren(ctx)



