from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *
# import faulthandler

# faulthandler.enable()
# 0. Define game type (Int/ Real/ Bool)
game_type = "Bool"

# 1. Define Environment moves
def environment(req, gra, req_, gra_):
    return And(req_ == req, gra_ == gra)

#2. Define Controller moves

def move(req, gra, req_, gra_):
    return And(req_ == req, gra_ == gra)

controller_moves = [move]

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "safety":

    # 3. Define Guarantee
    def guarantee(r, g):
        return True

    safety_fixedpoint(controller_moves, environment, guarantee, int(mode))

else:
    if spec == "omega":

        # Spec: G(r -> F g), where environment controls r and controller controls g.
        # Complete Universal Co-Buchi Automaton from spot encoded in LRA.
        # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 3
        def automaton(q, q_, req, gra):
            return Or(
                    And(q == 0, q_==0),
                    And(q == 0, q_==1, req),
                    And(q == 1, q_==1, Not(gra)),
                    And(q == 1, q_==2, gra),
                    And(q == 2, q_==2),
    
                    )
        # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
        def isFinal(p):
            return If(p == 1, 1, 0)

        #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
        def sigma(req, gra):
            return [And(req, gra), And(req, Not(gra)), And(Not(req), gra), And(Not(req), Not(gra))]
            # return [And(x>=1, x<=2), Not(And(x>=1, x<=2))] # This is expensive to project for some reason
            # return [Or(x == 1, x == 2), Not(And(x>=1, x<=2))]

        # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # Default: Returns the True formula in Z3
        def guarantee(req, gra):
            return And(True)

        # Call the fixpoint engine for omega regular specifications.
        otfd_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ,0, game_type)
        antichain_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ, 0, game_type)

    else:
        print("Not a valid input: Please enter \"safety\" or \"omega\" as the third argument")