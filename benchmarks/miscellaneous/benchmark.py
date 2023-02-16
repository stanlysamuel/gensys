from z3 import *
from  gensys.helper import *
from  gensys.fixpoints import *

x = Int('x')

#----------------------------------------------------------------------------------------------

# # BENCHMARK 1: SAFETY

# # 1. Define Automaton
# #Complete automaton from spot

# nQ = 2

# def automaton(q, q_, x):
#     return Or(
#             And(q == 0, q_==1, Or(x<0, x>2)),
#             And(q == 0, q_==0),
#             And(q == 1, q_==1),
#             )

# def isFinal(p):
#     return If(p==1, 1, 0)

# #2. Define Controller moves
# def controller(x, x_):
#     return Or(x_== x+1, x_== x-1)

# # 3. Define Environment moves.
# def environment(x, x_):
#         return x_== x

# sigma = [Not(And(x>=0, x<=2)), And(x>=0, x<=2)]

#----------------------------------------------------------------------------------------------

# # # BENCHMARK 2: 3 FLOOR

# # 1. Define Automaton
# # Complete automaton from spot
# nQ = 6
# def automaton(q, q_, x):
#     return Or(
#             And(q == 0, q_==0, And(x>=1, x<=3)),
#             And(q == 0, q_==1, Not(And(x>=1, x<=3))),
#             And(q == 1, q_==1),
#             And(q == 0, q_==2, And(x>=1, x<=3, x!=1)),
#             And(q == 2, q_==2, x!=1),
#             And(q == 2, q_==5, x==1),
#             And(q == 0, q_==3, And(x>=1, x<=3, x!=2)),
#             And(q == 3, q_==3, x!=2),
#             And(q == 3, q_==5, x==2),
#             And(q == 0, q_==4, And(x>=1, x<=3, x!=3)),
#             And(q == 4, q_==4, x!=3),
#             And(q == 4, q_==5, x==3),
#             And(q == 5, q_==5),
#             )

# def isFinal(p):
#     return If(And(p <=4, p >=1), 1, 0)

# #2. Define Controller moves
# def controller(x, x_):
#     return Or(x_== x+1, x_== x-1, x_==x)

# # 3. Define Environment moves.
# def environment(x, x_):
#         return x_== x

# sigma = [x == 1, x == 2, x == 3, Not(And(x>=1, x<=3))]

# #----------------------------------------------------------------------------------------------

# # BENCHMARK 3: 2 FLOOR

# # 1. Define Automaton
# # Complete automaton from spot
# nQ = 5
# def automaton(q, q_, x):
#     return Or(
#             And(q == 0, q_==0, And(x>=1, x<=2)),
#             And(q == 0, q_==1, Not(And(x>=1, x<=2))),
#             And(q == 1, q_==1),
#             And(q == 0, q_==2, And(x>=1, x<=2, x!=1)),
#             And(q == 2, q_==2, x!=1),
#             And(q == 2, q_==4, x==1),
#             And(q == 0, q_==3, And(x>=1, x<=2, x!=2)),
#             And(q == 3, q_==3, x!=2),
#             And(q == 3, q_==4, x==2),
#             And(q == 4, q_==4),
#             )

# def isFinal(p):
#     return If(And(p <=3, p >=1), 1, 0)

# #2. Define Controller moves

# def move1(x,x_):
#     return And(x_ == x-1)

# def move2(x,x_):
#     return And(x_ == x+1)

# controller_moves = [move1, move2]

# # 3. Define Environment moves.
# def environment(x, x_):
#         return x_== x

# def sigma(x):
#     return [x == 1, x == 2, Not(And(x>=1, x<=2))]

# #Optional explicit safety guarantee
# def guarantee(x):
#     return And(True)

#----------------------------------------------------------------------------------------------

# BENCHMARK 4: 1 FLOOR

# 4 and 1 showed that Succ is needed for correctness. not just succ.

# # 1. Define Automaton
# # Complete automaton from spot
# nQ = 2
# def automaton(q, q_, x):
#     return Or(
#             And(q == 0, q_==0, x == 1),
#             And(q == 0, q_==1, x!=1),
#             And(q == 1, q_==1)
#             )

# def isFinal(p):
#     return If(p==1, 1, 0)

# #2. Define Controller moves
# def controller(x, x_):
#     return Or(x_== x+1, x_== x-1, x_==x)

# # 3. Define Environment moves.
# def environment(x, x_):
#         return x_== x

# sigma = [x == 1, x != 1]

#-----------------------------------------------------------------------------------------

# #BENCHMARK 5: Cinderella

# # 1. Define Environment moves
# def environment(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
#     return And(b1_ + b2_ + b3_ + b4_ + b5_ == b1 + b2 + b3 + b4 + b5 + 1, b1_>=b1, b2_>=b2, b3_>=b3, b4_>=b4, b5_>=b5)

# #2. Define Controller moves

# def move1(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
#     return And( b1_ == 0.0,  b2_ == 0.0, b3_ == b3, b4_ == b4, b5_ == b5)

# def move2(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
#     return And( b2_ == 0.0,  b3_ == 0.0, b4_ == b4, b5_ == b5, b1_ == b1)

# def move3(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
#     return And( b3_ == 0.0,  b4_ == 0.0, b5_ == b5, b1_ == b1, b2_ == b2)

# def move4(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
#     return And( b4_ == 0.0,  b5_ == 0.0, b1_ == b1, b2_ == b2, b3_ == b3)

# def move5(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
#     return And( b5_ == 0.0,  b1_ == 0.0, b2_ == b2, b3_ == b3, b4_ == b4)

# controller_moves = [move1, move2, move3, move4, move5]





#-----------------------------------------------------------------------------------------




# BENCHMARK 1: SAFETY

# 1. Define Automaton
#Complete automaton from spot

nQ = 2

def automaton(q, q_, x):
    return Or(
            And(q == 0, q_==1, Or(x<0, x>2)),
            And(q == 0, q_==0),
            And(q == 1, q_==1),
            )

def isFinal(p):
    return If(p==1, 1, 0)

#2. Define Controller moves

def move1(x,x_):
    return And(x_ == x-1)

def move2(x,x_):
    return And(x_ == x+1)

controller_moves = [move1, move2]

# 3. Define Environment moves.
def environment(x, x_):
        return x_== x

def pred(x):
    return [Or(x<0, x>2)]

def sigma(x):
    return [Not(And(x>=0, x<=2)), And(x>=0, x<=2)]

#Optional explicit safety guarantee
def guarantee(x):
    return And(True)

omega_fixedpoint(controller_moves, environment, guarantee, 0, automaton, isFinal, sigma, nQ)

# Both optional guarantee and automaton give sound result.
# Add these to benchmarks with documentation for users.