from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Non deterministic based approach for G(x==1 => X x!=1)

# 1. Define Environment moves.

#Environment moves as Disjunction of Conjunctions: Simplified.
def environment(state,x,c, state_, x_,c_):
    return  And(
        Or(
            And(state == 1, state_==2, x==1),
            And(state == 1, state_==1),
            And(state == 2, state_==3, x==1),
            And(state == 3, state_==3),
            And(state == 2, state_==4, x!=1),
            And(state == 4, state_==4),
            ),
        x_== x,
        counter_constraints(state_, c, c_)
    )

#2. Define Controller moves

def move1(state, x, c, state_, x_, c_):
    return And(state == 1, state_==2, x==1, x_ == x + 1, counter_constraints(state_, c, c_))
def move2(state, x, c, state_, x_, c_):
    return And(state == 1, state_==1, x_ == x + 1, counter_constraints(state_, c, c_))
def move3(state, x, c, state_, x_, c_):
    return And(state == 2, state_==3, x==1, x_ == x + 1, counter_constraints(state_, c, c_))
def move4(state, x, c, state_, x_, c_):
    return And(state == 3, state_==3, x_ == x + 1, counter_constraints(state_, c, c_))
def move5(state, x, c, state_, x_, c_):
    return And(state == 1, state_==2, x==1, x_ == x - 1, counter_constraints(state_, c, c_))
def move6(state, x, c, state_, x_, c_):
    return And(state == 1, state_==1, x_ == x - 1, counter_constraints(state_, c, c_))
def move7(state, x, c, state_, x_, c_):
    return And(state == 2, state_==3, x==1, x_ == x - 1, counter_constraints(state_, c, c_))
def move8(state, x, c, state_, x_, c_):
    return And(state == 3, state_==3, x_ == x - 1, counter_constraints(state_, c, c_))
def move9(state, x, c, state_, x_, c_):
    return And(state == 2, state_==4, x!=1, x_ == x - 1, counter_constraints(state_, c, c_))
def move10(state, x, c, state_, x_, c_):
    return And(state == 2, state_==4, x!=1, x_ == x + 1, counter_constraints(state_, c, c_))
def move11(state, x, c, state_, x_, c_):
    return And(state == 4, state_==4, x_ == x - 1, counter_constraints(state_, c, c_))
def move12(state, x, c, state_, x_, c_):
    return And(state == 4, state_==4, x_ == x + 1, counter_constraints(state_, c, c_))

controller_moves = [move1, move2, move3, move4, move5, move6, move7, move8, move9, move10, move11, move12]

mode = sys.argv[1]

# 3. Define Guarantee
def guarantee(state, x, c):
    return c == 0

# 4. Define counter constraints
def counter_constraints(state_, c, c_):
    return  And(
            Implies(And(state_==3, c_ == -1), c == c_),
            Implies(And(state_==3, c_ >= 0), c == c_ - 1),
            Implies(state_!=3, c == c_)
    )

safety_fixedpoint(controller_moves, environment, guarantee, int(mode))