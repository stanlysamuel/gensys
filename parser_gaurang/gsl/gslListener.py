# Generated from gsl.g4 by ANTLR 4.9.1
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


    # Enter a parse tree produced by gslParser#declList.
    def enterDeclList(self, ctx:gslParser.DeclListContext):
        pass

    # Exit a parse tree produced by gslParser#declList.
    def exitDeclList(self, ctx:gslParser.DeclListContext):
        pass


    # Enter a parse tree produced by gslParser#decl.
    def enterDecl(self, ctx:gslParser.DeclContext):
        pass

    # Exit a parse tree produced by gslParser#decl.
    def exitDecl(self, ctx:gslParser.DeclContext):
        pass


    # Enter a parse tree produced by gslParser#assignmentList.
    def enterAssignmentList(self, ctx:gslParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by gslParser#assignmentList.
    def exitAssignmentList(self, ctx:gslParser.AssignmentListContext):
        pass


    # Enter a parse tree produced by gslParser#assignment.
    def enterAssignment(self, ctx:gslParser.AssignmentContext):
        pass

    # Exit a parse tree produced by gslParser#assignment.
    def exitAssignment(self, ctx:gslParser.AssignmentContext):
        pass


    # Enter a parse tree produced by gslParser#expr.
    def enterExpr(self, ctx:gslParser.ExprContext):
        pass

    # Exit a parse tree produced by gslParser#expr.
    def exitExpr(self, ctx:gslParser.ExprContext):
        pass


    # Enter a parse tree produced by gslParser#op.
    def enterOp(self, ctx:gslParser.OpContext):
        pass

    # Exit a parse tree produced by gslParser#op.
    def exitOp(self, ctx:gslParser.OpContext):
        pass


    # Enter a parse tree produced by gslParser#type.
    def enterType(self, ctx:gslParser.TypeContext):
        pass

    # Exit a parse tree produced by gslParser#type.
    def exitType(self, ctx:gslParser.TypeContext):
        pass



del gslParser