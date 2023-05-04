from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Three floor elevator example.

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
def environment(x,x_):
    return And(x_ == x)

#2. Define Controller moves

def move1(x,x_):
    return And(x_ == x)

def move2(x,x_):
    return And(x_ == x+1)

def move3(x,x_):
    return And(x_ == x-1)

# Define initial state
def init(x):
    return And(x>=1, x<=5)

# def init(x):
#     return False

controller_moves = [move1, move2, move3]

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "product":
    # Spec: Liveness, G(1<=x<=3) and G(F(x==1) and F(x==2) and F(x==3) and F(x==4))
    # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

    # Deterministic Buchi Automaton
    nQ = 7
    def automaton(q, q_, x):
        return Or(And(q == 0, q_ == 0, And(And(x>=1, x<=5), x == 1, x == 2, x == 3, x == 4, x == 5)), And(q == 0, q_ == 1, And(And(x>=1, x<=5), Not(x == 5))), And(q == 0, q_ == 2, And(And(x>=1, x<=5), Not(x == 4), x == 5)), And(q == 0, q_ == 3, And(And(x>=1, x<=5), Not(x == 3), x == 4, x == 5)), And(q == 0, q_ == 4, And(And(x>=1, x<=5), Not(x == 2), x == 3, x == 4, x == 5)), And(q == 0, q_ == 5, And(And(x>=1, x<=5), Not(x == 1), x == 2, x == 3, x == 4, x == 5)), And(q == 0, q_ == 6, Not(And(x>=1, x<=5))), And(q == 1, q_ == 0, And(And(x>=1, x<=5), x == 1, x == 2, x == 3, x == 4, x == 5)), And(q == 1, q_ == 1, And(And(x>=1, x<=5), Not(x == 5))), And(q == 1, q_ == 2, And(And(x>=1, x<=5), Not(x == 4), x == 5)), And(q == 1, q_ == 3, And(And(x>=1, x<=5), Not(x == 3), x == 4, x == 5)), And(q == 1, q_ == 4, And(And(x>=1, x<=5), Not(x == 2), x == 3, x == 4, x == 5)), And(q == 1, q_ == 5, And(And(x>=1, x<=5), Not(x == 1), x == 2, x == 3, x == 4, x == 5)), And(q == 1, q_ == 6, Not(And(x>=1, x<=5))), And(q == 2, q_ == 0, And(And(x>=1, x<=5), x == 1, x == 2, x == 3, x == 4)), And(q == 2, q_ == 2, And(And(x>=1, x<=5), Not(x == 4))), And(q == 2, q_ == 3, And(And(x>=1, x<=5), Not(x == 3), x == 4)), And(q == 2, q_ == 4, And(And(x>=1, x<=5), Not(x == 2), x == 3, x == 4)), And(q == 2, q_ == 5, And(And(x>=1, x<=5), Not(x == 1), x == 2, x == 3, x == 4)), And(q == 2, q_ == 6, Not(And(x>=1, x<=5))), And(q == 3, q_ == 0, And(And(x>=1, x<=5), x == 1, x == 2, x == 3)), And(q == 3, q_ == 3, And(And(x>=1, x<=5), Not(x == 3))), And(q == 3, q_ == 4, And(And(x>=1, x<=5), Not(x == 2), x == 3)), And(q == 3, q_ == 5, And(And(x>=1, x<=5), Not(x == 1), x == 2, x == 3)), And(q == 3, q_ == 6, Not(And(x>=1, x<=5))), And(q == 4, q_ == 0, And(And(x>=1, x<=5), x == 1, x == 2)), And(q == 4, q_ == 4, And(And(x>=1, x<=5), Not(x == 2))), And(q == 4, q_ == 5, And(And(x>=1, x<=5), Not(x == 1), x == 2)), And(q == 4, q_ == 6, Not(And(x>=1, x<=5))), And(q == 5, q_ == 0, And(And(x>=1, x<=5), x == 1)), And(q == 5, q_ == 5, And(And(x>=1, x<=5), Not(x == 1))), And(q == 5, q_ == 6, Not(And(x>=1, x<=5))), And(q == 6, q_ == 6))
    def isFinal(p):
        return p == 0

    # (Optional): Explicit safety guarantee that complements the omega-regular formula
    # Default: Returns the True formula in Z3
    def guarantee(q):
        return And(True)

    # Call the fixpoint engine for omega regular specifications.
    buchi_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, nQ, game_type, init)


else:
    if spec == "bounded":
        # Spec: Safety, G(formula) where formula = And(x<=3, x>=0)
        # Complete Universal Co-Buchi Automaton from spot encoded in LRA.
        # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 6
        def automaton(q, q_, x):
            return Or(
                    And(q == 0, q_==0, And(x>=1, x<=3)),
                    And(q == 0, q_==1, Not(And(x>=1, x<=3))),
                    And(q == 1, q_==1),
                    And(q == 0, q_==2, And(x>=1, x<=3, x!=1)),
                    And(q == 2, q_==2, x!=1),
                    And(q == 2, q_==5, x==1),
                    And(q == 0, q_==3, And(x>=1, x<=3, x!=2)),
                    And(q == 3, q_==3, x!=2),
                    And(q == 3, q_==5, x==2),
                    And(q == 0, q_==4, And(x>=1, x<=3, x!=3)),
                    And(q == 4, q_==4, x!=3),
                    And(q == 4, q_==5, x==3),
                    And(q == 5, q_==5),
                    )
        # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
        def isFinal(p):
            return If(And(p <=4, p >=1), 1, 0)

        #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
        def sigma(x):
            return [x == 1, x == 2, x == 3, Not(And(x>=1, x<=3))]

        # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # Default: Returns the True formula in Z3
        def guarantee(x):
            return And(True)

        # Call the fixpoint engine for omega regular specifications.
        for i in range(0,7):
            otfd_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, i, game_type, init)
        # antichain_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 6, game_type)
        # otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 6, game_type, init)
        # antichain_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 6, game_type)
    
    else:
        print("Not a valid input: Please enter \"safety\" or \"omega\" as the third argument")
