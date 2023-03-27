# Two Water Tanks example TSL(LRA)

from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 0. Define game type (Int/ Real)
game_type = "Real"

# 1. Define Environment moves
def environment(x1, x2, x1_, x2_):
    return And(x1_ == x1, x2_ == x2)

def move1(x1, x2, x1_, x2_):
    return Implies(And(x1< 0.2, x2<0.2), And(x1_ == x1, x2_ == 0.9635*x2))

def move2(x1, x2, x1_, x2_):
    return Implies(And(x1< 0.2, x2<0.2), And(x1_ == x1 + 0.0003 * 324.6753, x2_ == 0.9635*x2))

def move3(x1, x2, x1_, x2_):
    return Implies(Or(x1>= 0.2, x2>=0.2), And(x1_ == 0.8281*x1 + 0.1719*x2, x2_ == 0.7916*x2 + 0.1719*x1))

def move4(x1, x2, x1_, x2_):
    return Implies(Or(x1>= 0.2, x2>=0.2), And(x1_ == 0.8281*x1 + 0.1719*x2 + 0.0003*324.6753, x2_ == 0.7916*x2 + 0.1719*x1))

controller_moves = [move1, move2, move3, move4]

mode = sys.argv[1]

# 3. Define Guarantee
def guarantee(x1, x2):
    return And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7)

safety_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)