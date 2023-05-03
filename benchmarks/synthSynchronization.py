from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Synth Synchronization example: Beyene et. al. POPL 2014 taken from Vechev et. al. POPL 2010, Figure 1.
# Case of three threads.
# All possible interleavings are enumerated and the controller is required to find a strategy that avoids the assertion failure at program 3 line 3

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

def init(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
    return And(pc1==1,pc2==1, f1a==0, f1b==0, t1b==0, f2a==0, f2b==0, t2b==0)

# def init(pc, l, gl):
#     return False

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "simple":

    # 3. Define Guarantee
    def guarantee(x, y1, y2, z, pc1, pc2, pc3):
        return And(Not(And(pc3 == 3, y1 == y2)))

    safety_fixedpoint_gensys(controller_moves, environment, guarantee, int(mode), game_type, init)

else:
    if spec == "product":

        # Spec: Safety, G(formula) where formula == And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7)))
        # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
            return Or(
                    And(q == 0, q_==1, Not(And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7))))),
                    And(q == 0, q_==0, And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7)))),
                    And(q == 1, q_==1),
                    )
        
        def isFinal(p):
            return p == 0

        # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # Default: Returns the True formula in Z3
        def guarantee(q):
            return And(True)

        # Call the fixpoint engine for omega regular specifications.
        # buchi_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, nQ, game_type, init)
        cobuchi_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, nQ, game_type, init)


    else:
        if spec == "bounded":
            # Only UCW's used in this section (i.e., from the negation of the specification)
            # Spec: Safety, G(formula) where formula == And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7)))
            # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

            nQ = 2
            def automaton(q, q_, f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
                return Or(
                        And(q == 0, q_==1, Not(And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7))))),
                        And(q == 0, q_==0, And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7)))),
                        And(q == 1, q_==1),
                        )

            # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
            def isFinal(p):
                return If(p==1, 1, 0)

            #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
            def sigma(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
                return [And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7))), Not(And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7))))]

            # (Optional): Explicit safety guarantee that complements the omega-regular formula
            # Default: Returns the True formula in Z3
            def guarantee(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
                return And(True)

            # Spec: Safety, G(formula) where formula == Not(Or(And(pc==2, l == 1),And(pc == 5, l == 0)))
            # Complete Universal Co-Buchi Automaton from spot encoded in LRA.
            # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

            # nQ = 6
            # def automaton(q, q_, f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
            #     return Or(
            #             And(q == 0, q_==0),
            #             And(q == 0, q_==1, And(pc1 == 3, pc1 !=4)),
            #             And(q == 0, q_==2, And(pc1 == 7, pc1 !=8)),
            #             And(q == 0, q_==3, And(pc2 == 3, pc2 !=4)),
            #             And(q == 0, q_==4, And(pc2 == 6, pc2 !=7)),
            #             And(q == 1, q_==1, pc1 !=4),
            #             And(q == 1, q_==5, pc1 == 4),
            #             And(q == 2, q_==2, pc1 !=8),
            #             And(q == 2, q_==5, pc1 == 8),
            #             And(q == 3, q_==3, pc2 !=4),
            #             And(q == 3, q_==5, pc2 == 4),
            #             And(q == 4, q_==4, pc2 !=7),
            #             And(q == 4, q_==5, pc2 == 7),
            #             And(q == 5, q_==5)
            #             )
            # # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
            # def isFinal(p):
            #     return If(And(p>=1, p<=4), 1, 0)

            # #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
            # def sigma(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
            #     return []

            # # (Optional): Explicit safety guarantee that complements the omega-regular formula
            # # Default: Returns the True formula in Z3
            # def guarantee(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
            #     return And(True)

            # Call the fixpoint engine for omega regular specifications.
            # otfd_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)
            # otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)

            # antichain_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)
            antichain_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)

        else:
            print("Not a valid input: Please enter \"simple\" \"product\" or \"bounded\" as the third argument")
