from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Andreas example non-deterministic controller: 

# 1. Define Environment moves
def environment(x,y,x_,y_):
    return And(x_ > y, y_ == y)

#2. Define Controller moves

def move(x,y,x_,y_):
    return And(y_ < x, x_ == x)

controller_moves = [move]

# 3. Define Guarantee
def guarantee(x, y):
    return y > 0

safety_fixedpoint(controller_moves, environment, guarantee, 0)