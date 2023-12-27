from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Evasion game: Neider et. al., TACAS 2016 and DTSynth Tool, FMCAD 2019
# Two robots are moving in an infinite, discrete two-dimensional grid world. The robots take turns
# moving at most one cell in any direction. Each players
# controls one robot. Player 0's objective is to avoid getting
# caught by Player 1's robot

# Specification: Safety: G(formula) where formula = Not(And(x1==x2, y1==y2))

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
def environment(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(Or(x1_ == x1 + 1, x1_ == x1 - 1, x1_ == x1), Or(y1_ == y1 + 1, y1_ == y1 - 1, y1_ == y1),x2_==x2, y2_==y2)

# 2. Define Controller moves

def move1(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2, y2_ == y2, x1_==x1, y1_==y1)

def move2(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2+1, y2_ == y2, x1_==x1, y1_==y1)

def move3(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2-1, y2_ == y2, x1_==x1, y1_==y1)

def move4(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2, y2_ == y2 + 1, x1_==x1, y1_==y1)

def move5(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2+1, y2_ == y2 + 1, x1_==x1, y1_==y1)

def move6(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2-1, y2_ == y2 + 1, x1_==x1, y1_==y1)

def move7(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2, y2_ == y2 - 1, x1_==x1, y1_==y1)

def move8(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2+1, y2_ == y2 - 1, x1_==x1, y1_==y1)

def move9(x1,y1,x2,y2,x1_,y1_,x2_,y2_):
    return And(x2_ == x2-1, y2_ == y2 - 1, x1_==x1, y1_==y1)

controller_moves = [move1, move2, move3, move4, move5, move6, move7, move8, move9]

# 3. Define Initial Condition

def init(x1,y1,x2,y2):
    return And(x1 == 0, y1 == 0, x2 == 0, y2 == 0)

# def init(x1,y1,x2,y2):
#     return False

spec_type = sys.argv[1]

if spec_type == "simple":

    # 3. Define Guarantee
    def guarantee(x1,y1,x2,y2):
        return Not(And(x1==x2, y1==y2))

    safety_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)

else:
    # If automaton is deterministic, same automaton is enough for both buchi and cobuchi product fixpoints. 
    # If final states are X, just run GF(X) and FG(X) on them to get results for buchi and cobuchi respectively.

    if spec_type == "product-buchi":

        # Complete Deterministic Buchi Automaton for the above specification
        # Functions such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, x1,y1,x2,y2):
            return Or(
                    And(q == 0, q_==1, Not(Not(And(x1==x2, y1==y2)))),
                    And(q == 0, q_==0, Not(And(x1==x2, y1==y2))),
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
            def automaton(q, q_, x1,y1,x2,y2):
                return Or(
                        And(q == 0, q_==1, Not(Not(And(x1==x2, y1==y2)))),
                        And(q == 0, q_==0, Not(And(x1==x2, y1==y2))),
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
                def automaton(q, q_, x1,y1,x2,y2):
                    return Or(
                            And(q == 0, q_==1, Not(Not(And(x1==x2, y1==y2)))),
                            And(q == 0, q_==0),
                            And(q == 1, q_==1),
                            )
                # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
                def isFinal(p):
                    return If(p==1, 1, 0)

                # Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
                def sigma(x1,y1,x2,y2):
                    return [Not(And(x1==x2, y1==y2)), Not(Not(And(x1==x2, y1==y2)))]

                # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
                def guarantee(x1,y1,x2,y2):
                    return And(True)

                # Call the fixpoint engine for omega regular specifications (k = 0).
                # otfd_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)
                otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)

            else:
                print("Not a valid input: Please enter \"simple\", \"product-buchi\", \"product-co-buchi\", or \"bounded\" as the third argument")