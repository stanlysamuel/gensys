from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Andreas example non-deterministic controller: 

game_type  =  "Int"

# 1. Define Environment moves
def environment(x,x_):
    return And(x_ == x)

#2. Define Controller moves

def move1(x,x_):
    return And(x_ == x + 1)

def move2(x,x_):
    return And(x_ == x + 2)

controller_moves = [move1, move2]

mode = 0

# 3. Define Guarantee
def guarantee(x):
    return x == 1

# safety_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# reachability_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
buchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)