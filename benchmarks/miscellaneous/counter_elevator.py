from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Counter/Elevator example: 

# 1. Define Environment moves
def environment(x,x_):
    return x_ == x

#2. Define Controller moves

def move1(x,x_):
    return And(x_ == x + 1)

def move2(x,x_):
    return And(x_ == x - 1)

controller_moves = [move1, move2]

# 3. Define Guarantee
def guarantee(x):
    return And(0<=x, x<=10)

safety_fixedpoint(controller_moves, environment, guarantee, 0)