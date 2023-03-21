from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Synth Synchronization example: Beyene et. al. POPL 2014 taken from Vechev et. al. POPL 2010, Figure 1.
# Case of three threads.
# All possible interleavings are enumerated and the controller is required to find a strategy that avoids the assertion failure at program 3 line 3

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
#Environment move is Skip here
def environment(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return And(x == x_, y1 == y1_, y2 == y2_, z == z_, pc1 == pc1_, pc2 == pc2_, pc3 == pc3_)

#2. Define Controller moves

#Transition System 1

def move1(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return Or(  # Single transitions
                And(pc1 == 1, pc1_ == 2, x_ == x + z, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc3_ == pc3),
                And(pc1 == 2, pc1_ == 3, x_ == x + z, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc3_ == pc3),
                # Atomic Sections
                And(pc1 == 1, pc1_ == 3, x_ == x + z + z, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc3_ == pc3)
                )

def move2(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return Or(  # Single transitions
                And(pc2 == 1, pc2_ == 2, z_ == z + 1, y1_ == y1, y2_ == y2, x_ == x, pc1_ == pc1, pc3_ == pc3),
                And(pc2 == 2, pc2_ == 3, z_ == z + 1, y1_ == y1, y2_ == y2, x_ == x, pc1_ == pc1, pc3_ == pc3),
                # Atomic Sections
                And(pc2 == 1, pc2_ == 3, z_ == z + 2, y1_ == y1, y2_ == y2, x_ == x, pc1_ == pc1, pc3_ == pc3)
                )

def move3(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return Or(  # Single transitions
                And(pc3 == 1, pc3_ == 2, x == 1, y1_ == 3, y2_ == y2, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 1, pc3_ == 2, x == 2, y1_ == 6, y2_ == y2, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 1, pc3_ == 2, Or(x<=0, x>=3), y1_ == 5, y2_ == y2, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 2, pc3_ == 3, y2_ == x, x_ == x, y1_ == y1, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 3, pc3_ == 4, y1 != y2, x_ == x, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc1_ == pc1),
                # Atomic Sections
                And(pc3 == 1, pc3_ == 3, x == 1, y1_ == 3, y2_ == x, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 1, pc3_ == 3, x == 2, y1_ == 6, y2_ == x, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 1, pc3_ == 3, Or(x<=0, x>=3), y1_ == 5, y2_ == x, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 2, pc3_ == 4, Or(y1>=x+1, x>=y1+1), y2_ == x, x_ == x, y1_ == y1, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 1, pc3_ == 4, x == 1, y1_ == 3, y2_ == x, Or(2>= x, x>=4), x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 1, pc3_ == 4, x == 2, y1_ == 6, y2_ == x, Or(5>= x, x>=7), x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 1, pc3_ == 4, Or(x<=0, x>=3), y1_ == 5, y2_ == x, Or(4>= x, x>=6), x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1)
                
                )

controller_moves = [move1, move2, move3]

# 3. Define Guarantee
def guarantee(x, y1, y2, z, pc1, pc2, pc3):
    return Not(And(pc3 == 3, y1 == y2))

# safety_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type)


def guarantee_reach(x, y1, y2, z, pc1, pc2, pc3):
    return And(pc3 == 3, y1 == y2)

def controller(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return Or(move1(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_),move2(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_),move3(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_))
# reachability_fixedpoint_gensys([environment], controller, guarantee_reach, 0, game_type)
reachability_fixedpoint_gensys(controller_moves, environment, guarantee_reach, 0, game_type)

