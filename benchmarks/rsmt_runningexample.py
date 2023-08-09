from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Motivating Example taken from the paper "Reactive Synthesis Modulo Theories Using Abstraction Refinement"

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves (asssumption over the TSL-MT specification)
def environment(x,i,x_,i_):
    return And(x_ == x, i_>=0, i_<5)

#2. Define Controller moves

def move1(x,i,x_,i_):
    return And(x_ == x+i, i_ == i)

def move2(x,i,x_,i_):
    return And(x_ == x-i, i_ == i)

# Define initial state (must contain environment assumption as well, else too weaks)
def init(x,i):
    return And(x>=0, x<100, i>=0, i<5)

# def init(x,i):
#     return False

controller_moves = [move1, move2]

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "simple":

    # 3. Define Guarantee
    def guarantee(x, i):
        return And(x>=0, x<100)

    # Spec: G (x>=0, x<=3)
    safety_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)
