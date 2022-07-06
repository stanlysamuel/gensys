from antlr4 import *
from gslParser import gslParser
from gslVisitor import gslVisitor


class gslToZ3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gslParser#prog.
    def visitProg(self, ctx:gslParser.ProgContext):
        print("PRINT")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#expr1.
    def visitExpr1(self, ctx:gslParser.Expr1Context):
        print("PRINT")  
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#expr2.
    def visitExpr2(self, ctx:gslParser.Expr2Context):
        print("PRINT")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#type.
    def visitType(self, ctx:gslParser.TypeContext):
        print("PRINT")
        return self.visitChildren(ctx)