from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Two Water Tanks example TSL(LRA)
# Spec: General LTL (Liveness), G (And(x>= 0.0, x<0.7)) & G( x<0.1 -> F x>=0.4)

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

spec_type = sys.argv[1]

if spec_type == "simple":

    # Not applicable for non-simple LTL specifications
    # Use exit code 5 to denote N/A.
    sys.exit(5)

else:
    # If automaton is deterministic, same automaton is enough for both buchi and cobuchi product fixpoints. 
    # If final states are X, just run GF(X) and FG(X) on them to get results for buchi and cobuchi respectively.

    if spec_type == "product-buchi":

        # Complete Deterministic Buchi Automaton for the above specification
        # Functions such as automaton, isFinal and nQ can be retreived from spot tool manually.

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
        def isFinal(p):
            return p == 0
        
        # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
        def guarantee(q):
            return True
        
        buchi_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, nQ, game_type, init)
        
    else:
        if spec_type == "product-co-buchi":

            # Not applicable Co-Buchi automaton is not deterministic.
            # Use exit code 5 to denote N/A.
            sys.exit(5)

        else:
            if spec_type == "otf":
                # Only Buchi Automatons used in this section (i.e., from the negation of the specification)
                # Deterministic Buchi Automatons can be used in this setting as well. 

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

                # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
                def guarantee(x):
                    return And(True)

                # Call the fixpoint engine for omega regular specifications (k = 0).
                # otfd_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)
                otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)

            else:
                print("Not a valid input: Please enter \"simple\", \"product-buchi\", \"product-co-buchi\", or \"bounded\" as the third argument")