from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 3 variable Sorting Example taken from the paper "Reactive Synthesis Modulo Theories using Abstraction Refinement"
# Spec: FG (a>=b, b>=c)

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
#Environment move is Skip here
def environment(a, b, c, a_, b_, c_):
    return And(a_ == a, b_ == b, c_ == c)

#2. Define Controller moves

# flip(a,b)
def move1(a, b, c, a_, b_, c_):
    return And(a_ == b, b_ == a, c_ == c)

# flip(b,c)
def move2(a, b, c, a_, b_, c_):
    return And(a_ == a, b_ == c, c_ == b)

# skip
def move3(a, b, c, a_, b_, c_):
    return And(a_ == a, b_ == b, c_ == c)

controller_moves = [move1, move2, move3]

# 3. Define Initial States
def init(a, b, c):
    return False

spec_type = sys.argv[1]

if spec_type == "simple":

    # 3. Define Guarantee
    def guarantee(a, b, c):
        return And(a>=b, b>=c)

    # Spec: FG (a>=b, b>=c, c>=d, d>=e)
    cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)

else:
    # If automaton is deterministic, same automaton is enough for both buchi and cobuchi product fixpoints. 
    # If final states are X, just run GF(X) and FG(X) on them to get results for buchi and cobuchi respectively.

    if spec_type == "product-buchi":

        # Complete Deterministic Buchi Automaton for the above specification
        # Functions such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, a, b, c):
            return Or(
                    And(q == 0, q_==1, And(a>=b, b>=c)),
                    And(q == 0, q_==0, Not(And(a>=b, b>=c))),
                    And(q == 1, q_==1, And(a>=b, b>=c)),
                    And(q == 1, q_==0, Not(And(a>=b, b>=c)))
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

                nQ = 2
                def automaton(q, q_, a, b, c):
                    return Or(
                            And(q == 0, q_==1, And(a>=b, b>=c)),
                            And(q == 0, q_==0, Not(And(a>=b, b>=c))),
                            And(q == 1, q_==1, And(a>=b, b>=c)),
                            And(q == 1, q_==0, Not(And(a>=b, b>=c)))
                            )

                # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
                def isFinal(p):
                    return If(p==0, 1, 0)

                #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
                def sigma(a, b, c):
                    return [And(a>=b, b>=c), Not(And(a>=b, b>=c))]

                # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
                def guarantee(a, b, c):
                    return And(True)

                # Call the fixpoint engine for omega regular specifications (k = 0).
                # otfd_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)
                otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)

            else:
                print("Not a valid input: Please enter \"simple\", \"product-buchi\", \"product-co-buchi\", or \"bounded\" as the third argument")