from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Andreas example non-deterministic controller: 

game_type  =  "Int"

# 1. Define Environment moves
def environment(x,x_):
    return And(Or(x_ == x, x_ == x - 1), x>=0, x<=10)

#2. Define Controller moves

def move1(x,x_):
    return And(x>=0, x<=10, x_ == x + 1)

def move2(x,x_):
    return And(x>=0, x<=10, x_ == x)

def move3(x,x_):
    return And(x>=0, x<=10, x_ == x - 1)

controller_moves = [move1, move2, move3]

mode = 0

# 3. Define Guarantee
def guarantee(x):
    return Or(x == 1, x ==2)

# safety_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# reachability_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
buchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)