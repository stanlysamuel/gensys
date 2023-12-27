from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Limited Box example: Neider et. al., TACAS 2016 and DTSynth Tool, FMCAD 2019
# A variation of the box game. Player 0 can
# only control the robot's vertical movement and Player 1
# the horizontal.

# Specification: Safety: G(formula) where formula = And(x<=3, x>=0)

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
def environment(x,y,x_,y_):
    return And(Or(x_ == x + 1, x_ == x - 1, x_ == x), y_ == y)

#2. Define Controller moves

def move1(x,y,x_,y_):
    return And(x_ == x, y_ == y)

def move2(x,y,x_,y_):
    return And(x_ == x, y_ == y+1)

def move3(x,y,x_,y_):
    return And(x_ == x, y_ == y-1)

controller_moves = [move1, move2, move3]

# 3. Define Initial Condition

def init(x,y):
    return And(x == 0, y == 0)

# def init(x,y):
#     return False

spec_type = sys.argv[1]

if spec_type == "simple":

    # 3. Define Guarantee
    def guarantee(x, y):
        return And(x<=3, x>=0)

    safety_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)

else:
    # If automaton is deterministic, same automaton is enough for both buchi and cobuchi product fixpoints. 
    # If final states are X, just run GF(X) and FG(X) on them to get results for buchi and cobuchi respectively.

    if spec_type == "product-buchi":

        # Complete Deterministic Buchi Automaton for the above specification
        # Functions such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, x, y):
            return Or(
                    And(q == 0, q_==1, Not(And(x<=3, x>=0))),
                    And(q == 0, q_==0, And(x<=3, x>=0)),
                    And(q == 1, q_==1),
                    )
        
        # Denotes which states in the automaton are final states i.e, those states that should be visited finitely often for every run
        def isFinal(p):
            return p == 0

        # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
        def guarantee(q):
            return True
        
        buchi_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, nQ, game_type, init)
        
    else:
        if spec_type == "product-co-buchi":
            nQ = 2
            def automaton(q, q_, x, y):
                return Or(
                        And(q == 0, q_==1, Not(And(x<=3, x>=0))),
                        And(q == 0, q_==0, And(x<=3, x>=0)),
                        And(q == 1, q_==1),
                        )
            
            # Denotes which states in the automaton are final states i.e, those states that should be visited finitely often for every run
            def isFinal(p):
                return p == 0

            # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
            def guarantee(q):
                return True
        
            cobuchi_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, nQ, game_type, init)

        else:
            if spec_type == "otf":
                # Only Buchi Automatons used in this section (i.e., from the negation of the specification)
                # Deterministic Buchi Automatons can be used in this setting as well. 

                nQ = 2
                def automaton(q, q_, x, y):
                    return Or(
                            And(q == 0, q_==1, Not(And(x<=3, x>=0))),
                            And(q == 0, q_==0),
                            And(q == 1, q_==1),
                            )
                # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
                def isFinal(p):
                    return If(p==1, 1, 0)

                # Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
                def sigma(x, y):
                    return [And(x<=3, x>=0), Not(And(x<=3, x>=0))]

                # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
                def guarantee(x, y):
                    return And(True)

                # Call the fixpoint engine for omega regular specifications (k = 0).
                # otfd_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)
                otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)

            else:
                print("Not a valid input: Please enter \"simple\", \"product-buchi\", \"product-co-buchi\", or \"bounded\" as the third argument")