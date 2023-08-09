from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Motivating Example taken from the paper "Solving Infinite-State Games via Acceleration"

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
def environment(l, x, i, l_, x_, i_):
    return And(l_ == l, x_ == x)

#2. Define Controller moves
# A move for each transition in the reactive program game

def move1(l, x, i, l_, x_, i_):
    return And(l == 0, x > 42, i != 0, l_ == 0, x_ == x + i, i_ == i)

def move2(l, x, i, l_, x_, i_):
    return And(l == 0, x > 42, i != 0, l_ == 0, x_ == x - i, i_ == i)

def move3(l, x, i, l_, x_, i_):
    return And(l == 0, Or(x <= 42, i == 0), l_ == 1, x_ == x, i_ == i)

def move4(l, x, i, l_, x_, i_):
    return And(l == 1, x_ == x, l_ == 1, x_ == x, i_ == i)

controller_moves = [move1, move2, move3, move4]

# 4. Define Initial States
def init(l, x, i):
    return l == 0

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "simple":

    # 3. Define Guarantee
    def guarantee(l, x, i):
        return And(l == 1)

    # Spec: F (l == 1)
    reachability_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)

# else:
#     if spec == "product":

#         # Spec: FG(formula) where formula == And(a>=b, b>=c, c>=d)
#         # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

#         nQ = 2
#         def automaton(q, q_, a, b, c, d):
#             return Or(
#                     And(q == 0, q_==1, And(a>=b, b>=c, c>=d)),
#                     And(q == 0, q_==0, Not(And(a>=b, b>=c, c>=d))),
#                     And(q == 1, q_==1, And(a>=b, b>=c, c>=d)),
#                     And(q == 1, q_==0, Not(And(a>=b, b>=c, c>=d)))
#                     )
        
#         def isFinal(p):
#             return p == 0

#         # (Optional): Explicit safety guarantee that complements the omega-regular formula
#         # Default: Returns the True formula in Z3
#         def guarantee(q):
#             return And(True)

#         # Call the fixpoint engine for omega regular specifications.
#         buchi_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, nQ, game_type, init)

#     else:
#         if spec == "bounded":
#             # Only UCW's used in this section (i.e., from the negation of the specification)
#             # Spec: FG(formula) where formula == And(a>=b, b>=c, c>=d)
#             # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

#             nQ = 2
#             def automaton(q, q_, a, b, c, d):
#                 return Or(
#                         And(q == 0, q_==1, And(a>=b, b>=c, c>=d)),
#                         And(q == 0, q_==0, Not(And(a>=b, b>=c, c>=d))),
#                         And(q == 1, q_==1, And(a>=b, b>=c, c>=d)),
#                         And(q == 1, q_==0, Not(And(a>=b, b>=c, c>=d)))
#                         )

#             # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
#             def isFinal(p):
#                 return If(p==1, 1, 0)

#             #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
#             def sigma(a, b, c, d):
#                 return [And(a>=b, b>=c, c>=d), Not(And(a>=b, b>=c, c>=d))]

#             # (Optional): Explicit safety guarantee that complements the omega-regular formula
#             # Default: Returns the True formula in Z3
#             def guarantee(a, b, c, d):
#                 return And(True)

#             # Call the fixpoint engine for omega regular specifications.
#             otfd_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)
#             # otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)

#             # antichain_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)
#             # antichain_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)

#         else:
#             print("Not a valid input: Please enter \"simple\" \"product\" or \"bounded\" as the third argument")