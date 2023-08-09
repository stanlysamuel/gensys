from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Cinderella-Stepmother game of 5 buckets with bucket size of C. Here, the controller (protagonist) is Cinderella and it aims to win the game by staying in the safe region i.e., G(safe) or other complex LTL properties

# 0. Define game type (Int/ Real)
game_type = "Real"

# 1. Define Environment moves

def stepmother(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And(b1_ + b2_ + b3_ + b4_ + b5_ == b1 + b2 + b3 + b4 + b5 + 1, b1_>=b1, b2_>=b2, b3_>=b3, b4_>=b4, b5_>=b5)

#2. Define (Finite) Controller moves

def move1(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b1_ == 0.0,  b2_ == 0.0, b3_ == b3, b4_ == b4, b5_ == b5)

def move2(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b2_ == 0.0,  b3_ == 0.0, b4_ == b4, b5_ == b5, b1_ == b1)

def move3(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b3_ == 0.0,  b4_ == 0.0, b5_ == b5, b1_ == b1, b2_ == b2)

def move4(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b4_ == 0.0,  b5_ == 0.0, b1_ == b1, b2_ == b2, b3_ == b3)

def move5(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b5_ == 0.0,  b1_ == 0.0, b2_ == b2, b3_ == b3, b4_ == b4)

cinderella_moves = [move1, move2, move3, move4, move5]

#3. Define Init Region (False by default => Maximal winning region will be returned)

# def init(b1, b2, b3, b4, b5):
#     return And(b1 == 0.0, b2 == 0.0, b3 == 0.0, b4 == 0.0, b5 == 0.0)

def init(b1, b2, b3, b4, b5):
    return False

# Benchmark specific parameters

C = sys.argv[1]

# 4. Specify property

spec1 = 'G (And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C, b1>=0.0, b2>=0.0, b3>=0.0, b4>=0.0, b5>=0.0))'
spec2 = 'GF (And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C, b1>=0.0, b2>=0.0, b3>=0.0, b4>=0.0, b5>=0.0))'
spec3 = 'GF (And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)) | (GF (And(b1 <= C, b2 > C)) & !GF (And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)) & !GF (b1 > C))'


# 5. Call GenSys
# gensys(controller_moves, environment, specification_ltl, mode of play (environment plays first or cinderella), game_type (Int or Real), init)
gensys(cinderella_moves, stepmother, spec, int(mode), game_type, init)
