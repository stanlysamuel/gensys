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


    # Visit a parse tree produced by gslParser#declList1.
    def visitDeclList1(self, ctx:gslParser.DeclList1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#decl.
    def visitDecl(self, ctx:gslParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#declList2.
    def visitDeclList2(self, ctx:gslParser.DeclList2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#identifierList.
    def visitIdentifierList(self, ctx:gslParser.IdentifierListContext):
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


    # Visit a parse tree produced by gslParser#UnaryOp.
    def visitUnaryOp(self, ctx:gslParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#BracketFormula.
    def visitBracketFormula(self, ctx:gslParser.BracketFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#BinaryLogicOp.
    def visitBinaryLogicOp(self, ctx:gslParser.BinaryLogicOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#Atom.
    def visitAtom(self, ctx:gslParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#BinaryOp.
    def visitBinaryOp(self, ctx:gslParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#predicate.
    def visitPredicate(self, ctx:gslParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gslParser#relOp.
    def visitRelOp(self, ctx:gslParser.RelOpContext):
        return self.visitChildren(ctx)



del gslParser