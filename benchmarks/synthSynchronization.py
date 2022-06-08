from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Synth Synchronization example: Beyene et. al. POPL 2014

# 1. Define Environment moves
#Environment move is Skip here
def environment(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return And(x == x_, y1 == y1_, y2 == y2_, z == z_, pc1 == pc1_, pc2 == pc2_, pc3 == pc3_)

#2. Define Controller moves

#Transition System 1
def next1(x, y1, y2, z, pc1, x_, y1_, y2_, z_, pc1_):
    return Or(  And(pc1 == 1, pc1_ == 2, x_ == x + z, y1_ == y1, y2_ == y2, z_ == z), 
                And(pc1 == 2, pc1_ == 3, x_ == x + z, y1_ == y1, y2_ == y2, z_ == z))

def next2(x, y1, y2, z, pc2, x_, y1_, y2_, z_, pc2_):
    return Or(  And(pc2 == 1, pc2_ == 2, z_ == z + 1, y1_ == y1, y2_ == y2, x_ == x), 
                And(pc2 == 2, pc2_ == 3, z_ == z + 1, y1_ == y1, y2_ == y2, x_ == x))

def next3(x, y1, y2, z, pc3, x_, y1_, y2_, z_, pc3_):
    return Or(  And(pc3 == 1, pc3_ == 2, x == 1, y1_ == 3, y2_ == y2, x_ == x, z_ == z), 
                And(pc3 == 1, pc3_ == 2, x == 2, y1_ == 6, y2_ == y2, x_ == x, z_ == z),
                And(pc3 == 1, pc3_ == 2, Or(x<=0, x>=3), y1_ == 5, y2_ == y2, x_ == x, z_ == z),
                And(pc3 == 2, pc3_ == 3, y2_ == x, x_ == x, y1_ == y1, z_ == z),
                And(pc3 == 3, pc3_ == 4, y1 != y2, x_ == x, y1_ == y1, y2_ == y2, z_ == z)
                )

def move1(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return And(next1(x, y1, y2, z, pc1, x_, y1_, y2_, z_, pc1_), pc2_ == pc2, pc3_ == pc3)

def move2(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return And(next2(x, y1, y2, z, pc2, x_, y1_, y2_, z_, pc2_), pc1_ == pc1, pc3_ == pc3)

def move3(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return And(next3(x, y1, y2, z, pc3, x_, y1_, y2_, z_, pc3_), pc2_ == pc2, pc1_ == pc1)

controller_moves = [move1, move2, move3]

# 3. Define Guarantee
def guarantee(x, y1, y2, z, pc1, pc2, pc3):
    return And(Not(And(pc3 == 3, y1 == y2)), pc1<=3, pc1>=1, pc2<=3, pc2>=1, pc3<=4, pc3>=1)

safety_fixedpoint(controller_moves, environment, guarantee,0)
