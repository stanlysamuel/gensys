# Generated from task.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .taskParser import taskParser
else:
    from taskParser import taskParser

# This class defines a complete listener for a parse tree produced by taskParser.
class taskListener(ParseTreeListener):

    # Enter a parse tree produced by taskParser#prog.
    def enterProg(self, ctx:taskParser.ProgContext):
        pass

    # Exit a parse tree produced by taskParser#prog.
    def exitProg(self, ctx:taskParser.ProgContext):
        pass


    # Enter a parse tree produced by taskParser#expr.
    def enterExpr(self, ctx:taskParser.ExprContext):
        pass

    # Exit a parse tree produced by taskParser#expr.
    def exitExpr(self, ctx:taskParser.ExprContext):
        pass


    # Enter a parse tree produced by taskParser#decl.
    def enterDecl(self, ctx:taskParser.DeclContext):
        pass

    # Exit a parse tree produced by taskParser#decl.
    def exitDecl(self, ctx:taskParser.DeclContext):
        pass



del taskParser