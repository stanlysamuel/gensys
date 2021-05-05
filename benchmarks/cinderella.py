from  gensys.helper import *
from z3 import *

# This version is without the i variables. So quantification is over the b1__ variables. For some reason qe2 is stuck and only the other tactic works. Maybe this is because of Exists and not the i part. YES! it is because of EA. AA may gives better result in qe2. See why later.
#OBSERVATION: qe2 performs extremely well for realizability using AA
#-------------------------------------------------------------------#
#Initialize the three tactics required for the tool
#-------------------------------------------------------------------#
#Fixpoint
# tactic_qe_fixpoint= Then(Then(Then(Then(Tactic('qe_rec'), Tactic('qe2')), Tactic('qe')), Tactic('simplify')), Repeat('ctx-solver-simplify')) #Best tactic combination so far that works for simplification for 1.9999999
# tactic_qe_fixpoint= Then(Then(Then(Tactic('qe_rec'), Tactic('qe2')), Tactic('qe')), Tactic('simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe2'), Tactic('simplify'))
tactic_qe_fixpoint = Tactic('qe2') #C=2.0 and C=3.0 this works faster

#Controller Extraction: Use same tactic as fixpoint and use ctx-solver-simplify to make the controller readable.
tactic_qe_controller = tactic_qe_fixpoint
tactic_simplification = Repeat('ctx-solver-simplify')
# tactic_simplification = Repeat('simplify') #Slightly larger but fine

#-------------------------------------------------------------------#

set_option(max_depth=100000, rational_to_decimal = True, precision =40, max_lines=10000)

# define-fun in SMT-LIB2 essentially creates a macro. Macros are not supported in z3py. 

# Environment moves
def environment(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And(b1_ + b2_ + b3_ + b4_ + b5_ == b1 + b2 + b3 + b4 + b5 + 1, b1_>=b1, b2_>=b2, b3_>=b3, b4_>=b4, b5_>=b5)

# Guarantee
def guarantee(b1, b2, b3, b4, b5, C):
    return And(b1 <= C , b2 <=C , b3 <=C , b4 <=C , b5 <=C , b1 >= 0.0 , b2 >= 0.0 , b3 >= 0.0 , b4 >= 0.0 , b5 >= 0.0)

#Controller moves

def move1(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b1_ == 0.0,  b2_ == 0.0, b3_ == b3, b4_ == b4, b5_ == b5)

def move2(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b2_ == 0.0,  b3_ == 0.0, b4_ == b4, b5_ == b5, b1_ == b1)

def move3(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b3_ == 0.0,  b4_ == 0.0, b5_ == b5, b1_ == b1, b2_ == b2)

def move4(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b4_ == 0.0,  b5_ == 0.0, b1_ == b1, b2_ == b2, b3_ == b3)

def move5(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return And( b5_ == 0.0,  b1_ == 0.0, b2_ == b2, b3_ == b3, b4_ == b4)

def controller(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_):
    return Or(move1(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_), move2(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_), move3(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_), move4(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_), move5(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_))

b1 = Real('b1')
b2 = Real('b2')
b3 = Real('b3')
b4 = Real('b4')
b5 = Real('b5')
b1_ = Real('b1_')
b2_ = Real('b2_')
b3_ = Real('b3_')
b4_ = Real('b4_')
b5_ = Real('b5_')
b1__ = Real('b1__')
b2__ = Real('b2__')
b3__ = Real('b3__')
b4__ = Real('b4__')
b5__ = Real('b5__')
C = sys.argv[1]


wpAssertion = Exists([b1_, b2_, b3_, b4_, b5_], And(controller(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_),guarantee(b1_, b2_, b3_, b4_, b5_, C), ForAll([b1__, b2__, b3__, b4__, b5__], Implies(environment(b1_, b2_, b3_, b4_, b5_, b1__, b2__, b3__, b4__, b5__), guarantee(b1__, b2__, b3__, b4__, b5__, C) ) ) ) )

g =Goal()
g.add(wpAssertion)
wp = tactic_qe_fixpoint(g).as_expr()
# print wp
W = And(wp, guarantee(b1, b2, b3, b4, b5, C))
F = guarantee(b1, b2, b3, b4, b5, C)
i = 0
print("Iteration", i )
while(not valid(Implies(F, W),0)):
# while(not valid(F == W)): gives same as above so => holds one way
    #Backup for F
    temp = W
    #Substitute current variables with post variables
    W = substitute(W, (b1, b1__), (b2, b2__), (b3, b3__), (b4, b4__), (b5, b5__))

    #Macros become useless here as substitute W directly here. See some form of dynamic function assignment and then calling like guarantee() = return W. Update in this line. else unnecessary formula repetition

    wpAssertion = Exists([b1_, b2_, b3_, b4_, b5_], And(controller(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_),guarantee(b1_, b2_, b3_, b4_, b5_, C), ForAll([b1__, b2__, b3__, b4__, b5__], Implies(environment(b1_, b2_, b3_, b4_, b5_, b1__, b2__, b3__, b4__, b5__), W ) ) ) )

    g = Goal()
    g.add(wpAssertion)
    wp = tactic_qe_fixpoint(g).as_expr()
    W = And(wp, guarantee(b1, b2, b3, b4, b5, C))
    F = temp
    i=i+1
    print("Iteration ", i )

print("")
print("Number of times WP computed: ", i+1)
print("")

# F = False

if not satisfiable(F,0):
    print("Invariant is Unsatisifiable i.e. False")
    print("UNREALIZABLE")
else:
    print("Invariant is Satisfiable")
    print("REALIZABLE")
    print("EXTRACTING CONTROLLER...")
    #Controller ex)traction
    # In the invariant, substitute with post varaibles
    #Take backup of invariant to analyse in the end
    Invariant = F
    F = substitute(F, (b1, b1__), (b2, b2__), (b3, b3__), (b4, b4__), (b5, b5__))

    # WP for each move wrt F
    condition_move1 = Exists([b1_, b2_, b3_, b4_, b5_], And(move1(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_),guarantee(b1_, b2_, b3_, b4_, b5_, C), ForAll([b1__, b2__, b3__, b4__, b5__], Implies(environment(b1_, b2_, b3_, b4_, b5_, b1__, b2__, b3__, b4__, b5__), F ) ) ) )

    condition_move2 = Exists([b1_, b2_, b3_, b4_, b5_], And(move2(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_),guarantee(b1_, b2_, b3_, b4_, b5_, C), ForAll([b1__, b2__, b3__, b4__, b5__], Implies(environment(b1_, b2_, b3_, b4_, b5_, b1__, b2__, b3__, b4__, b5__), F ) ) ) )

    condition_move3 = Exists([b1_, b2_, b3_, b4_, b5_], And(move3(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_),guarantee(b1_, b2_, b3_, b4_, b5_, C), ForAll([b1__, b2__, b3__, b4__, b5__], Implies(environment(b1_, b2_, b3_, b4_, b5_, b1__, b2__, b3__, b4__, b5__), F ) ) ) )

    condition_move4 = Exists([b1_, b2_, b3_, b4_, b5_], And(move4(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_),guarantee(b1_, b2_, b3_, b4_, b5_, C), ForAll([b1__, b2__, b3__, b4__, b5__], Implies(environment(b1_, b2_, b3_, b4_, b5_, b1__, b2__, b3__, b4__, b5__), F ) ) ) )

    condition_move5 = Exists([b1_, b2_, b3_, b4_, b5_], And(move5(b1, b2, b3, b4, b5, b1_, b2_, b3_, b4_, b5_),guarantee(b1_, b2_, b3_, b4_, b5_, C), ForAll([b1__, b2__, b3__, b4__, b5__], Implies(environment(b1_, b2_, b3_, b4_, b5_, b1__, b2__, b3__, b4__, b5__), F ) ) ) )

    #Move 1 condition extraction
    #Eliminate quantifiers and simplify to get the conditions for each move
    g = Goal()
    g.add(condition_move1)
    #Eliminate qe and conjunct with guarantee
    condition_move1 = And(tactic_qe_controller(g).as_expr(), guarantee(b1, b2, b3, b4, b5, C))
    g = Goal()
    g.add(condition_move1)
    #Simplify to get final condition
    condition_move1 = tactic_simplification(g).as_expr()

    #Move 2 condition extraction
    #Eliminate quantifiers and simplify to get the conditions for each move
    g = Goal()
    g.add(condition_move2)
    #Eliminate qe and conjunct with guarantee
    condition_move2 = And(tactic_qe_controller(g).as_expr(), guarantee(b1, b2, b3, b4, b5, C))
    g = Goal()
    g.add(condition_move2)
    #Simplify to get final condition
    condition_move2 = tactic_simplification(g).as_expr()

    #Move 3 condition extraction
    #Eliminate quantifiers and simplify to get the conditions for each move
    g = Goal()
    g.add(condition_move3)
    #Eliminate qe and conjunct with guarantee
    condition_move3 = And(tactic_qe_controller(g).as_expr(), guarantee(b1, b2, b3, b4, b5, C))
    g = Goal()
    g.add(condition_move3)
    #Simplify to get final condition
    condition_move3 = tactic_simplification(g).as_expr()

    #Move 4 condition extraction
    #Eliminate quantifiers and simplify to get the conditions for each move
    g = Goal()
    g.add(condition_move4)
    #Eliminate qe and conjunct with guarantee
    condition_move4 = And(tactic_qe_controller(g).as_expr(), guarantee(b1, b2, b3, b4, b5, C))
    g = Goal()
    g.add(condition_move4)
    #Simplify to get final condition
    condition_move4 = tactic_simplification(g).as_expr()

    #Move 5 condition extraction
    #Eliminate quantifiers and simplify to get the conditions for each move
    g = Goal()
    g.add(condition_move5)
    #Eliminate qe and conjunct with guarantee
    condition_move5 = And(tactic_qe_controller(g).as_expr(), guarantee(b1, b2, b3, b4, b5, C))
    g = Goal()
    g.add(condition_move5)
    #Simplify to get final condition
    condition_move5 = tactic_simplification(g).as_expr()

    print("MOVE 1 CONDITION:")
    print(condition_move1)
    print("")
    print("MOVE 2 CONDITION:")
    print(condition_move2)
    print("")
    print("MOVE 3 CONDITION:")
    print(condition_move3)
    print("")
    print("MOVE 4 CONDITION:")
    print(condition_move4)
    print("")
    print("MOVE 5 CONDITION:")
    print(condition_move5)
    print("")

    
    #Sanity check: Disjunction of controller conditions is equal to Invariant
    formula = Or(condition_move1, condition_move2, condition_move3, condition_move4, condition_move5) == Invariant
    # formula = condition_move1 == Invariant
    # formula = Implies(condition_move1, Invariant)
    # formula = Implies(Invariant, condition_move1)
    valid(formula,0)