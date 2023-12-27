from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Synth Synchronization example: Beyene et. al. POPL 2014 taken from Vechev et. al. POPL 2010, Figure 1.
# Case of three threads; all possible interleavings are enumerated and the controller is required to find a strategy that avoids the assertion failure at program 3 line 3.
# Spec: Safety, G(formula) where formula == Not(And(pc3 == 3, y1 == y2))

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
#Environment move is Skip here
def environment(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return And(x == x_, y1 == y1_, y2 == y2_, z == z_, pc1 == pc1_, pc2 == pc2_, pc3 == pc3_)

#2. Define Controller moves

#Transition System 1

def move1(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return Or(  # Single transitions
                And(pc1 == 1, pc1_ == 2, x_ == x + z, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc3_ == pc3),
                And(pc1 == 2, pc1_ == 3, x_ == x + z, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc3_ == pc3),
                # Making it complete
                And(Or(pc1<=0, pc1>=3), pc1_ == pc1, x_ == x, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc3_ == pc3)
                # Atomic Sections
                # And(pc1 == 1, pc1_ == 3, x_ == x + z + z, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc3_ == pc3)
                )

def move2(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return Or(  # Single transitions
                And(pc2 == 1, pc2_ == 2, z_ == z + 1, y1_ == y1, y2_ == y2, x_ == x, pc1_ == pc1, pc3_ == pc3),
                And(pc2 == 2, pc2_ == 3, z_ == z + 1, y1_ == y1, y2_ == y2, x_ == x, pc1_ == pc1, pc3_ == pc3),
                # Making it complete
                And(Or(pc2<=0, pc2>=3), pc2_ == pc2, x_ == x, y1_ == y1, y2_ == y2, z_ == z, pc1_ == pc1, pc3_ == pc3)
                # Atomic Sections
                # And(pc2 == 1, pc2_ == 3, z_ == z + 2, y1_ == y1, y2_ == y2, x_ == x, pc1_ == pc1, pc3_ == pc3)
                )

def move3(x, y1, y2, z, pc1, pc2, pc3, x_, y1_, y2_, z_, pc1_, pc2_, pc3_):
    return Or(  # Single transitions
                And(pc3 == 1, pc3_ == 2, x == 1, y1_ == 3, y2_ == y2, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 1, pc3_ == 2, x == 2, y1_ == 6, y2_ == y2, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 1, pc3_ == 2, Or(x<=0, x>=3), y1_ == 5, y2_ == y2, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 2, pc3_ == 3, y2_ == x, x_ == x, y1_ == y1, z_ == z, pc2_ == pc2, pc1_ == pc1),
                And(pc3 == 3, pc3_ == 4, y1 != y2, x_ == x, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc1_ == pc1),
                # Making it complete
                And(Or(pc3<=0, pc3>=4), pc3_ == pc3, x_ == x, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc1_ == pc1)
                # Atomic Sections
                # And(pc3 == 1, pc3_ == 3, x == 1, y1_ == 3, y2_ == x, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                # And(pc3 == 1, pc3_ == 3, x == 2, y1_ == 6, y2_ == x, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                # And(pc3 == 1, pc3_ == 3, Or(x<=0, x>=3), y1_ == 5, y2_ == x, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                # And(pc3 == 2, pc3_ == 4, Or(y1>=x+1, x>=y1+1), y2_ == x, x_ == x, y1_ == y1, z_ == z, pc2_ == pc2, pc1_ == pc1),
                # And(pc3 == 1, pc3_ == 4, x == 1, y1_ == 3, y2_ == x, Or(2>= x, x>=4), x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                # And(pc3 == 1, pc3_ == 4, x == 2, y1_ == 6, y2_ == x, Or(5>= x, x>=7), x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1),
                # And(pc3 == 1, pc3_ == 4, Or(x<=0, x>=3), y1_ == 5, y2_ == x, Or(4>= x, x>=6), x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1)
                
                )

controller_moves = [move1, move2, move3]


#3. Define Init Region (False by default => Maximal winning region will be returned)

def init(x, y1, y2, z, pc1, pc2, pc3):
    return And(x == 0, y1 == 0, y2 == 0, z == 0, pc1 == 1, pc2 == 1, pc3 == 1)

# def init(pc, l, gl):
#     return False

spec_type = sys.argv[1]

if spec_type == "simple":

    # 3. Define Guarantee
    def guarantee(x, y1, y2, z, pc1, pc2, pc3):
        return And(Not(And(pc3 == 3, y1 == y2)))

    safety_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)

else:
    # If automaton is deterministic, same automaton is enough for both buchi and cobuchi product fixpoints. 
    # If final states are X, just run GF(X) and FG(X) on them to get results for buchi and cobuchi respectively.

    if spec_type == "product-buchi":

        # Complete Deterministic Buchi Automaton for the above specification
        # Functions such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, x, y1, y2, z, pc1, pc2, pc3):
            return Or(
                    And(q == 0, q_==1, And(pc3 == 3, y1 == y2)),
                    And(q == 0, q_==0, Not(And(pc3 == 3, y1 == y2))),
                    And(q == 1, q_==1)
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
            def automaton(q, q_, x, y1, y2, z, pc1, pc2, pc3):
                return Or(
                        And(q == 0, q_==1, And(pc3 == 3, y1 == y2)),
                        And(q == 0, q_==0, Not(And(pc3 == 3, y1 == y2))),
                        And(q == 1, q_==1)
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
                def automaton(q, q_, x, y1, y2, z, pc1, pc2, pc3):
                    return Or(
                            And(q == 0, q_==1, And(pc3 == 3, y1 == y2)),
                            And(q == 0, q_==0, Not(And(pc3 == 3, y1 == y2))),
                            And(q == 1, q_==1)
                            )

                # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
                def isFinal(p):
                    return If(p==1, 1, 0)

                # Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
                def sigma(x, y1, y2, z, pc1, pc2, pc3):
                    return [Not(And(pc3 == 3, y1 == y2)), And(pc3 == 3, y1 == y2)]

                # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
                def guarantee(x, y1, y2, z, pc1, pc2, pc3):
                    return And(True)

                # Call the fixpoint engine for omega regular specifications (k = 0).
                # otfd_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)
                otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)

            else:
                print("Not a valid input: Please enter \"simple\", \"product-buchi\", \"product-co-buchi\", or \"bounded\" as the third argument")