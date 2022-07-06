from antlr4 import *
from gsl.gslVisitor import *
from gsl.gslParser import *

class gslToZ3Visitor(gslVisitor): 

    # Visit a parse tree produced by gslParser#expr.
    def visitExpr(self, ctx:gslParser.ExprContext):
        print("Visitor")
        return self.visitChildren(ctx)