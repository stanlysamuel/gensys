# GenSys v0.1: Synthesis of Maximal Controllers for Safety Specifications
# Copyright (C) 2021  Stanly Samuel

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>

from  gensys.helper import *
from z3 import *

#The encoding where environment plays first i.e. ForAll-Exists.
#-------------------------------------------------------------------#
#Initialize the three tactics required for the tool. Assume user cannot controler them now
#-------------------------------------------------------------------#
# Tactics for fixedpoint algorithm
# tactic_qe_fixpoint = Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe2'), Tactic('simplify'))
tactic_qe_fixpoint = Tactic('qe2')

#Controller Extraction: Use same tactic as fixpoint and use ctx-solver-simplify to make the controller readable.
tactic_qe_controller = tactic_qe_fixpoint
tactic_simplification = Repeat('ctx-solver-simplify')
# tactic_simplification = Repeat('simplify')

#-------------------------------------------------------------------#

#Options for printing in Z3
set_option(max_depth=100000, rational_to_decimal = True, precision =40, max_lines=10000)

#Cinderella-Stepmother game of 5 buckets with bucket size of C.

# 1. Define Environment assumption and moves
def assumption(i1, i2, i3, i4, i5):
    return And( i1 + i2 + i3 + i4 + i5 <=1.0, i1 >= 0.0, i2 >= 0.0, i3 >= 0.0, i4 >= 0.0, i5 >= 0.0)

#2. Define Controller moves
def move1(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5):
    return And(t1 == b1 + i1,  t2 == b2 + i2, t3 == b3 + i3, t4 == b4 + i4, t5 == b5 + i5, b1_ == 0,  b2_ == 0, b3_ == t3, b4_ == t4, b5_ == t5)
    
def move2(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5):
    return And(t1 == b1 + i1,  t2 == b2 + i2, t3 == b3 + i3, t4 == b4 + i4, t5 == b5 + i5, b2_ == 0,  b3_ == 0, b4_ == t4, b5_ == t5, b1_ == t1)

def move3(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5):
    return And(t1 == b1 + i1,  t2 == b2 + i2, t3 == b3 + i3, t4 == b4 + i4, t5 == b5 + i5, b3_ == 0,  b4_ == 0, b5_ == t5, b1_ == t1, b2_ == t2)

def move4(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5):
    return And(t1 == b1 + i1,  t2 == b2 + i2, t3 == b3 + i3, t4 == b4 + i4, t5 == b5 + i5, b4_ == 0,  b5_ == 0, b1_ == t1, b2_ == t2, b3_ == t3)

def move5(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5):
    return And(t1 == b1 + i1,  t2 == b2 + i2, t3 == b3 + i3, t4 == b4 + i4, t5 == b5 + i5, b5_ == 0,  b1_ == 0, b2_ == t2, b3_ == t3, b4_ == t4)

# 3. Define Guarantee
def guarantee(b1, b2, b3, b4, b5, C):
    return And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)

# 4. Define One Step ForAll-Exists transition
def transition(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5):
    return Or(move1(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5), move2(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5), move3(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5), move4(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5), move5(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5))

#Function to print z3py formula in SMTLIB2 format
def toSMT2Benchmark(f, status="unknown", name="benchmark", logic=""):
  v = (Ast * 0)()
  return Z3_benchmark_to_smtlib_string(f.ctx_ref(), name, logic, status, "", 0, v, f.as_ast())

b1 = Real('b1')
b2 = Real('b2')
b3 = Real('b3')
b4 = Real('b4')
b5 = Real('b5')
i1 = Real('i1')
i2 = Real('i2')
i3 = Real('i3')
i4 = Real('i4')
i5 = Real('i5')
b1_ = Real('b1_')
b2_ = Real('b2_')
b3_ = Real('b3_')
b4_ = Real('b4_')
b5_ = Real('b5_')
t1 = Real('t1')
t2 = Real('t2')
t3 = Real('t3')
t4 = Real('t4')
t5 = Real('t5')
C = sys.argv[1]

#Forall-Exists valuation as AE-VAL
ExistsFormula = Exists([b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5], And(transition(b1, b2, b3, b4, b5, i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5), guarantee(t1, t2, t3, t4, t5, C), guarantee(b1_, b2_, b3_, b4_, b5_, C)))

#Simplify Exists first before projecting.
g =Goal()
g.add(ExistsFormula)
ExistsFormula = tactic_qe_fixpoint(g).as_expr()
# print ExistsFormula

wpAssertion = ForAll([i1, i2, i3, i4, i5],Implies(assumption(i1, i2, i3, i4, i5), ExistsFormula ))

g =Goal()
g.add(wpAssertion)
wp = tactic_qe_fixpoint(g).as_expr()
# print "WP"
# print wp

W = And(wp, guarantee(b1, b2, b3, b4, b5, C))
W = tactic_qe_fixpoint(W).as_expr()
F = guarantee(b1, b2, b3, b4, b5, C)
i = 0
print("Iteration", i )
while(not valid(Implies(F, W),0)):
# while(not valid(F == W)): gives same as above so => holds one way
    #Backup for F
    temp = W
    #Substitute current variables with post variables
    W = substitute(W, (b1, b1_), (b2, b2_), (b3, b3_), (b4, b4_), (b5, b5_))

#     #Macros become useless here as substitute W directly here. See some form of dynamic function assignment and then calling like guarantee() = return W. Update in this line. else unnecessary formula repetition

    ExistsFormula = Exists([b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5], And(transition(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5),guarantee(t1, t2, t3, t4, t5, C), W))
    #Simplify Exists first before projecting.
    g =Goal()
    g.add(ExistsFormula)
    ExistsFormula = tactic_qe_fixpoint(g).as_expr()
    # print ExistsFormula

    wpAssertion = ForAll([i1, i2, i3, i4, i5],Implies(assumption(i1, i2, i3, i4, i5), ExistsFormula ))

    g = Goal()
    g.add(wpAssertion)
    wp = tactic_qe_fixpoint(g).as_expr()
    W = And(wp, guarantee(b1, b2, b3, b4, b5, C))
    # print W
    F = temp
    i=i+1
    print("Iteration ", i )

print("")
print("Number of times WP computed: ", i+1)
print("")

if not satisfiable(F,0):
    print "Invariant is Unsatisifiable i.e. False"
    print "UNREALIZABLE"
else:
    print "Invariant is Satisfiable"
    print "REALIZABLE"
    print "EXTRACTING CONTROLLER..."
    #Controller extraction
    # In the invariant, substitute with post varaibles
    #Take backup of invariant to analyse in the end
    Invariant = F
    F = substitute(F, (b1, b1_), (b2, b2_), (b3, b3_), (b4, b4_), (b5, b5_))

    # ExistsFormula move 1:
    ExistsFormula = Exists([b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5], And(move1(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5),guarantee(t1, t2, t3, t4, t5, C), F))
    #Simplify Exists first before projecting.
    g =Goal()
    g.add(ExistsFormula)
    ExistsFormula = tactic_qe_fixpoint(g).as_expr()

    condition_move1 = ForAll([i1, i2, i3, i4, i5],Implies(assumption(i1, i2, i3, i4, i5), ExistsFormula ))

    # ExistsFormula move 2:
    ExistsFormula = Exists([b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5], And(move2(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5),guarantee(t1, t2, t3, t4, t5, C), F))
    #Simplify Exists first before projecting.
    g =Goal()
    g.add(ExistsFormula)
    ExistsFormula = tactic_qe_fixpoint(g).as_expr()

    condition_move2 = ForAll([i1, i2, i3, i4, i5],Implies(assumption(i1, i2, i3, i4, i5), ExistsFormula ))

    # ExistsFormula move 3:
    ExistsFormula = Exists([b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5], And(move3(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5),guarantee(t1, t2, t3, t4, t5, C), F))
    #Simplify Exists first before projecting.
    g =Goal()
    g.add(ExistsFormula)
    ExistsFormula = tactic_qe_fixpoint(g).as_expr()

    condition_move3 = ForAll([i1, i2, i3, i4, i5],Implies(assumption(i1, i2, i3, i4, i5), ExistsFormula ))

    # ExistsFormula move 4:
    ExistsFormula = Exists([b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5], And(move4(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5),guarantee(t1, t2, t3, t4, t5, C), F))
    #Simplify Exists first before projecting.
    g =Goal()
    g.add(ExistsFormula)
    ExistsFormula = tactic_qe_fixpoint(g).as_expr()

    condition_move4 = ForAll([i1, i2, i3, i4, i5],Implies(assumption(i1, i2, i3, i4, i5), ExistsFormula ))

    # ExistsFormula move 5:
    ExistsFormula = Exists([b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5], And(move5(b1, b2, b3, b4, b5,i1, i2, i3, i4, i5, b1_, b2_, b3_, b4_, b5_, t1, t2, t3, t4, t5),guarantee(t1, t2, t3, t4, t5, C), F))
    #Simplify Exists first before projecting.
    g =Goal()
    g.add(ExistsFormula)
    ExistsFormula = tactic_qe_fixpoint(g).as_expr()

    condition_move5 = ForAll([i1, i2, i3, i4, i5],Implies(assumption(i1, i2, i3, i4, i5), ExistsFormula ))

    #Move 1 condition extraction
    #Eliminate quantifiers and simplify to get the conditions for each move
    g = Goal()
    g.add(condition_move1)
    #Eliminate qe and conjunct with guarantee and assumption
    condition_move1 = And(tactic_qe_controller(g).as_expr(), guarantee(b1, b2, b3, b4, b5, C))
    g = Goal()
    g.add(condition_move1)
    #Simplify to get final condition
    condition_move1 = tactic_simplification(g).as_expr()

    #Move 2 condition extraction
    #Eliminate quantifiers and simplify to get the conditions for each move
    g = Goal()
    g.add(condition_move2)
    #Eliminate qe and conjunct with guarantee and assumption
    condition_move2 = And(tactic_qe_controller(g).as_expr(), guarantee(b1, b2, b3, b4, b5, C))
    g = Goal()
    g.add(condition_move2)
    #Simplify to get final condition
    condition_move2 = tactic_simplification(g).as_expr()

    #Move 3 condition extraction
    #Eliminate quantifiers and simplify to get the conditions for each move
    g = Goal()
    g.add(condition_move3)
    #Eliminate qe and conjunct with guarantee and assumption
    condition_move3 = And(tactic_qe_controller(g).as_expr(), guarantee(b1, b2, b3, b4, b5, C))
    g = Goal()
    g.add(condition_move3)
    #Simplify to get final condition
    condition_move3 = tactic_simplification(g).as_expr()

    #Move 4 condition extraction
    #Eliminate quantifiers and simplify to get the conditions for each move
    g = Goal()
    g.add(condition_move4)
    #Eliminate qe and conjunct with guarantee and assumption
    condition_move4 = And(tactic_qe_controller(g).as_expr(), guarantee(b1, b2, b3, b4, b5, C))
    g = Goal()
    g.add(condition_move4)
    #Simplify to get final condition
    condition_move4 = tactic_simplification(g).as_expr()

    #Move 5 condition extraction
    #Eliminate quantifiers and simplify to get the conditions for each move
    g = Goal()
    g.add(condition_move5)
    #Eliminate qe and conjunct with guarantee and assumption
    condition_move5 = And(tactic_qe_controller(g).as_expr(), guarantee(b1, b2, b3, b4, b5, C))
    g = Goal()
    g.add(condition_move5)
    #Simplify to get final condition
    condition_move5 = tactic_simplification(g).as_expr()

    print "MOVE 1 CONDITION:"
    print condition_move1
    print ""
    print "MOVE 2 CONDITION:"
    print condition_move2
    print ""
    print "MOVE 3 CONDITION:"
    print condition_move3
    print ""
    print "MOVE 4 CONDITION:"
    print condition_move4
    print ""
    print "MOVE 5 CONDITION:"
    print condition_move5
    print ""

    #Sanity check: Disjunction of controller conditions is equal to Invariant
    formula = Or(condition_move1, condition_move2, condition_move3, condition_move4, condition_move5) == Invariant
    # formula = condition_move1 == Invariant
    # formula = Implies(condition_move1, Invariant)
    # formula = Implies(Invariant, condition_move1)
    valid(formula,0)