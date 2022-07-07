import sys
import antlr4

from gsl.gslLexer import *
from gsl.gslParser import *
from gslToZ3Visitor import *

def parseGsl(filepath):
    f = open(filepath, "r")
    gslFile = f.read()
    data = InputStream(gslFile)
    lexer = gslLexer(data)
    tokenStream = CommonTokenStream(lexer)
    parser = gslParser(tokenStream)
    tree = parser.prog()
    visitor = gslToZ3Visitor()
    visitor.visit(tree)

parseGsl("./benchmarks/test/test1.gsl")