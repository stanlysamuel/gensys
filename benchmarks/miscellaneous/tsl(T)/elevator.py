from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Elevator example: Maderbacher et al.
# An elevator that ranges between 1 and max.

# 1. Define Environment moves
def environment(floor, floor_):
    return floor_ == floor + 2

#2. Define Controller moves

def move1(floor, floor_):
    return floor_ == floor

def move2(floor, floor_):
    return floor_ == floor + 1

def move3(floor, floor_):
    return floor_ == floor - 2

controller_moves = [move1, move2, move3]

max = sys.argv[1]

# 3. Define Guarantee
def guarantee(floor):
    return And(floor >=1, floor <=max)

safety_fixedpoint(controller_moves, environment, guarantee, 0)