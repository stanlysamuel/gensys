from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Diagonal example: Neider et. al., TACAS 2016 and DTSynth Tool, FMCAD 2019
# A robot moves in an infinite, discrete twodimensional grid world. Player 0 controls the robot’s
# vertical movement, while Player 1 controls the horizontal.
# Player 0 wins if the robot stays within two cell around
# the diagonal

# 1. Define Environment moves
#Environment move is Skip here
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
    return And(y >= x - 2, y <= x + 2)

safety_fixedpoint(controller_moves, environment, guarantee)