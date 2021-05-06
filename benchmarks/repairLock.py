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

# 3. Define Guarantee
def guarantee(pc, l, gl):
    return Not(Or(And(pc==2, l == 1),And(pc == 5, l == 0)))

safety_fixedpoint(controller_moves, environment, guarantee)