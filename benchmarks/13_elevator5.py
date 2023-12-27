from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Five floor elevator example.
# Spec: General LTL (Liveness), G(1<=x<=3) and G(F(x==1) and F(x==2) and F(x==3) and F(x==4))

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

        nQ = 7
        def automaton(q, q_, x):
            return Or(And(q == 0, q_ == 0, And(And(x>=1, x<=5), x == 1, x == 2, x == 3, x == 4, x == 5)), And(q == 0, q_ == 1, And(And(x>=1, x<=5), Not(x == 5))), And(q == 0, q_ == 2, And(And(x>=1, x<=5), Not(x == 4), x == 5)), And(q == 0, q_ == 3, And(And(x>=1, x<=5), Not(x == 3), x == 4, x == 5)), And(q == 0, q_ == 4, And(And(x>=1, x<=5), Not(x == 2), x == 3, x == 4, x == 5)), And(q == 0, q_ == 5, And(And(x>=1, x<=5), Not(x == 1), x == 2, x == 3, x == 4, x == 5)), And(q == 0, q_ == 6, Not(And(x>=1, x<=5))), And(q == 1, q_ == 0, And(And(x>=1, x<=5), x == 1, x == 2, x == 3, x == 4, x == 5)), And(q == 1, q_ == 1, And(And(x>=1, x<=5), Not(x == 5))), And(q == 1, q_ == 2, And(And(x>=1, x<=5), Not(x == 4), x == 5)), And(q == 1, q_ == 3, And(And(x>=1, x<=5), Not(x == 3), x == 4, x == 5)), And(q == 1, q_ == 4, And(And(x>=1, x<=5), Not(x == 2), x == 3, x == 4, x == 5)), And(q == 1, q_ == 5, And(And(x>=1, x<=5), Not(x == 1), x == 2, x == 3, x == 4, x == 5)), And(q == 1, q_ == 6, Not(And(x>=1, x<=5))), And(q == 2, q_ == 0, And(And(x>=1, x<=5), x == 1, x == 2, x == 3, x == 4)), And(q == 2, q_ == 2, And(And(x>=1, x<=5), Not(x == 4))), And(q == 2, q_ == 3, And(And(x>=1, x<=5), Not(x == 3), x == 4)), And(q == 2, q_ == 4, And(And(x>=1, x<=5), Not(x == 2), x == 3, x == 4)), And(q == 2, q_ == 5, And(And(x>=1, x<=5), Not(x == 1), x == 2, x == 3, x == 4)), And(q == 2, q_ == 6, Not(And(x>=1, x<=5))), And(q == 3, q_ == 0, And(And(x>=1, x<=5), x == 1, x == 2, x == 3)), And(q == 3, q_ == 3, And(And(x>=1, x<=5), Not(x == 3))), And(q == 3, q_ == 4, And(And(x>=1, x<=5), Not(x == 2), x == 3)), And(q == 3, q_ == 5, And(And(x>=1, x<=5), Not(x == 1), x == 2, x == 3)), And(q == 3, q_ == 6, Not(And(x>=1, x<=5))), And(q == 4, q_ == 0, And(And(x>=1, x<=5), x == 1, x == 2)), And(q == 4, q_ == 4, And(And(x>=1, x<=5), Not(x == 2))), And(q == 4, q_ == 5, And(And(x>=1, x<=5), Not(x == 1), x == 2)), And(q == 4, q_ == 6, Not(And(x>=1, x<=5))), And(q == 5, q_ == 0, And(And(x>=1, x<=5), x == 1)), And(q == 5, q_ == 5, And(And(x>=1, x<=5), Not(x == 1))), And(q == 5, q_ == 6, Not(And(x>=1, x<=5))), And(q == 6, q_ == 6))
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

                # Use exit code 6 to denote timeout. (We know the otf approach does not scale beyond 3 floors, thus we do not manually convert the automaton here. This will be automated in future versions).
                sys.exit(6)

            else:
                print("Not a valid input: Please enter \"simple\", \"product-buchi\", \"product-co-buchi\", or \"bounded\" as the third argument")