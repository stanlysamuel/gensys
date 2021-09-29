#  GenSys v0.1

#  Copyright (C) 2021 Stanly Samuel

#  This software is available under the MIT license. Please see LICENSE in the
#  top-level directory for details.

#  This file is part of gensys.
from z3 import *

#Function to check validity of a formula
def valid(formula, verbose):
    s = Solver()
    s.add(Not(formula))
    if s.check() == unsat:
        if(verbose):
            print("Valid")
        return True
    else:
        if(verbose):
            print("Not Valid")
        return False

#Function to check satisfiability of a formula
def satisfiable(formula, verbose):
    s = Solver()
    s.add(formula)
    if s.check() == sat:
        if(verbose):
            print("SAT")
        return True
    else:
        if(verbose):
            print("UNSAT")
        return False