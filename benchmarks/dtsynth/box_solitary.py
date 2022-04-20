from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Solitary Box example: Neider et. al., TACAS 2016 and DTSynth Tool, FMCAD 2019
# Another variation of the Box game in
# which only Player 0 is in control of the robot

# 1. Define Environment moves
#Environment move is Skip here
def environment(x,y,x_,y_):
    return And(x_ == x, y_==y)

# 2. Define Controller moves

def move1(x,y,x_,y_):
    return And(x_ == x, y_ == y)

def move2(x,y,x_,y_):
    return And(x_ == x+1, y_ == y)

def move3(x,y,x_,y_):
    return And(x_ == x-1, y_ == y)

def move4(x,y,x_,y_):
    return And(x_ == x, y_ == y + 1)

def move5(x,y,x_,y_):
    return And(x_ == x+1, y_ == y + 1)

def move6(x,y,x_,y_):
    return And(x_ == x-1, y_ == y + 1)

def move7(x,y,x_,y_):
    return And(x_ == x, y_ == y - 1)

def move8(x,y,x_,y_):
    return And(x_ == x+1, y_ == y - 1)

def move9(x,y,x_,y_):
    return And(x_ == x-1, y_ == y - 1)

controller_moves = [move1, move2, move3, move4, move5, move6, move7, move8, move9]

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "safety":

    # 3. Define Guarantee
    def guarantee(x, y):
        return And(x<=3, x>=0)

    safety_fixedpoint(controller_moves, environment, guarantee, int(mode))

else:
    if spec == "omega":

        # Spec: Safety, G(formula) where formula = And(x<=3, x>=0)
        # Complete Universal Co-Buchi Automaton from spot encoded in LRA.
        # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, x, y):
            return Or(
                    And(q == 0, q_==1, Not(And(x<=3, x>=0))),
                    And(q == 0, q_==0),
                    And(q == 1, q_==1),
                    )
        # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
        def isFinal(p):
            return If(p==1, 1, 0)

        #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
        def sigma(x, y):
            return [Not(And(x<=3, x>=0)), And(x<=3, x>=0)]

        # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # Default: Returns the True formula in Z3
        def guarantee(x, y):
            return And(True)

        # Call the fixpoint engine for omega regular specifications.
        omega_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ)

    else:
        print("Not a valid input: Please enter \"safety\" or \"omega\" as the third argument")