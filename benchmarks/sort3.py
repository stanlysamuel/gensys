from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 3 variable Sorting Example taken from the paper "Reactive Synthesis Modulo Theories using Abstraction Refinement"

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
#Environment move is Skip here
def environment(a, b, c, a_, b_, c_):
    return And(a_ == a, b_ == b, c_ == c)

#2. Define Controller moves

# flip(a,b)
def move1(a, b, c, a_, b_, c_):
    return And(a_ == b, b_ == a, c_ == c)

# flip(b,c)
def move2(a, b, c, a_, b_, c_):
    return And(a_ == a, b_ == c, c_ == b)

# skip
def move3(a, b, c, a_, b_, c_):
    return And(a_ == a, b_ == b, c_ == c)

controller_moves = [move1, move2, move3]

# 3. Define Guarantee
def guarantee(a, b, c):
    return And(a>=b, b>=c)

# Spec: FG (a>=b, b>=c)
cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type)
