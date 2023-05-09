# Two Water Tanks example TSL(LRA)

from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 0. Define game type (Int/ Real)
game_type = "Real"

# 1. Define Environment moves
def environment(x1, x2, x1_, x2_):
    return And(x1_ == x1, x2_ == x2)

def move1(x1, x2, x1_, x2_):
    return Implies(And(x1< 0.2, x2<0.2), And(x1_ == x1, x2_ == 0.9635*x2))

def move2(x1, x2, x1_, x2_):
    return Implies(And(x1< 0.2, x2<0.2), And(x1_ == x1 + 0.0003 * 324.6753, x2_ == 0.9635*x2))

def move3(x1, x2, x1_, x2_):
    return Implies(Or(x1>= 0.2, x2>=0.2), And(x1_ == 0.8281*x1 + 0.1719*x2, x2_ == 0.7916*x2 + 0.1719*x1))

def move4(x1, x2, x1_, x2_):
    return Implies(Or(x1>= 0.2, x2>=0.2), And(x1_ == 0.8281*x1 + 0.1719*x2 + 0.0003*324.6753, x2_ == 0.7916*x2 + 0.1719*x1))

controller_moves = [move1, move2, move3, move4]

# 4. Define Initial States
def init(x1, x2):
    return And(x1>= 0.2, x1<0.7, x2>=0.2, x2<0.7)

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "simple":

    # 3. Define Guarantee
    def guarantee(x1, x2):
        return And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7)

    safety_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type, init)

else:
    if spec == "product":

        # Spec: Safety, G(formula) where formula == And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7)
        # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, x1, x2):
            return Or(
                    And(q == 0, q_==1, Not(And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7))),
                    And(q == 0, q_==0, And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7)),
                    And(q == 1, q_==1),
                    )
        
        def isFinal(p):
            return p == 0

        # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # Default: Returns the True formula in Z3
        def guarantee(q):
            return And(True)

        # Call the fixpoint engine for omega regular specifications.
        buchi_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, nQ, game_type, init)
        # cobuchi_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, nQ, game_type, init)

    else:
        if spec == "bounded":
            # Only UCW's used in this section (i.e., from the negation of the specification)
            # Spec: Safety, G(formula) where formula == And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7)
            # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

            nQ = 2
            def automaton(q, q_, x1, x2):
                return Or(
                        And(q == 0, q_==1, Not(And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7))),
                        And(q == 0, q_==0, And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7)),
                        And(q == 1, q_==1),
                        )

            # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
            def isFinal(p):
                return If(p==1, 1, 0)

            #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
            def sigma(x1, x2):
                return [And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7), Not(And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7))]

            # (Optional): Explicit safety guarantee that complements the omega-regular formula
            # Default: Returns the True formula in Z3
            def guarantee(x1, x2):
                return And(True)

            # Call the fixpoint engine for omega regular specifications.
            otfd_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)
            # otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)

            # antichain_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)
            # antichain_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)

        else:
            print("Not a valid input: Please enter \"simple\" \"product\" or \"bounded\" as the third argument")