from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Repair Critical example: Beyene et. al. POPL 2014, taken from Figure 5, Program Repair as a game paper.
# Spec: Safety, G(formula) where formula == And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7)))

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
#Environment move is Skip here
def environment(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
    return And(f1a == f1a_, f1b_ == f1b, t1b == t1b_, f2a == f2a_, f2b == f2b_, t2b == t2b_, pc1 == pc1_, pc2 == pc2_)

# 2. Define Controller moves

# thread A
def move1(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
    return  Or( And(pc1==1, f1a_==1,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==2,pc2_==pc2),
                And(pc1 == 2, f1a_==f1a,f1b_==f1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==3,pc2_==pc2),
                And(pc1 == 3, f1b==1,t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==3,pc2_==pc2),
                And(pc1 == 3, Or(f1b==0, t1b==0),f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==4,pc2_==pc2),
                And(pc1 == 4, f1a_==0,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==5,pc2_==pc2),
                And(pc1 == 5, t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==1,  f2b_==f2b,t2b_==t2b,pc1_==6,pc2_==pc2),
                And(pc1 == 5, t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==9,pc2_==pc2),
                And(pc1 == 6, t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,  f2b_==f2b,t2b_==1,  pc1_==7,pc2_==pc2),
                And(pc1 == 7, f2b==1,t2b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==8,pc2_==pc2),
                And(pc1 == 8, f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==0,  f2b_==f2b,t2b_==t2b,pc1_==9,pc2_==pc2),
                And(pc1 == 9, f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==1,pc2_==pc2),
                # And(Or(pc1<1, pc1>9), f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==pc2)
                 )

# thread B
def move2(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
    return Or(  And(f1a == 1, f1a_ == 0, f1b_ == f1b, t1b == t1b_, f2a == f2a_, f2b == f2b_, t2b == t2b_, pc1 == pc1_, pc2 == pc2_),
                And(pc2==1,f1a_==f1a,f1b_==1,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==2),
                And(pc2==2,f1a_==f1a,f1b_==f1b,t1b_==0,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==3),
                And(pc2==3,f1a==1,t1b==0,  f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==3),
                And(pc2==3,Or(f1a==0,t1b==1),f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==4),
                And(pc2==4,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==1,t2b_==t2b,pc1_==pc1,pc2_==5),
                And(pc2==5,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==0,pc1_==pc1,pc2_==6),
                And(pc2==6,f2a==1,t2b==0,  f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==6),
                And(pc2==6,Or(f2a==0,t2b==1),f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==7),
                And(pc2==7,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==0,t2b_==t2b,pc1_==pc1,pc2_==8),
                And(pc2==8,f1a_==f1a,f1b_==0,t1b_==t1b,f2a_==f2a,f2b_==f1b,t2b_==t2b,pc1_==pc1,pc2_==9),
                And(pc2==9,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==1),
                # And(Or(pc2<1, pc2>9), f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==pc2)
                )

controller_moves = [move1, move2]

# # thread A
# def move1(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1==1, f1a_==1,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==2,pc2_==pc2)

# def move2(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1 == 2, f1a_==f1a,f1b_==f1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==3,pc2_==pc2)

# def move3(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1 == 3, f1b==1,t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==3,pc2_==pc2)

# def move4(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1 == 3, Or(f1b==0, t1b==0),f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==4,pc2_==pc2)

# def move5(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1 == 4, f1a_==0,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==5,pc2_==pc2)

# def move6(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1 == 5, t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==1,  f2b_==f2b,t2b_==t2b,pc1_==6,pc2_==pc2)

# def move7(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1 == 5, t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==9,pc2_==pc2)

# def move8(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1 == 6, t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,  f2b_==f2b,t2b_==1,  pc1_==7,pc2_==pc2)

# def move9(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1 == 7, f2b==1,t2b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==8,pc2_==pc2)

# def move10(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1 == 8, f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==0,  f2b_==f2b,t2b_==t2b,pc1_==9,pc2_==pc2)

# def move11(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc1 == 9, f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==1,pc2_==pc2)

# # And(Or(pc1<1, pc1>9), f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==pc2)

# # thread B
# def move12(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(f1a == 1, f1a_ == 0, f1b_ == f1b, t1b == t1b_, f2a == f2a_, f2b == f2b_, t2b == t2b_, pc1 == pc1_, pc2 == pc2_)

# def move13(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==1,f1a_==f1a,f1b_==1,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==2)

# def move14(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==2,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==3)

# def move15(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==3,f1a==1,t1b==0,  f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==3)

# def move16(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==3,Or(f1a==0,t1b==1),f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==4)

# def move17(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==4,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==1,t2b_==t2b,pc1_==pc1,pc2_==5)

# def move18(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==5,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==0,pc1_==pc1,pc2_==6)

# def move19(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==6,f2a==1,t2b==0,  f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==6)

# def move20(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==6,Or(f2a==0,t2b==1),f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==7)

# def move21(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==7,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==0,t2b_==t2b,pc1_==pc1,pc2_==8)

# def move22(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==8,f1a_==f1a,f1b_==0,t1b_==t1b,f2a_==f2a,f2b_==f1b,t2b_==t2b,pc1_==pc1,pc2_==9)

# def move23(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2, f1a_, f1b_, t1b_, f2a_, f2b_, t2b_, pc1_, pc2_):
#     return And(pc2==9,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==1)
# # And(Or(pc2<1, pc2>9), f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==pc2)

# controller_moves = [move1, move2, move3, move4, move5, move6, move7, move8, move9, move10, move11, move12, move13, move14, move15, move16, move17, move18, move19, move20, move21, move22, move23]

#3. Define Init Region (False by default => Maximal winning region will be returned)

def init(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
    return And(pc1==1,pc2==1, f1a==0, f1b==0, t1b==0, f2a==0, f2b==0, t2b==0)

# def init(pc, l, gl):
#     return False

spec_type = sys.argv[1]

if spec_type == "simple":

    # 3. Define Guarantee
    def guarantee(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
        return And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7)))

    safety_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)

else:
    # If automaton is deterministic, same automaton is enough for both buchi and cobuchi product fixpoints. 
    # If final states are X, just run GF(X) and FG(X) on them to get results for buchi and cobuchi respectively.

    if spec_type == "product-buchi":

        # Complete Deterministic Buchi Automaton for the above specification
        # Functions such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
            return Or(
                    And(q == 0, q_==1, Not(And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7))))),
                    And(q == 0, q_==0, And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7)))),
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
            def automaton(q, q_, f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
                return Or(
                        And(q == 0, q_==1, Not(And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7))))),
                        And(q == 0, q_==0, And(Not(And(pc1 == 4, pc2 == 4)), Not(And(pc1 == 8, pc2==7)))),
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

                # This is dummy and not used in the product fixpoint engine; will be removed in future versions.
                def guarantee(f1a, f1b, t1b, f2a, f2b, t2b, pc1, pc2):
                    return And(True)

                # Call the fixpoint engine for omega regular specifications (k = 0).
                # otfd_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)
                otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ, 0, game_type, init)

            else:
                print("Not a valid input: Please enter \"simple\", \"product-buchi\", \"product-co-buchi\", or \"bounded\" as the third argument")