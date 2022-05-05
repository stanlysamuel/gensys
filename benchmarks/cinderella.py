from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Cinderella-Stepmother game of 5 buckets with bucket size of C. Here, the controller (protagonist) is Cinderella and it aims to win the game by staying in the safe region i.e., G(safe).

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

C = sys.argv[1]
mode = sys.argv[2]
spec = sys.argv[3]

if spec == "safety":
    # 3. Define Guarantee
    def guarantee(b1, b2, b3, b4, b5):
        return And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)

    safety_fixedpoint(controller_moves, environment, guarantee, int(mode))

else:
    if spec == "omega":

        # Spec 1: Safety, G(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)))
        # Complete Universal Co-Buchi Automaton from spot encoded in LRA.
        # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

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
        omega_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ)

        # --------------------------------------------------------------------------------------------------------------------------------

        # # Spec 2: Buchi, GF(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)))
        # # Complete Universal Co-Buchi Automaton from spot encoded in LRA.
        # # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        # nQ = 3
        # def automaton(q, q_, b1, b2, b3, b4, b5):
        #     return Or(
        #             And(q == 0, q_==0),
        #             And(q == 0, q_==1, Not(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0))),
        #             And(q == 1, q_==1, Not(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0))),
        #             And(q == 1, q_==2, And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)),
        #             And(q == 2, q_==2),
        #             )
        # # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
        # def isFinal(p):
        #     return If(p==1, 1, 0)

        # #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
        # def sigma(b1, b2, b3, b4, b5):
        #     return [Not(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)), And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)]

        # # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # # Default: Returns the True formula in Z3
        # def guarantee(b1, b2, b3, b4, b5):
        #     return And(True)

        # # Call the fixpoint engine for omega regular specifications.
        # omega_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ)

        # --------------------------------------------------------------------------------------------------------------------------------

        # # Spec 3: LTL, GF(And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)))
        # # Complete Universal Co-Buchi Automaton from spot encoded in LRA.
        # # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        # nQ = 5
        # def automaton(q, q_, b1, b2, b3, b4, b5):
        #     p0 = And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)
        #     p1 = b1 > C
        #     p2 = And(b1 <= C, b2 > C)
        #     return Or(
        #             And(q == 0, q_==0),
        #             And(q == 0, q_==1, And(Not(p0), p1)),
        #             And(q == 0, q_==2, And(Not(p0), Not(p2))),
        #             And(q == 1, q_==1, And(Not(p0), p1)),
        #             And(q == 1, q_==3, And(Not(p0), Not(p1))),
        #             And(q == 1, q_==4, p0),
        #             And(q == 2, q_==2, And(Not(p0), Not(p2))),
        #             And(q == 2, q_==4, Or(p0, p2)),
        #             And(q == 3, q_==1, And(Not(p0), p1)),
        #             And(q == 3, q_==3, And(Not(p0), Not(p1))),
        #             And(q == 3, q_==4, p0),
        #             And(q == 4, q_==4)
        #             )
        # # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
        # def isFinal(p):
        #     return If(Or(p==1, p==2), 1, 0)

        # #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
        # def sigma(b1, b2, b3, b4, b5):
        #     p0 = And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)
        #     p1 = b1 > C
        #     p2 = And(b1 <= C, b2 > C)
        #     return [And(p0, Not(p1), Not(p2)), And(Not(p0), p1, Not(p2)), And(Not(p0), Not(p1), p2), And(Not(p0), Not(p1), Not(p2)) ]

        # # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # # Default: Returns the True formula in Z3
        # def guarantee(b1, b2, b3, b4, b5):
        #     return And(True)

        # # Call the fixpoint engine for omega regular specifications.
        # omega_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ)

    else:
        print("Not a valid input: Please enter \"safety\" or \"omega\" as the third argument")