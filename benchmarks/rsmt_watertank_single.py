# Two Water Tanks example TSL(LRA)

from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 0. Define game type (Int/ Real)
game_type = "Real"

# 1. Define Environment moves
def environment(x, x_):
    return And(x_ == x)

def move1(x, x_):
    return And(x_ == 0.9635*x)

def move2(x, x_):
    return And(x_ == 0.9635*x + 0.1)

controller_moves = [move1, move2]

mode = sys.argv[1]

# Spec: G (And(x>= 0.0, x<0.7)) & G( x<0.1 -> x>=0.4)
# Complete Universal Co-Buchi Automaton from spot encoded in LRA.
# Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

nQ = 2
def automaton(q, q_, x):
    return Or(
            And(q == 0, q_==0),
            And(q == 1, q_==0,Or(Not(And(x>= 0.0, x<0.7)), And(x<0.1, Not(x>=0.4)))),
            And(q == 0, q_==1, And(x>= 0.0, x<0.7, Or(Not(x<0.1), x>=0.4)))
            )
# Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
def isFinal(p):
    return If(And(p == 0), 1, 0)

# (Optional): Explicit safety guarantee that complements the omega-regular formula
# Default: Returns the True formula in Z3
def guarantee(x):
    return And(True)

cobuchi_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, nQ, game_type)