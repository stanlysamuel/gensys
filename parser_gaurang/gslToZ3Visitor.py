from lib2to3.pygram import Symbols
from symtable import SymbolTable
from antlr4 import *
from gsl.gslVisitor import *
from gsl.gslParser import *

class gslToZ3Visitor(gslVisitor): 
    
    symbolTable = []

    # Visit a parse tree produced by gslParser#decl.
    def visitDecl(self, ctx:gslParser.DeclContext):
        print(ctx.getText())
        type = self.visit(ctx.type_())
        variable = str(ctx.IDENTIFIER())
        self.symbolTable.append((variable, type))
        self.printSymbolTable()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gslParser#type.
    def visitType(self, ctx:gslParser.TypeContext):
        return str(ctx.children[0])
    
    # Visit a parse tree produced by gslParser#assignment.
    def visitAssignment(self, ctx:gslParser.AssignmentContext):
        print(ctx.getText())
        # print(self.symbolTable[0])
        varPresent = False
        for symbol in self.symbolTable:
            print(symbol)
            if str(ctx.IDENTIFIER()) in symbol[0]:
                varPresent = True
        if(not varPresent):
            print("Error: Identifier not declared")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gslParser#expr.
    def visitExpr(self, ctx:gslParser.ExprContext):
        print(ctx.getText())

        varPresent = False
        if ctx.IDENTIFIER():
            for symbol in self.symbolTable:
                print(symbol)
                if str(ctx.IDENTIFIER()) in symbol[0]:
                    varPresent = True
            if(not varPresent):
                print("Error: Identifier not declared")
        return self.visitChildren(ctx)

    def printSymbolTable(self):
        for i in range(len(self.symbolTable)):
            print(self.symbolTable[i])
