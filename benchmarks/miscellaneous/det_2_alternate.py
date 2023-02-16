from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Non turn based, deterministic safety automaton k=0 for G(x==1 => X x!=1)

# Note: No need to add the transitons for the unsafe states. Let them be sink nodes without outgoing transitions.

# 1. Define Environment moves.

#Envrionment move not considering the automaton product
# def environment(state,x, state_, x_):
#     return And(state_ == state, x_==x)

#Environment moves as Disjunction of Conjunctions
# def environment(state,x, state_, x_):

#Environment moves as Disjunction of Conjunctions: Simplified.
def environment(state,x, state_, x_):
    return  And(
        Or(
            And(state == 1, state_==2, x==1),
            And(state == 1, state_==1, x!=1),
            And(state == 2, state_==3, x==1),
            And(state == 2, state_==1, x!=1),
            ),
        # state_==state,
        x_== x
    )

#Environment moves as Conjunction of Implications
# def environment(state,x, state_, x_):
#     return  And(
#         Implies(And(state == 1, x>=0, x<=10), state_==1, x_==x),  
#         Implies(And(state == 1, Or(x<0, x>10)), state_==2, x_==x),
#         Implies(And(state == 2, state_==2), x_==x))

#2. Define Controller moves

def move1(state, x, state_, x_):
    return And(state == 1, state_==1, x!=1, x_ == x + 1)
def move2(state, x, state_, x_):
    return And(state == 1, state_==2, x==1, x_ == x + 1)
def move3(state, x, state_, x_):
    return And(state == 2, state_==1, x!=1, x_ == x + 1)
def move4(state, x, state_, x_):
    return And(state == 2, state_==3, x==1, x_ == x + 1)
def move5(state, x, state_, x_):
    return And(state == 1, state_==1, x!=1, x_ == x - 1)
def move6(state, x, state_, x_):
    return And(state == 1, state_==2, x==1, x_ == x - 1)
def move7(state, x, state_, x_):
    return And(state == 2, state_==1, x!=1, x_ == x - 1)
def move8(state, x, state_, x_):
    return And(state == 2, state_==3, x==1, x_ == x - 1)


controller_moves = [move1, move2, move3, move4, move5, move6, move7, move8]

mode = sys.argv[1]

# 3. Define Guarantee
def guarantee(state, x):
    return And(state!=3)

safety_fixedpoint(controller_moves, environment, guarantee, int(mode))