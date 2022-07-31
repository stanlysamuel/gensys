from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 1. Define Environment moves
def environment(x, i, x_, i_):
    return And(i_ < 5, i_ >=0, x_ == x)

def move1(x, i, x_, i_):
    return And( x_ == x + i)

def move2(x, i, x_, i_):
    return  And( x_ == x - i)

controller_moves = [move1, move2]

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "safety":
    # 3. Define Guarantee
    def guarantee(x, i):
        return And(x>=0, x<=100, i>=0, i< 50)

    safety_fixedpoint(controller_moves, environment, guarantee, int(mode))