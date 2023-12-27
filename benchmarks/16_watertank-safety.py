from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Two Water Tanks example TSL(LRA)
# Spec: Safety, G(formula) where formula == And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7)

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

spec_type = sys.argv[1]

if spec_type == "simple":

    # 3. Define Guarantee
    def guarantee(x1, x2):
        return And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7)

    safety_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)

else:
    # If automaton is deterministic, same automaton is enough for both buchi and cobuchi product fixpoints. 
    # If final states are X, just run GF(X) and FG(X) on them to get results for buchi and cobuchi respectively.

    if spec_type == "product-buchi":

        # Complete Deterministic Buchi Automaton for the above specification
        # Functions such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, x1, x2):
            return Or(
                    And(q == 0, q_==1, Not(And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7))),
                    And(q == 0, q_==0, And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7)),
                    And(q == 1, q_==1),
                    )
        
        def isFinal(p):
            return p == 0
        
        # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
        def guarantee(q):
            return True
        
        buchi_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, nQ, game_type, init)
        
    else:
        if spec_type == "product-co-buchi":

            nQ = 2
            def automaton(q, q_, x1, x2):
                return Or(
                        And(q == 0, q_==1, Not(And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7))),
                        And(q == 0, q_==0, And(x1>=0.1, x1<0.7, x2>=0.1, x2<0.7)),
                        And(q == 1, q_==1),
                        )
            
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

                # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
                def guarantee(x1, x2):
                    return And(True)

                # Call the fixpoint engine for omega regular specifications (k = 0).
                # otfd_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)
                otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)

            else:
                print("Not a valid input: Please enter \"simple\", \"product-buchi\", \"product-co-buchi\", or \"bounded\" as the third argument")