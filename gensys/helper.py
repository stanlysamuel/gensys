# GenSys v0.1: Synthesis of Maximal Controllers for Safety Specifications
# Copyright (C) 2021  Stanly Samuel

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>

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