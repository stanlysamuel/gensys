from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Limited Box example: Neider et. al., TACAS 2016 and DTSynth Tool, FMCAD 2019
# A variation of the box game. Player 0 can
# only control the robot's vertical movement and Player 1
# the horizontal.

# 1. Define Environment moves
def environment(x,y,x_,y_):
    return And(Or(x_ == x + 1, x_ == x - 1, x_ == x), y_ == y)

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
    return And(x<=3, x>=0)

safety_fixedpoint(controller_moves, environment, guarantee, 0)