# Two Water Tanks example TSL(LRA)

from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 0. Define game type (Int/ Real)
game_type = "Real"

# 1. Define Environment moves
def environment(x, x_):
    return And(x_ == x)

# 2. Define Controller moves
def move1(x, x_):
    return And(x_ == 0.9635*x)

def move2(x, x_):
    return And(x_ == 0.9635*x + 0.1)

controller_moves = [move1, move2]

# 3. Define Initial States
def init(x):
    return And(x>= 0.0, x<0.7)

# def init(x):
#     return False

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "product":

    # Spec: G (And(x>= 0.0, x<0.7)) & G( x<0.1 -> F x>=0.4)
    # Co-Buchi Automaton is not deterministc but Buchi automaton is.
    # Complete Universal Co-Buchi Automaton from spot encoded in LRA.
    # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

    # Buchi Automata details for Spec from spot: G (p) & G( x1 -> F x2)
    # Initial State: 0
    # Final States: [0]
    # Is deterministic? True
    # Atomic propositions: (spot.formula("p"), spot.formula("x1"), spot.formula("x2"))
    # Transitions:
    # 0 ->  (0, (p & !x1) | (p & x2)) (1, p & x1 & !x2) (2, !p) 
    # 1 ->  (0, p & x2) (1, p & !x2) (2, !p) 
    # 2 ->  (2, 1)

    nQ = 3
    def automaton(q, q_, x):
        return Or(
                And(q == 0, q_==0, Or(And(x>= 0.0, x<0.7, Not(x<0.1)), And(x>= 0.0, x<0.7, x>=0.4))),
                And(q == 0, q_==1, And(x>= 0.0, x<0.7, x<0.1 , x<0.4 )),
                And(q == 0, q_==2, Not(And(x>= 0.0, x<0.7))),
                And(q == 1, q_==0, And(x>= 0.0, x<0.7, x>=0.4)),
                And(q == 1, q_==1, And(x>= 0.0, x<0.7, x<0.4)),
                And(q == 1, q_==2, Not(And(x>= 0.0, x<0.7))),
                And(q == 2, q_==2)
                )
    # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
    def isFinal(p):
        return p == 0

    # (Optional): Explicit safety guarantee that complements the omega-regular formula
    # Default: Returns the True formula in Z3
    def guarantee(x):
        return And(True)

    buchi_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, nQ, game_type, init)

else:
    if spec == "bounded":
        # Only UCW's used in this section (i.e., from the negation of the specification)
        # Spec: G (And(x>= 0.0, x<0.7)) & G( x<0.1 -> F x>=0.4)
        # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        # 2 FLOOR EXAMPLE
        # UCW details: 
        # Initial State: 0
        # Final States: [1, 2]
        # Is deterministic? maybe
        # Atomic propositions: (spot.formula("p"), spot.formula("x1"), spot.formula("x2"))
        # Transitions:
        # 0 ->  (0, p) (1, !p) (2, p & x1 & !x2) 
        # 1 ->  (1, 1) 
        # 2 ->  (2, !x2) (3, x2) 
        # 3 ->  (3, 1) 

        nQ = 4
        def automaton(q, q_, x):
            return Or(
                    And(q == 0, q_==0, And(x>= 0.0, x<0.7)),
                    And(q == 0, q_==1, Not(And(x>= 0.0, x<0.7))),
                    And(q == 0, q_==2, And(x>= 0.0, x<0.7, x<0.1 , x<0.4 )),
                    And(q == 1, q_==1),
                    And(q == 2, q_==2, x<0.4),
                    And(q == 2, q_==3, x>=0.4),
                    And(q == 3, q_==3)
                    )

        # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
        def isFinal(p):
            return If(Or(p == 1, p == 2), 1, 0)

        #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
        def sigma(x):
            return [And(x>=0.0, x<0.1), And(x>=0.1, x<0.4), And(x>=0.4, x<0.7), Or(x<0.0, x>=0.7)]

        # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # Default: Returns the True formula in Z3
        def guarantee(x):
            return And(True)

        # Call the fixpoint engine for omega regular specifications.
        # for i in range(0, 10):
        #     print("Iteration: ", i)
        # otfd_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)
        # otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)

        antichain_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)
        # antichain_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)

    else:
        print("Not a valid input: Please enter \"product\" or \"bounded\" as the third argument")