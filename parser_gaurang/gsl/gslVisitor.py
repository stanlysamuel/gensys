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


    # Visit a parse tree produced by gslParser#declList.
    def visitDeclList(self, ctx:gslParser.DeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#decl.
    def visitDecl(self, ctx:gslParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#assignmentList.
    def visitAssignmentList(self, ctx:gslParser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#assignment.
    def visitAssignment(self, ctx:gslParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#expr.
    def visitExpr(self, ctx:gslParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#op.
    def visitOp(self, ctx:gslParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#type.
    def visitType(self, ctx:gslParser.TypeContext):
        return self.visitChildren(ctx)



del gslParser