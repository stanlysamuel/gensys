from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Test 1: move 1 winning region is (x = 3) but can only be computed if fixedpoint is computed from AE mode.

game_type  =  "Int"

# 1. Define Environment moves
def environment(x,x_):
    return And(x_ == x-1)

#2. Define Controller moves

def move1(x,x_):
    return And(x_ == x+1)

controller_moves = [move1]

mode = 0

# 3. Define Guarantee
def guarantee(x):
    return Or(x<1, x>3)

# safety_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# reachability_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
buchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)


# Test 2: move 1 winning region is not 0,1,2. move 2 has true as winning region
# Good example
game_type  =  "Int"

# 1. Define Environment moves
def environment(x,x_):
    return Or(x_ == x-1, x_ == x+2)

#2. Define Controller moves

def move1(x,x_):
    return And(x_ == x+1)

def move2(x,x_):
    return And(x_ == x+2)

controller_moves = [move1, move2]

mode = 0

# 3. Define Guarantee
def guarantee(x):
    return Or(x<=-1, x>=4)

# safety_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# reachability_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
buchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)

# Test 3: move 1, 2

game_type  =  "Int"

# 1. Define Environment moves
def environment(x,x_):
    return Or(x_ == x-1, x_ == x-2)

#2. Define Controller moves

def move1(x,x_):
    return And(x_ == x+1)

def move2(x,x_):
    return And(x_ == x+2)

controller_moves = [move1, move2]

mode = 0

# 3. Define Guarantee
def guarantee(x):
    return Or(x<=-1, x>=4)

# safety_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# reachability_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
buchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)