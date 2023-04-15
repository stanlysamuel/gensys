from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Andreas example non-deterministic controller: 

game_type  =  "Int"

# 1. Define Environment moves
def environment(x,x_):
    return And(x_ == x-1)

#2. Define Controller moves

def move1(x,x_):
    return And(x_ == x+1)

# def move2(x,x_):
#     return And(x_ == x)

controller_moves = [move1]

mode = 0

# 3. Define Guarantee
def guarantee(x):
    return Or(x<1, x>3)

# safety_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# reachability_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
buchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)
# cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type)



# Spec: Buchi, G(F(x==1) and F(x==2))
# Complete Buchi Automaton from spot encoded in LIA for the above formula
# Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

# nQ = 3
# def automaton(q, q_, x):
#     return Or(
#             And(q == 0, q_==1, x!=2),
#             And(q == 0, q_==2, x==2),
#             And(q == 1, q_==1, x!=2),
#             And(q == 1, q_==2, x==2),
#             And(q == 2, q_==2, x!=1),
#             And(q == 2, q_==0, x==1)
#             # And(q>=0, q<=3, q_>=0, q_<=3)
#             )

# # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
# def isFinal(p):
#     return If(p == 0, 1, 0)

# # (Optional): Explicit safety guarantee that complements the omega-regular formula
# # Default: Returns the True formula in Z3
# def guarantee(x):
#     return And(True)

# # Call the fixpoint engine for omega regular specifications.
# buchi_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, nQ, game_type)