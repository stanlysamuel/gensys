from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Cinderella-Stepmother game of 5 buckets with bucket size of C = 2.0. Here, the controller (protagonist) is Cinderella and it aims to win the game by staying in the safe region i.e., G(safe) or other complex LTL properties
# Specification: Safety, G(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)))
# C = 2.0

# 0. Define game type (Int/ Real)
game_type = "Real"

# 1. Define Environment moves

def environment(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And(b1_ + b2_ + b3_ + b4_ + b5_ == b1 + b2 + b3 + b4 + b5 + 1, b1_>=b1, b2_>=b2, b3_>=b3, b4_>=b4, b5_>=b5)

#2. Define Controller moves

def move1(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b1_ == 0.0,  b2_ == 0.0, b3_ == b3, b4_ == b4, b5_ == b5)

def move2(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b2_ == 0.0,  b3_ == 0.0, b4_ == b4, b5_ == b5, b1_ == b1)

def move3(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b3_ == 0.0,  b4_ == 0.0, b5_ == b5, b1_ == b1, b2_ == b2)

def move4(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b4_ == 0.0,  b5_ == 0.0, b1_ == b1, b2_ == b2, b3_ == b3)

def move5(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b5_ == 0.0,  b1_ == 0.0, b2_ == b2, b3_ == b3, b4_ == b4)

controller_moves = [move1, move2, move3, move4, move5]

#3. Define Init Region (False by default => Maximal winning region will be returned)

def init(b1, b2, b3, b4, b5):
    return And(b1 == 0.0, b2 == 0.0, b3 == 0.0, b4 == 0.0, b5 == 0.0)

# def init(b1, b2, b3, b4, b5):
#     return False

C = 2.0
spec_type = sys.argv[1]

if spec_type == "simple":
    # 3. Define Guarantee
    def guarantee(b1, b2, b3, b4, b5):
        return And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C, b1>=0.0, b2>=0.0, b3>=0.0, b4>=0.0, b5>=0.0)

    safety_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)

else:
    # If automaton is deterministic, same automaton is enough for both buchi and cobuchi product fixpoints. 
    # If final states are X, just run GF(X) and FG(X) on them to get results for buchi and cobuchi respectively.

    if spec_type == "product-buchi":

        # Complete Deterministic Buchi Automaton for the above specification
        # Functions such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, b1, b2, b3, b4, b5):
            return Or(
                    And(q == 0, q_==1, Not(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0))),
                    And(q == 0, q_==0, And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)),
                    And(q == 1, q_==1),
                    )
        
        # Denotes which states in the automaton are final states i.e, those states that should be visited finitely often for every run
        def isFinal(p):
            return p == 0

        def guarantee(q):
            return True
        
        buchi_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, nQ, game_type, init)
        
    else:
        if spec_type == "product-co-buchi":
            nQ = 2
            def automaton(q, q_, b1, b2, b3, b4, b5):
                return Or(
                        And(q == 0, q_==1, Not(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0))),
                        And(q == 0, q_==0, And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)),
                        And(q == 1, q_==1),
                        )
            # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
            def isFinal(p):
                return p == 0

            def guarantee(q):
                return True
        
            cobuchi_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, nQ, game_type, init)

        else:
            if spec_type == "otf":
                # Only Buchi Automatons used in this section (i.e., from the negation of the specification)
                # Deterministic Buchi Automatons can be used in this setting as well. 

                nQ = 2
                def automaton(q, q_, b1, b2, b3, b4, b5):
                    return Or(
                            And(q == 0, q_==1, Not(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0))),
                            And(q == 0, q_==0),
                            And(q == 1, q_==1),
                            )
                # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
                def isFinal(p):
                    return If(p==1, 1, 0)

                #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
                def sigma(b1, b2, b3, b4, b5):
                    return [Not(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)), And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)]

                # (Optional): Explicit safety guarantee that complements the omega-regular formula
                # Default: Returns the True formula in Z3
                def guarantee(b1, b2, b3, b4, b5):
                    return And(True)

                # Call the fixpoint engine for omega regular specifications.
                # otfd_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)
                otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 1, game_type, init)

            else:
                print("Not a valid input: Please enter \"simple\", \"product-buchi\", \"product-co-buchi\", or \"bounded\" as the third argument")