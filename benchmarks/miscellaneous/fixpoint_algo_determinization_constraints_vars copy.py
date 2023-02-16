from z3 import *
from benchmark import *
from itertools import chain, combinations

# describe_tactics()

# Fixpoint algorithm with deterministic Succ over arrays

# tactic_qe_fixpoint= Then(Then(Then(Then(Tactic('qe_rec'), Tactic('qe2')), Tactic('qe')), Tactic('simplify')), Repeat('ctx-solver-simplify')) #Best tactic combination so far that works for simplification for 1.9999999
# tactic_qe_fixpoint= Then(Then(Then(Tactic('qe_rec'), Tactic('qe2')), Tactic('qe')), Tactic('simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe2'), Tactic('simplify'))
tactic_qe_fixpoint = Tactic('qe2') #C=2.0 and C=3.0 this works faster

# Controller Extraction: Use same tactic as fixpoint and use ctx-solver-simplify to make the controller readable.
tactic_qe_controller = tactic_qe_fixpoint
tactic_simplification = Repeat('ctx-solver-simplify')

def print_states(formula):
    print("Printing determinized automaton states")
    # #Function to check models
    s = Solver()
    # s.add(And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==1, c[4]==1, c[5]==-1, succ(c,sigma[1],c_)))
    # s.add(And(c_[0]==-1, c_[1]==1, c_[2]==-1, c_[3]==-1, c_[4]==-1, c_[5]==-1, succ(c,sigma[3],c_)))
    s.add(formula)
    count = 0
    while s.check() == sat:
        count+=1
        # Print readable model
        m = s.model()
        model = []
        for i in range(nQ):
            model.append((i, m[c[i]]))
        print(model)
        # Block current model
        constraints = Or(False)
        for i in range(nQ):
            constraints = Or(constraints, c[i] != m.evaluate(c[i]))
        s.add(constraints)
    # Print total number of states
    print("Number of states:", count)

# Function to check validity of a formula
def valid(formula):
    s = Solver()
    s.add(Not(formula))
    result = s.check()
    if result == unsat:
        print("Valid")
        return True
    if result ==unknown:
        print("Unknown: Not able to solve")
        return False
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

# 3. Define Guarantee
def guarantee_c(c):

    l_bound = And([c[q] >= -1 for q in range(0, len(c))])
    u_bound = And([c[q] < k+1 for q in range(0, len(c))])
    bot = And([c[q] == -1 for q in range(0, len(c))])

    return And(l_bound, u_bound, Not(bot))

# Define succ function for determinization

def min(x,y):
    return If(x < y, x, y)

# Plug in sigma_x and c_ to get c
def succ(c, sigma_x, c_):

    # 1. Range Constraints

    range_c = And([And(c[q] >= -1, c[q] <= k+1) for q in range(0, len(c))])
    range_c_ = And([And(c_[q] >= -1, c_[q] <= k+1) for q in range(0, len(c))])

    # 2. Reachability constraint
    # Target state number is reachable iff ( exists some transition to it on some input)
    # One direction is enough. The other is implied from the determinization constraint
    
    reach = And([Implies(c_[q] != -1,  Or([Exists(s, And(automaton(p,q,*s), sigma_x, c[p] != -1)) for p in range(0, len(c))])) for q in range(0, len(c_))])

    # 3. Determinization constraint

    # This constraint gives the count on valid target states that has >1 input states.
    det1 = And([And([And([ForAll(s, Implies(And(automaton(p,q,*s), sigma_x, c[p] != -1, automaton(p_,q,*s), sigma_x, c[p_] <= c[p], c[p_] != -1, p!=p_), c_[q] == min(c[p] + isFinal(q) , k+1))) for p_ in range(0, len(c))]) for p in range(0, len(c))]) for q in range(0, len(c_))])
    # print("det1")
    # print(det1)
    # This constraint gives the count on valid target states that has 1 input state.
    det2 = And([And([ForAll(s, Implies(And(automaton(p,q,*s), sigma_x, c[p] != -1, Not(Or([ And(automaton(p_,q,*s), sigma_x, c[p_] != -1, p!=p_) for p_ in range(0, len(c))]) )), c_[q] == min(c[p] + isFinal(q) , k+1))) for p in range(0, len(c))]) for q in range(0, len(c_))])

    return And(range_c, range_c_, reach, det1, det2)

#Get states from environment
s=[]
for var in environment.__code__.co_varnames:
    if not str(var).__contains__("_"):
        #Dynamic variable declaration
        #Issue: Can't use variable s in the code because it will get redeclared in this scope.
        exec(str(var) +"= Real('"+str(var) +"')")
        s.append(locals()[var])

#Declare and define s'
s_ = []
for var in s:
    exec(str(var)+"_" +" = Real('"+str(var)+"_" +"')")
    s_.append(locals()[str(var)+"_"])

#Declare and define s''
s__ = []
for var in s:
    exec(str(var)+"__" +" = Real('"+str(var)+"__" +"')")
    s__.append(locals()[str(var)+"__"])



c = IntVector('c', nQ)
c_ = IntVector('c_', nQ)
c__ = IntVector('c__', nQ)

k = 1

def guarantee_(s, c):
    return And(guarantee(*s), guarantee_c(c))
# print(guarantee_(s,c))
# exit()


# predicates = pred(*s)
# print(predicates)

# def powerset(iterable):
#     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

# print(list(powerset(predicates)))

# exit()

#0. Create Controller
# See if List Comprehension (or some better way can make it a single Or formula)
controller = False
for move in controller_moves:
    controller = Or(move(*s+s_), controller)


# solve(And(c[0]==0, c[1)==-1, c(2)==-1, c(3)==1, c(4)==1, c(5)==-1, succ(c,sigma[1],c_, k)))

# def Succ(c, x, c_):
#     return Or(  And(succ(c,sigma[0],c_), x == 1),
#                 And(succ(c,sigma[1],c_), x == 2),
#                 And(succ(c,sigma[2],c_), x == 3),
#                 And(succ(c,sigma[3],c_), Not(And(x>=1, x<=3))))

def Succ(c, x_subst, c_):
    return Or([And( substitute(sigma[i], [(s[j], x_subst[j]) for j in range(len(s))] ), succ(c,sigma[i],c_) ) for i in range(len(sigma))])

# exit()
# print(substitute(Succ(c, x, c_), (x, x__)))
# solve(And(c_[0]==0, c_[1]==-1, c_[2]==1, c_[3]==-1, c_[4]==2, c_[5]==1, Succ(c,x,c_, k), x== 2))
# solve(And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==1, c[4]==1, c[5]==-1, Succ(c,x,c_), x== 2))
# solve(And(c[0]==0, c[1]==-1, Succ(c,x,c_), 0<=x, x<=2))

# Succ takes more time to solve than succ. Optimize.
# solve(And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==1, c[4]==1, c[5]==-1, Succ(c,x,c_), x== 2))
# solve(And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==1, c[4]==1, c[5]==-1, succ(c,sigma[1],c_)))




# exit()

# X = Array('x', IntSort(), IntSort())
# 2. More efficient solution

#Vector of z3 variables

# X = IntVector('x', 3)
# print(X[0] + X[1] + X[2] >= 0)
# print(Sum(X) >= 0)
# solve(Exists([X[0]], Succ(c, x, c_, k)))

# solve(Exists([X], Succ(c, x, c_, k)))

# print([x_]+c_)
# print()
# My use case
# print_states(guarantee(x,c))
# exit()

#Create list of tuples for substitution pre variables with post
substList = []
for (var, var__) in zip(s,s__):
    substList = substList+[(var,var__)]

sigma = sigma(*s)
# print(sigma)
# print(substList)
# print(Succ(c,s,c_))
# exit()
# print(s)
# print(c)
# exit()

print("Creating wpAssertion")
# wpAssertion = Exists([x_, c_[0], c_[1]], And(controller(x,x_), Succ(c,x,c_), guarantee(x_,c_), ForAll([x__, c__[0], c__[1]], Implies(And(environment(x_,x__), Succ(c_,x_,c__)), guarantee(x__,c__)))))
wpAssertion = Exists(s_+c_, And(controller, Succ(c,s,c_), guarantee_(s_,c_), ForAll(s__+c__, Implies(And(environment(*s_+s__), Succ(c_,s_,c__)), guarantee_(s__,c__)))))
print("Projecting")
g =Goal()
g.add(wpAssertion)
wp = tactic_qe_fixpoint(g).as_expr()
# print(wp)
print_states(wp)

print("Projection done")
W = And(wp, guarantee_(s, c))
F = guarantee_(s, c)
i = 0
print("Iteration", i )
while(not valid(Implies(F, W))):
    temp = W
    #Substitute current variables with post variables

    W = substitute(W, *substList+[(c[j], c__[j]) for j in range(nQ)])

    # W = substitute(W, (x, x__), (c[0], c__[0]), (c[1], c__[1]), (c[2], c__[2]), (c[3], c__[3]), (c[4], c__[4]), (c[5], c__[5]))

    #Macros become useless here as substitute W directly here. See some form of dynamic function assignment and then calling like guarantee() = return W. Update in this line. else unnecessary formula repetition

    # wpAssertion = Exists([x_, c_[0], c_[1]], And(controller(x,x_), Succ(c,x,c_), guarantee(x_,c_), ForAll([x__, c__[0], c__[1]], Implies(And(environment(x_,x__), Succ(c_,x_,c__)), W))))
    # wpAssertion = Exists(s_+c_, And(controller, Succ(c,s,c_), guarantee_(*s_+[c_]), ForAll(s__+c__, Implies(And(environment(*s_+s__), Succ(c_,s_,c__)), W))))
    wpAssertion = Exists(s_+c_, And(controller, Succ(c,s,c_), guarantee_(s_,c_), ForAll(s__+c__, Implies(And(environment(*s_+s__), Succ(c_,s_,c__)), W))))    
    g = Goal()
    g.add(wpAssertion)
    wp = tactic_qe_fixpoint(g).as_expr()
    W = And(wp, guarantee_(s, c))
    print_states(W)
    print("W ", i)
    W.sexpr()
    # print(toSMT2Benchmark(W, logic="LRA")
    F = temp
    i=i+1
    print("Iteration ", i )

print("")
print("Number of times WP computed: ", i+1)
print("")

init_formula = c[0] == 0
init = And(init_formula, And([c[q] == -1 for q in range(1,nQ)]))
# init = And(c[0]==0, c[1]==-1)
# init = And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==-1, c[4]==-1, c[5]==-1)
# init = And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==-1, c[4]==-1)
# init = And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==-1)

if not satisfiable(And(F, init)):
    print("Invariant is Unsatisifiable i.e. False")
    print("UNREALIZABLE")
    g = Goal()
    g.add(F)
    F = tactic_qe_fixpoint(g).as_expr()
    print("Invariant is: ")
    print(F)
    g = Goal()
    
    # g.add(Exists([c[0], c[1]], F))
    g.add(Exists(c, F))
    PF = tactic_qe_fixpoint(g).as_expr()
    print("Projected invariant is: ")
    print(PF)
else:
    print("Invariant is Satisfiable")
    print("REALIZABLE")
    g = Goal()
    g.add(F)
    F = tactic_qe_fixpoint(g).as_expr()
    print("Invariant is: ")
    print(F)
    print_states(F)
    g = Goal()
    
    # g.add(Exists([c[0], c[1]], F))
    g.add(Exists(c, F))
    PF = tactic_qe_fixpoint(g).as_expr()
    print("Projected invariant is: ")
    print(PF)

    g.add(Exists(c, And(F, init)))
    PF = tactic_qe_fixpoint(g).as_expr()
    print("Projected invariant for initial state is: ")
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



# s = SolverFor('QF_UFBV')

# # s.add(guarantee(x,c_))

# # s.add(guarantee(x,c))
# valid(succ(c,sigma[0],c_))
# print(s.check())

# # Shows Succ with c and c_ as arrays give a solution
# solve(Succ(c, x, c_))
# uf_example = ForAll([c[0], c[1],x], And(c[0]==0, c[1]==-1, Succ(c, x, c_)))
# g =Goal()
# g.add(uf_example)
# print("Printing uf")
# uf_example_projected = tactic_qe_fixpoint(g).as_expr()
# print(uf_example_projected)