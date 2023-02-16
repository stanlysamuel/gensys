from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Sumanth's safety game using CHC's example

# 1. Define Environment moves
def environment(x,y,x_,y_):
    return And(Or(x_ == x + 1, x_ == x - 1, x_ == x), Or(y_ == y + 1, y_ == y - 1, y_ == y))

#2. Define Controller moves

def move1(x,y,x_,y_):
    return And(x_ == x, y_ == y)

def move2(x,y,x_,y_):
    return And(x_ == x, y_ == y+1)

def move3(x,y,x_,y_):
    return And(x_ == x, y_ == y-1)

controller_moves = [move1, move2, move3]

# 3. Define Guarantee
def guarantee(x, y):
    return And(y<=1, y>=-1)

safety_fixedpoint(controller_moves, environment, guarantee, 0)