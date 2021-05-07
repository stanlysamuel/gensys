from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Evasion game: Neider et. al., TACAS 2016 and DTSynth Tool, FMCAD 2019
# Two robots are moving in an infinite, discrete two-dimensional grid world. The robots take turns
# moving at most one cell in any direction. Each players
# controls one robot. Player 0's objective is to avoid getting
# caught by Player 1's robot

# 1. Define Environment moves
#Environment move is Skip here
def environment(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(Or(x1_ == x1 + 1, x1_ == x1 - 1, x1_ == x1), Or(y1_ == y1 + 1, y1_ == y1 - 1, y1_ == y1),x2_==x2, y2_==y2)

# 2. Define Controller moves

def move1(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2, y2_ == y2, x1_==x1, y1_==y1)

def move2(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2+1, y2_ == y2, x1_==x1, y1_==y1)

def move3(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2-1, y2_ == y2, x1_==x1, y1_==y1)

def move4(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2, y2_ == y2 + 1, x1_==x1, y1_==y1)

def move5(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2+1, y2_ == y2 + 1, x1_==x1, y1_==y1)

def move6(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2-1, y2_ == y2 + 1, x1_==x1, y1_==y1)

def move7(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2, y2_ == y2 - 1, x1_==x1, y1_==y1)

def move8(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2+1, y2_ == y2 - 1, x1_==x1, y1_==y1)

def move9(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2-1, y2_ == y2 - 1, x1_==x1, y1_==y1)

controller_moves = [move1, move2, move3, move4, move5, move6, move7, move8, move9]

# 3. Define Guarantee
def guarantee(x1, y1, x2, y2):
    return Not(And(x1==x2, y1==y2))

safety_fixedpoint(controller_moves, environment, guarantee)