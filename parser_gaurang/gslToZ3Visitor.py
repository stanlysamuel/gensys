from lib2to3.pygram import Symbols
from symtable import SymbolTable
from antlr4 import *
from gsl.gslVisitor import *
from gsl.gslParser import *

class gslToZ3Visitor(gslVisitor): 
    
    symbolTable = []

    # Visit a parse tree produced by gslParser#decl.
    def visitDecl(self, ctx:gslParser.DeclContext):
        # print(ctx.getText())
        self.symbolTable.append(str(ctx.IDENTIFIER()))
        # self.printSymbolTable()
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by gslParser#assignment.
    def visitAssignment(self, ctx:gslParser.AssignmentContext):
        print(ctx.getText())
        # print(self.symbolTable[0])
        if str(ctx.IDENTIFIER()) not in self.symbolTable:
            print("Error: Identifier not declared")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gslParser#expr.
    def visitExpr(self, ctx:gslParser.ExprContext):
        print(ctx.getText())
        if ctx.IDENTIFIER() and str(ctx.IDENTIFIER()) not in self.symbolTable:
            print("Error: Identifier not declared")
        return self.visitChildren(ctx)

    def printSymbolTable(self):
        for i in range(len(self.symbolTable)):
            print(self.symbolTable[i])
