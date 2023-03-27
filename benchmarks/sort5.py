from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 5 variable Sorting Example taken from the paper "Reactive Synthesis Modulo Theories using Abstraction Refinement"

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
#Environment move is Skip here
def environment(a, b, c, d, e, a_, b_, c_, d_, e_):
    return And(a_ == a, b_ == b, c_ == c, d_ == d, e_ == e)

#2. Define Controller moves

# flip(a,b)
def move1(a, b, c, d, e, a_, b_, c_, d_, e_):
    return And(a_ == b, b_ == a, c_ == c, d_ == d, e_ == e)

# flip(b,c)
def move2(a, b, c, d, e, a_, b_, c_, d_, e_):
    return And(a_ == a, b_ == c, c_ == b, d_ == d, e_ == e)

# flip(c,d)
def move3(a, b, c, d, e, a_, b_, c_, d_, e_):
    return And(a_ == a, b_ == b, c_ == d, d_ == c, e_ == e)

# flip(d,e)
def move4(a, b, c, d, e, a_, b_, c_, d_, e_):
    return And(a_ == a, b_ == b, c_ == c, d_ == e, e_ == d)

# skip
def move5(a, b, c, d, e, a_, b_, c_, d_, e_):
    return And(a_ == a, b_ == b, c_ == d, d_ == c, e_ == e)

controller_moves = [move1, move2, move3, move4, move5]

# 3. Define Guarantee
def guarantee(a, b, c, d, e):
    return And(a>=b, b>=c, c>=d, d>=e)

# Spec: FG (a>=b, b>=c, c>=d)
cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type)
