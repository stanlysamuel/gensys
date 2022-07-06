import sys

import antlr4

from gslLexer import gslLexer
from gslParser import gslParser
from gslToZ3Visitor import gslToZ3Visitor


def preparez3(gsl_spec, gsl_spec_location, no_of_ouputs):

    filename = gsl_spec_location + gsl_spec
    f = open(filename, "r")
    data = f.read()
    inputStream = antlr4.InputStream(data)
    lexer = gslLexer(inputStream)
    tokenStream = antlr4.CommonTokenStream(lexer)
    parser = gslParser(tokenStream)
    tree = parser.module_declaration()
    visitor = gslToZ3Visitor(gsl_spec, gsl_spec_location, no_of_ouputs)
    z3filecontent = visitor.visit(tree)
    file.close()