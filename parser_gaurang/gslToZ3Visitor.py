from antlr4 import *
from gsl.gslVisitor import *
from gsl.gslParser import *

class gslToZ3Visitor(gslVisitor): 
    
    symbolTable = []

    # Visit a parse tree produced by gslParser#decl.
    def visitDecl(self, ctx:gslParser.DeclContext):
        # ctx.getChildren.__eq__([0])
        print(ctx.getText())
        type = self.visit(ctx.type_())
        variable = str(ctx.IDENTIFIER())
        self.symbolTable.append((variable, type))
        # if (variable in gslVisitor.visitDecl): 
        #     print(variable+'_')
        #     equal=':='    
        # # if (equal in gslVisitor.visitDecl):
        # #      new=equal.replace(':=','==')
        # #      print(new)
        self.printSymbolTable()
        # exit()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gslParser#type.
    def visitType(self, ctx:gslParser.TypeContext):
        return str(ctx.children[0])
    
    # Visit a parse tree produced by gslParser#assignment.
    def visitAssignment(self, ctx:gslParser.AssignmentContext):
        f=open('z3.py','w')
        #data=f.read()
        print(ctx.getText())
        # print(self.symbolTable[0])
        varPresent = False
        for symbol in self.symbolTable:
            print(symbol)
            if str(ctx.IDENTIFIER()) in symbol[0]:
                varPresent = True
        if(not varPresent):
            print("Error: Identifier not declared")
        var=str(ctx.children[0])
        new1=var.replace(var,var+'_')  
        #print(new1)
        eq=str(ctx.children[1])
        new2=eq.replace(eq,"==")
       # print(new2)
        #print(ctx.expr().)
        f.write(new1)
        f.write(new2)
        f.write(str(self.visit(ctx.children[2])))
        print(ctx.children[2])
        f.close()
        exit()
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

# Visit a parse tree produced by gslParser#expr.
    def visitExpr(self, ctx:gslParser.ExprContext):
        if ctx.IDENTIFIER():
            return str(ctx.IDENTIFIER())
        else:
            if ctx.NUM():
                return str(ctx.NUM())
            else:
                return str(self.visit(ctx.children[0])+ str(self.visit(ctx.children[1])) + self.visit(ctx.children[2]))
            
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gslParser#op.
    def visitOp(self, ctx:gslParser.OpContext):
        return str(ctx.children[0])