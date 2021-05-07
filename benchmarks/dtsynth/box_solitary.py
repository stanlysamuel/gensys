from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Solitary Box example: Neider et. al., TACAS 2016 and DTSynth Tool, FMCAD 2019
# Another variation of the Box game in
# which only Player 0 is in control of the robot

# 1. Define Environment moves
#Environment move is Skip here
def environment(x,y,x_,y_):
    return And(x_ == x, y_==y)

# 2. Define Controller moves

def move1(x,y,x_,y_):
    return And(x_ == x, y_ == y)

def move2(x,y,x_,y_):
    return And(x_ == x+1, y_ == y)

def move3(x,y,x_,y_):
    return And(x_ == x-1, y_ == y)

def move4(x,y,x_,y_):
    return And(x_ == x, y_ == y + 1)

def move5(x,y,x_,y_):
    return And(x_ == x+1, y_ == y + 1)

def move6(x,y,x_,y_):
    return And(x_ == x-1, y_ == y + 1)

def move7(x,y,x_,y_):
    return And(x_ == x, y_ == y - 1)

def move8(x,y,x_,y_):
    return And(x_ == x+1, y_ == y - 1)

def move9(x,y,x_,y_):
    return And(x_ == x-1, y_ == y - 1)

controller_moves = [move1, move2, move3, move4, move5, move6, move7, move8, move9]

# 3. Define Guarantee
def guarantee(x, y):
    return And(x<=3, x>=0)

safety_fixedpoint(controller_moves, environment, guarantee)