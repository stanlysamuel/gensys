from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 4 variable Sorting Example taken from the paper "Reactive Synthesis Modulo Theories using Abstraction Refinement"

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
#Environment move is Skip here
def environment(a, b, c, d, a_, b_, c_, d_):
    return And(a_ == a, b_ == b, c_ == c, d_ == d)

#2. Define Controller moves

# flip(a,b)
def move1(a, b, c, d, a_, b_, c_, d_):
    return And(a_ == b, b_ == a, c_ == c, d_ == d)

# flip(b,c)
def move2(a, b, c, d, a_, b_, c_, d_):
    return And(a_ == a, b_ == c, c_ == b, d_ == d)

# flip(c,d)
def move3(a, b, c, d, a_, b_, c_, d_):
    return And(a_ == a, b_ == b, c_ == d, d_ == c)

# skip
def move4(a, b, c, d, a_, b_, c_, d_):
    return And(a_ == a, b_ == b, c_ == c, d_ == d)

controller_moves = [move1, move2, move3, move4]

# 3. Define Guarantee
def guarantee(a, b, c, d):
    return And(a>=b, b>=c, c>=d)

# 4. Define Initial States
def init(a, b, c, d):
    return False

# Spec: FG (a>=b, b>=c, c>=d)
cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)
