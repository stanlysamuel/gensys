from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Cinderella-Stepmother game of 5 buckets with bucket size of C. Here, the controller (protagonist) is Stepmother and it aims to win the game by violating the safety condition i.e., F(not safe).

# 1. Define Environment move

def environment(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return Or(
        And( b1_ == 0.0,  b2_ == 0.0, b3_ == b3, b4_ == b4, b5_ == b5),
        And( b2_ == 0.0,  b3_ == 0.0, b4_ == b4, b5_ == b5, b1_ == b1),
        And( b3_ == 0.0,  b4_ == 0.0, b5_ == b5, b1_ == b1, b2_ == b2),
        And( b4_ == 0.0,  b5_ == 0.0, b1_ == b1, b2_ == b2, b3_ == b3),
        And( b5_ == 0.0,  b1_ == 0.0, b2_ == b2, b3_ == b3, b4_ == b4)
    )

# 2. Define Controller moves

def stepmother(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And(b1_ + b2_ + b3_ + b4_ + b5_ == b1 + b2 + b3 + b4 + b5 + 1, b1_>=b1, b2_>=b2, b3_>=b3, b4_>=b4, b5_>=b5)

controller_moves = [stepmother]

C = sys.argv[1]
mode = sys.argv[2]
# spec = sys.argv[3]

# Spec 1: Reachability, F(Not(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0))))
# Complete Universal Co-Buchi Automaton from spot encoded in LRA.
# Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

nQ = 2
def automaton(q, q_, b1, b2, b3, b4, b5):
    return Or(
            And(q == 0, q_==1, Not(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0))),
            And(q == 0, q_==0, And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)),
            And(q == 1, q_==1),
            )
# Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
def isFinal(p):
    return If(p==0, 1, 0)

#Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
def sigma(b1, b2, b3, b4, b5):
    return [Not(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)), And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)]

# (Optional): Explicit safety guarantee that complements the omega-regular formula
# Default: Returns the True formula in Z3
def guarantee(b1, b2, b3, b4, b5):
    return And(True)

# Call the fixpoint engine for omega regular specifications.
omega_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ)