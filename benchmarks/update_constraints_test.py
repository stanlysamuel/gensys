from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Example to test constraints over updates such as x' = x + 1

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
#Environment move is Skip here
def environment(x, x_):
    return And(x_ == x)

#2. Define Controller moves

def move1(x, x_):
    return And(x_ == x + 1)

controller_moves = [move1]

# 4. Define Initial States
def init(x):
    return False

# 3. Define Guarantee
def guarantee(x):
    return And(a>=b, b>=c, c>=d, d>=e)

# Spec: FG (a>=b, b>=c, c>=d, d>=e)
cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)
