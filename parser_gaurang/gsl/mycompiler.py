import sys

import antlr4

from experiments.visitors.gsllexer import gsllexer
from experiments.visitors.gslParser import gslParser
from experiments.visitors.gslToZ3Visitor import gslToZ3Visitor


def preparez3(verilog_spec, verilog_spec_location, num_of_ouputs, manthan=0):
    '''
    Input: gsl file
    Output: z3py equivalent of gsl file
    Functionality: Parses the gsl file and converts it to z3py format.
                                    It does the same for the NN output as well.
    '''

    # verilog_spec = "sampleskf.v"
    # verilog_spec_location = ""
    filename = gsl_spec_location + gsl_spec
    f = open(filename, "r")
    data = f.read()
    inputStream = antlr4.InputStream(data)
    lexer = gslLexer(inputStream)
    tokenStream = antlr4.CommonTokenStream(lexer)
    parser = gslParser(tokenStream)
    tree = parser.module_declaration()
    visitor = gslVisitor(
        gsl_spec, gsl_spec_location, num_of_ouputs)
    z3filecontent = visitor.visit(tree)
     file.close()