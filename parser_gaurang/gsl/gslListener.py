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


    # Enter a parse tree produced by gslParser#declList.
    def enterDeclList(self, ctx:gslParser.DeclListContext):
        pass

    # Exit a parse tree produced by gslParser#declList.
    def exitDeclList(self, ctx:gslParser.DeclListContext):
        pass


    # Enter a parse tree produced by gslParser#declList1.
    def enterDeclList1(self, ctx:gslParser.DeclList1Context):
        pass

    # Exit a parse tree produced by gslParser#declList1.
    def exitDeclList1(self, ctx:gslParser.DeclList1Context):
        pass


    # Enter a parse tree produced by gslParser#decl.
    def enterDecl(self, ctx:gslParser.DeclContext):
        pass

    # Exit a parse tree produced by gslParser#decl.
    def exitDecl(self, ctx:gslParser.DeclContext):
        pass


    # Enter a parse tree produced by gslParser#declList2.
    def enterDeclList2(self, ctx:gslParser.DeclList2Context):
        pass

    # Exit a parse tree produced by gslParser#declList2.
    def exitDeclList2(self, ctx:gslParser.DeclList2Context):
        pass


    # Enter a parse tree produced by gslParser#identifierList.
    def enterIdentifierList(self, ctx:gslParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by gslParser#identifierList.
    def exitIdentifierList(self, ctx:gslParser.IdentifierListContext):
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


    # Enter a parse tree produced by gslParser#cmoveList.
    def enterCmoveList(self, ctx:gslParser.CmoveListContext):
        pass

    # Exit a parse tree produced by gslParser#cmoveList.
    def exitCmoveList(self, ctx:gslParser.CmoveListContext):
        pass


    # Enter a parse tree produced by gslParser#cmove.
    def enterCmove(self, ctx:gslParser.CmoveContext):
        pass

    # Exit a parse tree produced by gslParser#cmove.
    def exitCmove(self, ctx:gslParser.CmoveContext):
        pass


    # Enter a parse tree produced by gslParser#environmentMove.
    def enterEnvironmentMove(self, ctx:gslParser.EnvironmentMoveContext):
        pass

    # Exit a parse tree produced by gslParser#environmentMove.
    def exitEnvironmentMove(self, ctx:gslParser.EnvironmentMoveContext):
        pass


    # Enter a parse tree produced by gslParser#specification.
    def enterSpecification(self, ctx:gslParser.SpecificationContext):
        pass

    # Exit a parse tree produced by gslParser#specification.
    def exitSpecification(self, ctx:gslParser.SpecificationContext):
        pass


    # Enter a parse tree produced by gslParser#type.
    def enterType(self, ctx:gslParser.TypeContext):
        pass

    # Exit a parse tree produced by gslParser#type.
    def exitType(self, ctx:gslParser.TypeContext):
        pass


    # Enter a parse tree produced by gslParser#z3Formula.
    def enterZ3Formula(self, ctx:gslParser.Z3FormulaContext):
        pass

    # Exit a parse tree produced by gslParser#z3Formula.
    def exitZ3Formula(self, ctx:gslParser.Z3FormulaContext):
        pass


    # Enter a parse tree produced by gslParser#predicateList.
    def enterPredicateList(self, ctx:gslParser.PredicateListContext):
        pass

    # Exit a parse tree produced by gslParser#predicateList.
    def exitPredicateList(self, ctx:gslParser.PredicateListContext):
        pass


    # Enter a parse tree produced by gslParser#UnaryOp.
    def enterUnaryOp(self, ctx:gslParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by gslParser#UnaryOp.
    def exitUnaryOp(self, ctx:gslParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by gslParser#BracketFormula.
    def enterBracketFormula(self, ctx:gslParser.BracketFormulaContext):
        pass

    # Exit a parse tree produced by gslParser#BracketFormula.
    def exitBracketFormula(self, ctx:gslParser.BracketFormulaContext):
        pass


    # Enter a parse tree produced by gslParser#BinaryLogicOp.
    def enterBinaryLogicOp(self, ctx:gslParser.BinaryLogicOpContext):
        pass

    # Exit a parse tree produced by gslParser#BinaryLogicOp.
    def exitBinaryLogicOp(self, ctx:gslParser.BinaryLogicOpContext):
        pass


    # Enter a parse tree produced by gslParser#Atom.
    def enterAtom(self, ctx:gslParser.AtomContext):
        pass

    # Exit a parse tree produced by gslParser#Atom.
    def exitAtom(self, ctx:gslParser.AtomContext):
        pass


    # Enter a parse tree produced by gslParser#BinaryOp.
    def enterBinaryOp(self, ctx:gslParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by gslParser#BinaryOp.
    def exitBinaryOp(self, ctx:gslParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by gslParser#predicate.
    def enterPredicate(self, ctx:gslParser.PredicateContext):
        pass

    # Exit a parse tree produced by gslParser#predicate.
    def exitPredicate(self, ctx:gslParser.PredicateContext):
        pass


    # Enter a parse tree produced by gslParser#relOp.
    def enterRelOp(self, ctx:gslParser.RelOpContext):
        pass

    # Exit a parse tree produced by gslParser#relOp.
    def exitRelOp(self, ctx:gslParser.RelOpContext):
        pass



del gslParser