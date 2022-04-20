from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

#Repair Lock example: Beyene et. al. POPL 2014

# 1. Define Environment moves
#Environment move is Skip here
def environment(pc, l, gl, pc_, l_, gl_):
    return And(pc_ == pc, l_ == l, gl_ == gl)

#2. Define Controller moves

def move1(pc, l, gl, pc_, l_, gl_):
    return And(pc == 0, pc_ == 2, l_ == l, gl_ == gl)

def move2(pc, l, gl, pc_, l_, gl_):
    return And(pc == 0, pc_ == 4, l_ == l, gl_ == gl)

def move3(pc, l, gl, pc_, l_, gl_):
    return And(pc == 2, pc_ == 4, l <= 0, l_ == l)

def move4(pc, l, gl, pc_, l_, gl_):
    return And(pc == 4, pc_ == 5, gl!=0, l_ == l, gl_ == gl)

def move5(pc, l, gl, pc_, l_, gl_):
    return And(pc == 4, pc_ == 6, gl==0, l_ == l, gl_ == gl)

def move6(pc, l, gl, pc_, l_, gl_):
    return And(pc == 5, pc_ == 6, l>=1, l_==0, gl_ == gl)

def move7(pc, l, gl, pc_, l_, gl_):
    return And(pc == 6, pc_ == 0, l_==l)

controller_moves = [move1, move2, move3, move4, move5, move6, move7]

mode = sys.argv[1]
spec = sys.argv[2]

if spec == "safety":

    # 3. Define Guarantee
    def guarantee(pc, l, gl):
        return Not(Or(And(pc==2, l == 1),And(pc == 5, l == 0)))

    safety_fixedpoint(controller_moves, environment, guarantee, int(mode))

else:
    if spec == "omega":

        # Spec: Safety, G(formula) where formula = Not(Or(And(pc==2, l == 1),And(pc == 5, l == 0)))
        # Complete Universal Co-Buchi Automaton from spot encoded in LRA.
        # Automaton information such as automaton, isFinal and nQ can be retreived from spot tool manually.

        nQ = 2
        def automaton(q, q_, pc, l, gl):
            return Or(
                    And(q == 0, q_==1, Not(Not(Or(And(pc==2, l == 1),And(pc == 5, l == 0))))),
                    And(q == 0, q_==0),
                    And(q == 1, q_==1),
                    )
        # Denotes which states in the UCW are final states i.e, those states that should be visited finitely often for every run
        def isFinal(p):
            return If(p==1, 1, 0)

        #Partition of predicates obtained by finding all combinations of predicates present in the automaton (manual).
        def sigma(pc, l, gl):
            return [Not(Not(Or(And(pc==2, l == 1),And(pc == 5, l == 0)))), Not(Or(And(pc==2, l == 1),And(pc == 5, l == 0)))]

        # (Optional): Explicit safety guarantee that complements the omega-regular formula
        # Default: Returns the True formula in Z3
        def guarantee(pc, l, gl):
            return And(True)

        # Call the fixpoint engine for omega regular specifications.
        omega_fixedpoint(controller_moves, environment, guarantee, int(mode), automaton, isFinal, sigma, nQ)

    else:
        print("Not a valid input: Please enter \"safety\" or \"omega\" as the third argument")