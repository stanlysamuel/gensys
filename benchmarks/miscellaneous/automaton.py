from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Turn based automaton for G(r -> XF g)

# 1. Define Environment moves. Non determinism is denoted by Or.
def environment(state,state_):
    return And(Implies(state==4, Or(state_==1, state_==2)), Implies(state==5, state_==2), Implies(state==7, state_==3))

#2. Define Controller moves

def g(state, state_):
    return And(Implies(state==1, state_==4), Implies(state==2, state_==6), Implies(state==3, state_==7))

def not_g(state, state_):
    return And(Implies(state==1, state_==4), Implies(state==2, state_==5), Implies(state==3, state_==7))

controller_moves = [g, not_g]

mode = sys.argv[1]

# 3. Define Guarantee
def guarantee(state):
    return state != 2

safety_fixedpoint(controller_moves, environment, guarantee, int(mode))
# reachability_fixedpoint(controller_moves, environment, guarantee, int(mode))