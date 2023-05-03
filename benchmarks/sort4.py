from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# 4 variable Sorting Example taken from the paper "Reactive Synthesis Modulo Theories using Abstraction Refinement"

# 0. Define game type (Int/ Real)
game_type = "Int"

# 1. Define Environment moves
#Environment move is Skip here
def environment(a, b, c, d, a_, b_, c_, d_):
    return And(a_ == a, b_ == b, c_ == c, d_ == d)

#2. Define Controller moves

# flip(a,b)
def move1(a, b, c, d, a_, b_, c_, d_):
    return And(a_ == b, b_ == a, c_ == c, d_ == d)

# flip(b,c)
def move2(a, b, c, d, a_, b_, c_, d_):
    return And(a_ == a, b_ == c, c_ == b, d_ == d)

# flip(c,d)
def move3(a, b, c, d, a_, b_, c_, d_):
    return And(a_ == a, b_ == b, c_ == d, d_ == c)

# skip
def move4(a, b, c, d, a_, b_, c_, d_):
    return And(a_ == a, b_ == b, c_ == c, d_ == d)

controller_moves = [move1, move2, move3, move4]

# 4. Define Initial States
def init(a, b, c, d):
    return False

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "simple":

    # 3. Define Guarantee
    def guarantee(a, b, c, d):
        return And(a>=b, b>=c, c>=d)

    # Spec: FG (a>=b, b>=c, c>=d)
    cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, 0, game_type, init)

else:
    if spec == "product":

        # Spec: FG(formula) where formula == And(a>=b, b>=c, c>=d)
        # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, a, b, c, d):
            return Or(
                    And(q == 0, q_==1, And(a>=b, b>=c, c>=d)),
                    And(q == 0, q_==0, Not(And(a>=b, b>=c, c>=d))),
                    And(q == 1, q_==1, And(a>=b, b>=c, c>=d)),
                    And(q == 1, q_==0, Not(And(a>=b, b>=c, c>=d)))
                    )
        
        def isFinal(p):
            return p == 0

        # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # Default: Returns the True formula in Z3
        def guarantee(q):
            return And(True)

        # Call the fixpoint engine for omega regular specifications.
        buchi_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, nQ, game_type, init)

    else:
        if spec == "bounded":
            # Only UCW's used in this section (i.e., from the negation of the specification)
            # Spec: FG(formula) where formula == And(a>=b, b>=c, c>=d)
            # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

            nQ = 2
            def automaton(q, q_, a, b, c, d):
                return Or(
                        And(q == 0, q_==1, And(a>=b, b>=c, c>=d)),
                        And(q == 0, q_==0, Not(And(a>=b, b>=c, c>=d))),
                        And(q == 1, q_==1, And(a>=b, b>=c, c>=d)),
                        And(q == 1, q_==0, Not(And(a>=b, b>=c, c>=d)))
                        )

            # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
            def isFinal(p):
                return If(p==1, 1, 0)

            #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
            def sigma(a, b, c, d):
                return [And(a>=b, b>=c, c>=d), Not(And(a>=b, b>=c, c>=d))]

            # (Optional): Explicit safety guarantee that complements the omega-regular formula
            # Default: Returns the True formula in Z3
            def guarantee(a, b, c, d):
                return And(True)

            # Call the fixpoint engine for omega regular specifications.
            otfd_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)
            # otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)

            # antichain_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)
            # antichain_fixedpoint_nonsigma(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type, init)

        else:
            print("Not a valid input: Please enter \"simple\" \"product\" or \"bounded\" as the third argument")