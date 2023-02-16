from z3 import *

# describe_tactics()

# Fixpoint algorithm with deterministic Succ over arrays

# tactic_qe_fixpoint= Then(Then(Then(Then(Tactic('qe_rec'), Tactic('qe2')), Tactic('qe')), Tactic('simplify')), Repeat('ctx-solver-simplify')) #Best tactic combination so far that works for simplification for 1.9999999
# tactic_qe_fixpoint= Then(Then(Then(Tactic('qe_rec'), Tactic('qe2')), Tactic('qe')), Tactic('simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe'), Tactic('simplify'))
tactic_qe_fixpoint = Tactic('qe') #C=2.0 and C=3.0 this works faster

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

# 1. Define Automaton

#Complete automaton from spot
def automaton(q, q_, x):
    return Or(
            And(q == 0, q_==0, And(x>=1, x<=3)),
            And(q == 0, q_==1, Not(And(x>=1, x<=3))),
            And(q == 1, q_==1),
            And(q == 0, q_==2, And(x>=1, x<=3, x!=1)),
            And(q == 2, q_==2, x!=1),
            And(q == 2, q_==5, x==1),
            And(q == 0, q_==3, And(x>=1, x<=3, x!=2)),
            And(q == 3, q_==3, x!=2),
            And(q == 3, q_==5, x==2),
            And(q == 0, q_==4, And(x>=1, x<=3, x!=3)),
            And(q == 4, q_==4, x!=3),
            And(q == 4, q_==5, x==3),
            And(q == 5, q_==5),
            )

# 2. Define Environment moves.

# Environment moves as Disjunction of Conjunctions: Simplified.
def environment(x, x_):
        return x_== x

#2. Define Controller moves
def controller(x, x_):
    return Or(x_== x+1, x_== x-1, x_==x)

# 3. Define Guarantee
def guarantee(x, c):
    q = Int('q')
    range_q = And(q>=0, q<=5)
    range_c = And(c[q] >= -1, c[q] < 2)
    return And(ForAll([q], And(Implies(range_q, And(range_c), Implies(Not(range_q), c[q] == -1) ))))

# Define succ function for determinization

def min(x,y):
    return If(x < y, x, y)

def isFinal(p):
    return If(And(p <=4, p >=1), 1, 0)

def succ(c, x, c_, k):
    p = Int('p')
    q = Int('q')

    # 1. Range Constraints

    range_q = And(q>=0, q<=5) #gets finite models

    range_c = And(c[q] >= -1, c[q] < k+1)
    range_c_ = And(c_[q] >= -1, c_[q] < k+1)

    # 2. Reachability constraint
    # Target state number is reachable iff ( exists some transition to it on some input)
    # One direction is enough. The other is implied from the determinization constraint
    
    reach = Implies(c_[q] != -1, Exists([p,x], And(automaton(p,q,x), c[p] != -1)))

    # 3. Determinization constraint
    p_ = Int('p_')

    # This constraint gives the count on valid target states that has >1 input states.
    det1 = ForAll([p,p_,x], Implies(And(automaton(p,q,x), c[p] != -1, automaton(p_,q,x), c[p_] <= c[p], c[p_] != -1, p!=p_), c_[q] == min(c[p] + isFinal(q) , k+1)))

    # This constraint gives the count on valid target states that has 1 input state.
    det2 = ForAll([p,x], Implies(And(automaton(p,q,x), c[p] != -1, Not(Exists([p_], And(automaton(p_,q,x), c[p_] != -1, p!=p_)))), c_[q] == min(c[p] + isFinal(q) , k+1)))

    return ForAll([q], Implies(range_q, And(range_c, range_c_, reach, det1, det2)))

x = Int('x')
c = Array('c', IntSort(), IntSort())

x_ = Int('x_')
c_ = Array('c_', IntSort(), IntSort())

x__ = Int('x__')
c__ = Array('c__', IntSort(), IntSort())

k = 2

# My use case
wpAssertion = Exists([x_, c_], And(controller(x,x_), succ(c,x,c_,k), guarantee(x_,c_), ForAll([x__, c__], Implies(And(environment(x_,x__), succ(c_,x_,c__,k)), guarantee(x__,c__)))))

g =Goal()
g.add(wpAssertion)
wp = tactic_qe_fixpoint(g).as_expr()

W = And(wp, guarantee(x, c))
F = guarantee(x, c)
i = 0
print("Iteration", i )
while(not valid(Implies(F, W))):
    temp = W
    #Substitute current variables with post variables
    W = substitute(W, (x, x__), (c, c__))

    #Macros become useless here as substitute W directly here. See some form of dynamic function assignment and then calling like guarantee() = return W. Update in this line. else unnecessary formula repetition

    wpAssertion = Exists([x_, c_], And(controller(x,x_), succ(c,x,c_,k), guarantee(x_,c_), ForAll([x__, c__], Implies(And(environment(x_,x__), succ(c_,x_,c__,k)), W))))

    g = Goal()
    g.add(wpAssertion)
    wp = tactic_qe_fixpoint(g).as_expr()
    W = And(wp, guarantee(x, c))
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
    g.add(Exists([c], F))
    PF = tactic_qe_fixpoint(g).as_expr()
    print("Projected invariant is: ")
    print(PF)

    # print("Extracting controller by projecting out the automaton state space")
    # #Take backup of invariant to analyse in the end
    # Invariant = F
    # F = substitute(F, (s, s__), (x, x__), (c,c__))

    # # WP for each move wrt F
    # condition_move1 = Exists([x_], ForAll([s_, c_], And(x_ == x + 1, Implies(And(automaton(s,s_,x), counter_constraints(s_, c, c_)), And(guarantee(s_, x_, c_), ForAll([x__, s__, c__], Implies(And(environment(x_, x__), automaton(s_, s__, x_), counter_constraints(s__, c_, c__)), F)))))))

    # condition_move2 = Exists([x_], ForAll([s_, c_], And(x_ == x - 1, Implies(And(automaton(s,s_,x), counter_constraints(s_, c, c_)), And(guarantee(s_, x_, c_), ForAll([x__, s__, c__], Implies(And(environment(x_, x__), automaton(s_, s__, x_), counter_constraints(s__, c_, c__)), F)))))))

    # #Move 1 condition extraction
    # #Eliminate quantifiers and simplify to get the conditions for each move
    # g = Goal()
    # g.add(condition_move1)
    # #Eliminate qe and conjunct with guarantee
    # condition_move1 = And(tactic_qe_controller(g).as_expr(), guarantee(s, x, c))
    # g = Goal()
    # g.add(condition_move1)
    # #Simplify to get final condition
    # condition_move1 = tactic_simplification(g).as_expr()
    # condition_move1 = tactic_qe_fixpoint(g).as_expr()

    # #Move 2 condition extraction
    # #Eliminate quantifiers and simplify to get the conditions for each move
    # g = Goal()
    # g.add(condition_move2)
    # #Eliminate qe and conjunct with guarantee
    # condition_move2 = And(tactic_qe_controller(g).as_expr(), guarantee(s, x,c))
    # g = Goal()
    # g.add(condition_move2)
    # #Simplify to get final condition
    # condition_move2 = tactic_simplification(g).as_expr()
    # condition_move2 = tactic_qe_fixpoint(g).as_expr()

    # print("MOVE 1 CONDITION:")
    # print(condition_move1)
    # g = Goal()
    # g.add(Exists([s,c], condition_move1))
    # condition_move1_ = tactic_qe_fixpoint(g).as_expr()
    # print("Projected move 1 is: ")
    # print(condition_move1_)
    # print("")
    # print("MOVE 2 CONDITION:")
    # print(condition_move2)
    # g = Goal()
    # g.add(Exists([s,c], condition_move2))
    # condition_move2_ = tactic_qe_fixpoint(g).as_expr()
    # print("Projected move 2 is: ")
    # print(condition_move2_)
    # print("")

    # #Sanity check: Disjunction of controller conditions is equal to Invariant
    # formula = Or(condition_move1, condition_move2) == Invariant
    # valid(formula)

