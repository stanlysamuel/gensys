from z3 import *

# EAA algorithm for infinite games with LTL properties
# No counters in state space. 
# Simple safety algorithm i,e., for k = 0
# Extend with counters

# tactic_qe_fixpoint= Then(Then(Then(Then(Tactic('qe_rec'), Tactic('qe2')), Tactic('qe')), Tactic('simplify')), Repeat('ctx-solver-simplify')) #Best tactic combination so far that works for simplification for 1.9999999
# tactic_qe_fixpoint= Then(Then(Then(Tactic('qe_rec'), Tactic('qe2')), Tactic('qe')), Tactic('simplify'))
tactic_qe_fixpoint = Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe_rec'), Tactic('simplify'))
# tactic_qe_fixpoint = Tactic('qe_rec') #C=2.0 and C=3.0 this works faster

# Controller Extraction: Use same tactic as fixpoint and use ctx-solver-simplify to make the controller readable.
tactic_qe_controller = tactic_qe_fixpoint
tactic_simplification = Repeat('ctx-solver-simplify')

# Function to check validity of a formula
def valid(formula):
    s = Solver()
    s.add(Not(formula))
    if s.check() == unsat:
        print("Valid")
        return True
    else:
        print("Not Valid")
        return False

# Function to check satisfiability of a formula
def satisfiable(formula):
    s = Solver()
    s.add(formula)
    if s.check() == sat:
        print(s.model())
        return True
    else:
        return False

def check_conflict(F, controller, automaton):
    # Query to check if conflicting states occur or not.
    # If there exists a strategy, then it must be against all moves of the environment; hence, no need to add query for the environment moves.
    # Thus, we need to check if there exists same game states and different automaton states that have NO COMMON STRATEGY!
    s1 = Int('s1')
    s2 = Int('s2')
    s1_ = Int('s1_')
    s2_ = Int('s2_')
    x1 = Int('x1')
    x1_ = Int('x1_')
    x1__ = Int('x1__')

    W1 = substitute(F, (s, s1), (x,x1)) # State (s1, x1)
    W2 = substitute(F, (s, s2), (x,x1)) # State (s2, x1)

    W11 = substitute(F, (s, s1_), (x, x1_)) # State (s1_, x1_)
    W21 = substitute(F, (s, s2_), (x, x1_)) # State (s2_, x1_)
    W12 = substitute(F, (s, s1_), (x, x1__)) # State (s1_, x1_)
    W22 = substitute(F, (s, s2_), (x, x1__)) # State (s2_, x1_)

    T1 = And(controller(x1,x1_),  ForAll([s1_], Implies(automaton(s1,s1_,x1), W11 )))
    T2 = And(controller(x1,x1_),  ForAll([s2_], Implies(automaton(s2,s2_,x1), W21 )))
    T3 = And(controller(x1,x1__), ForAll([s1_], Implies(automaton(s1,s1_,x1), W12 )))
    T4 = And(controller(x1,x1__), ForAll([s2_], Implies(automaton(s2,s2_,x1), W22 )))

    # Attempt 1
    # unsat => CN's exist (definition of CN was different)
    # query_formula = And(W1, W2, T1, T2, T3, T4, s1 != s2, x1_ != x1__)

    # Attempt 2
    # unsat => CN's exist
    # query_formula_1 = And(W1, W2, T1, T2, T3, T4, s1 != s2, ForAll([x_], x1_ != x1__))
    # query_formula_2 = And(W1, W2, T1, T2, T3, T4, s1 != s2, ForAll([x__], x1_ != x1__))
    # query_formula = Or(query_formula_1, query_formula_2)

    # Attempt 3
    # sat => no CN's exist
    # query_formula = ForAll([s1,s2,x1], Implies( And(W1, W2, s1 != s2), Exists([x1_, x1__], And(T1, T2, T3, T4, x1_ == x1__)) ))
    # # unsat => no CN's exist
    # query_formula = Exists([s1,s2,x1], And(W1, W2, s1 != s2, ForAll([x1_, x1__], Implies(And(T1, T2, T3, T4), x1_ != x1__))))
    query_formula = And(W1, W2, s1 != s2, ForAll([x1_, x1__], Implies(And(T1, T2, T3, T4), x1_ != x1__)))
    solver = Solver()
    
    # print(solver.check(query_formula))
    # print(solver.model())
    return solver.check(query_formula)

# 1. Define Automaton

def automaton(s, s_, x):
    return Or(
            And(s == 1, s_==1),
            And(s == 1, s_==2, Or(x<1, x>10)),
            And(s == 2, s_==2)
            )

# 2. Define Environment moves.

# Environment moves as Disjunction of Conjunctions: Simplified.
def environment(x, x_):
        return x_== x

#2. Define Controller moves
def controller(x, x_):
    return Or(x_== x+1, x_== x-1)

# 3. Define Guarantee
def guarantee(s, x):
    return s==1

s = Int('s')
x = Int('x')
# c = Int('c')

s_ = Int('s_')
x_ = Int('x_')
# c_ = Int('c_')

s__ = Int('s__')
x__ = Int('x__')
# c__ = Int('c__')

wpAssertion = Exists([x_], ForAll([s_], And(controller(x,x_), Implies(automaton(s,s_,x), And(guarantee(s_, x_), ForAll([x__, s__], Implies(And(environment(x_, x__), automaton(s_, s__, x_)), guarantee(s__,x__))))))))

g =Goal()
g.add(wpAssertion)
wp = tactic_qe_fixpoint(g).as_expr()

W = And(wp, guarantee(s, x))
F = guarantee(s, x)
i = 0
print("Iteration", i )
while(not valid(Implies(F, W))):
    temp = W
    #Substitute current variables with post variables
    W = substitute(W, (s, s__), (x, x__))

    #Macros become useless here as substitute W directly here. See some form of dynamic function assignment and then calling like guarantee() = return W. Update in this line. else unnecessary formula repetition

    wpAssertion = Exists([x_], ForAll([s_], And(controller(x,x_), Implies(automaton(s,s_,x), And(guarantee(s_, x_), ForAll([x__, s__], Implies(And(environment(x_, x__), automaton(s_, s__, x_)), W)))))))

    g = Goal()
    g.add(wpAssertion)
    wp = tactic_qe_fixpoint(g).as_expr()
    W = And(wp, guarantee(s, x))
    print("W ", i)
    # print toSMT2Benchmark(W, logic="LRA")
    F = temp
    i=i+1
    print("Iteration ", i )

print("")
print("Number of times WP computed: ", i+1)
print("")

if not satisfiable(F):
    print("Invariant is Unsatisifiable i.e. False")
    print("UNREALIZABLE")
else:
    print("Invariant is Satisfiable")
    print("REALIZABLE")
    g = Goal()
    g.add(F)
    F = tactic_qe_fixpoint(g).as_expr()
    print("Invariant is: ")
    print(F)
    g = Goal()
    g.add(Exists([s], F))
    PF = tactic_qe_fixpoint(g).as_expr()
    print("Projected invariant is: ")
    print(PF)

    # Check for conflicting nodes.
    # F = And(s!=4, s!=5, s>=1, s<=5, x>=0, x<=3)
    if check_conflict(F, controller, automaton) == unsat:
        #If above is UNSAT, then we can extract the controller directly by projecting out s and extracting controller using the regular technique.
        print("Extracting controller by projecting out the automaton state space")
        #Take backup of invariant to analyse in the end
        Invariant = F
        F = substitute(F, (s, s__), (x, x__))

        # WP for each move wrt F
        condition_move1 = Exists([x_], ForAll([s_], And(x_ == x + 1, Implies(automaton(s,s_,x), And(guarantee(s_, x_), ForAll([x__, s__], Implies(And(environment(x_, x__), automaton(s_, s__, x_)), F))) ))))

        condition_move2 = Exists([x_], ForAll([s_], And(x_ == x - 1, Implies(automaton(s,s_,x), And(guarantee(s_, x_), ForAll([x__, s__], Implies(And(environment(x_, x__), automaton(s_, s__, x_)), F))) ))))

        #Move 1 condition extraction
        #Eliminate quantifiers and simplify to get the conditions for each move
        g = Goal()
        g.add(condition_move1)
        #Eliminate qe and conjunct with guarantee
        condition_move1 = And(tactic_qe_controller(g).as_expr(), guarantee(s, x))
        g = Goal()
        g.add(condition_move1)
        #Simplify to get final condition
        condition_move1 = tactic_simplification(g).as_expr()
        condition_move1 = tactic_qe_fixpoint(g).as_expr()

        #Move 2 condition extraction
        #Eliminate quantifiers and simplify to get the conditions for each move
        g = Goal()
        g.add(condition_move2)
        #Eliminate qe and conjunct with guarantee
        condition_move2 = And(tactic_qe_controller(g).as_expr(), guarantee(s, x))
        g = Goal()
        g.add(condition_move2)
        #Simplify to get final condition
        condition_move2 = tactic_simplification(g).as_expr()
        condition_move2 = tactic_qe_fixpoint(g).as_expr()

        print("MOVE 1 CONDITION:")
        print(condition_move1)
        g = Goal()
        g.add(Exists([s], condition_move1))
        condition_move1_ = tactic_qe_fixpoint(g).as_expr()
        print("Projected move 1 is: ")
        print(condition_move1_)
        print("")
        print("MOVE 2 CONDITION:")
        print(condition_move2)
        g = Goal()
        g.add(Exists([s], condition_move2))
        condition_move2_ = tactic_qe_fixpoint(g).as_expr()
        print("Projected move 2 is: ")
        print(condition_move2_)
        print("")
        #Interesting point in this output is that 1 does not occur here although we can decrement it to 0.

        #Sanity check: Disjunction of controller conditions is equal to Invariant
        formula = Or(condition_move1, condition_move2) == Invariant
        valid(formula)

    else:
        print("Conflict nodes exist in the winning region of the product graph")