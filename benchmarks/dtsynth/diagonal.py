from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Diagonal example: Neider et. al., TACAS 2016 and DTSynth Tool, FMCAD 2019
# A robot moves in an infinite, discrete twodimensional grid world. Player 0 controls the robot's
# vertical movement, while Player 1 controls the horizontal.
# Player 0 wins if the robot stays within two cell around
# the diagonal

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

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "safety":

    # 3. Define Guarantee
    def guarantee(x, y):
        return And(y >= x - 2, y <= x + 2)

    safety_fixedpoint(controller_moves, environment, guarantee, int(mode))

else:
    if spec == "omega":

        # Spec: Safety, G(formula) where formula = And(y >= x - 2, y <= x + 2)
        # Complete Universal Co-Buchi Automaton from spot encoded in LRA.
        # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, x, y):
            return Or(
                    And(q == 0, q_==1, Not(And(y >= x - 2, y <= x + 2))),
                    And(q == 0, q_==0),
                    And(q == 1, q_==1),
                    )
        # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
        def isFinal(p):
            return If(p==1, 1, 0)

        #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
        def sigma(x, y):
            return [Not(And(y >= x - 2, y <= x + 2)), And(y >= x - 2, y <= x + 2)]

        # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # Default: Returns the True formula in Z3
        def guarantee(x, y):
            return And(True)

        # Call the fixpoint engine for omega regular specifications.
        omega_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ)

    else:
        print("Not a valid input: Please enter \"safety\" or \"omega\" as the third argument")