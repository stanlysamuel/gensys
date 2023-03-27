from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
def environment(x, input, x_, input_):
    return And(input_ < 5, input_ >=0, x_ == x)

def move1(x, input, x_, input_):
    return And( x_ == x + input)

def move2(x, input, x_, input_):
    return  And( x_ == x - input)

controller_moves = [move1, move2]

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "safety":
    # 3. Define Guarantee
    def guarantee(x, input):
        return And(x>=0, x<=100000, input>=0, input< 50)

safety_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type)