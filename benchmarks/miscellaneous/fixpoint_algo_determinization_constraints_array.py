from z3 import *

# describe_tactics()
set_param(verbose=10)
# sys.setrecursionlimit(500000)
# Fixpoint algorithm with deterministic Succ over arrays

# tactic_qe_fixpoint= Then(Then(Then(Then(Tactic('qe_rec'), Tactic('qe2')), Tactic('qe')), Tactic('simplify')), Repeat('ctx-solver-simplify')) #Best tactic combination so far that works for simplification for 1.9999999
# tactic_qe_fixpoint= Then(Then(Then(Tactic('qe_rec'), Tactic('qe2')), Tactic('qe')), Tactic('simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe'), Tactic('simplify'))
tactic_qe_fixpoint = Tactic('qe-sat') #C=2.0 and C=3.0 this works faster

# Controller Extraction: Use same tactic as fixpoint and use ctx-solver-simplify to make the controller readable.
tactic_qe_controller = tactic_qe_fixpoint
tactic_simplification = Repeat('ctx-solver-simplify')

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

# 1. Define Automaton

#Complete automaton from spot

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

def automaton(q, q_, x):
    return Or(
            And(q == 0, q_==1, Or(x<0, x>2)),
            And(q == 0, q_==0),
            And(q == 1, q_==1),
            )

# 2. Define Environment moves.

# Environment moves as Disjunction of Conjunctions: Simplified.
def environment(x, x_):
        return x_== x

#2. Define Controller moves
def controller(x, x_):
    return Or(x_== x+1, x_== x-1)

# 3. Define Guarantee
def guarantee(x, c):
    q = Int('q')
    range_q = And(q>=0, q< nQ)
    not_bot = Exists([q], And(range_q, c[q]> -1))

    valid_range_constraint = Implies(range_q, And(c[q] >= -1, c[q] < k+1))
    invalid_range_constraint = Implies(Not(range_q), c[q] == -1)

    return And(ForAll([q],And(valid_range_constraint,invalid_range_constraint)), not_bot)


# Define succ function for determinization

def min(x,y):
    return If(x < y, x, y)

# def isFinal(p):
#     return If(And(p <=4, p >=1), 1, 0)

def isFinal(p):
    return If(p==1, 1, 0)

# Plug in sigma_x and c_ to get c
def succ(c, sigma_x, c_):
    p = Int('p')
    q = Int('q')

    # 1. Range Constraints

    range_q = And(q>=0, q< nQ) #gets finite models

    range_c = And(c[q] >= -1, c[q] <= k+1)
    range_c_ = And(c_[q] >= -1, c_[q] <= k+1)

    # 2. Reachability constraint
    # Target state number is reachable iff ( exists some transition to it on some input)
    # One direction is enough. The other is implied from the determinization constraint
    
    reach = Implies(c_[q] != -1, Exists([p,x], And(automaton(p,q,x), sigma_x, c[p] != -1)))

    # 3. Determinization constraint
    p_ = Int('p_')

    # This constraint gives the count on valid target states that has >1 input states.
    det1 = ForAll([p,p_,x], Implies(And(automaton(p,q,x), sigma_x, c[p] != -1, automaton(p_,q,x), sigma_x, c[p_] <= c[p], c[p_] != -1, p!=p_), c_[q] == min(c[p] + isFinal(q) , k+1)))

    # This constraint gives the count on valid target states that has 1 input state.
    det2 = ForAll([p,x], Implies(And(automaton(p,q,x), sigma_x, c[p] != -1, Not(Exists([p_], And(automaton(p_,q,x), sigma_x, c[p_] != -1, p!=p_)))), c_[q] == min(c[p] + isFinal(q) , k+1)))

    return ForAll([q], And(Implies(range_q, And(range_c, range_c_, reach, det1, det2)), Implies(Not(range_q), And(c[q] == -1, c_[q] == -1))))


x = Int('x')
c = Array('c', IntSort(), IntSort())

x_ = Int('x_')
c_ = Array('c_', IntSort(), IntSort())

x__ = Int('x__')
c__ = Array('c__', IntSort(), IntSort())

nQ = 10
k = 0

# c1 = [And(c[q] >= -1, c[q] < k+1) for q in range(0, nQ)]
# c2 = [And(c[q] == -1) for q in range(0, nQ)]

# valid(Implies(guarantee(x,c), And(And(c1), Not(And(c2)))) )

#Vector of Ints

c = IntVector('c', nQ)
# print(c)

c1 = [And(c[q] >= -1, c[q] < k+1) for q in range(0, len(c))]
c2 = [And(c[q] == -1) for q in range(0, len(c))]

s = SolverFor('QF_UFBV')

# s.add(guarantee(x,c_))

s.add(And(And(c1), Not(And(c2))))

print(s.check())

# print(c1)
# print(c2)


# s = Solver()
# s.add(Not(And(And(c1), Not(And(c2)))))

# while s.check() == sat:

#   m = s.model()
#   print(m)
#   s.add(Or(c[0] != m[c[0]], c[1] != m[c[1]]))


# sigma = [x == 1, x == 2, x == 3, Not(And(x>=1, x<=3))]

sigma = [Not(And(x>=0, x<=2)), And(x>=0, x<=2)]

# solve(And(c[0]==0, c[1)==-1, c(2)==-1, c(3)==1, c(4)==1, c(5)==-1, succ(c,sigma[1],c_, k)))
# solve(And(c_[0]==0, c_[1]==-1, c_[2]==1, c_[3]==-1, c_[4]==2, c_[5]==1, succ(c,sigma[0],c_, k)))
def Succ(c, x, c_):
    
    # sigma0 = substitute(sigma[0], (x, y))
    # sigma1 = substitute(sigma[1], (x, y))

    return Or( And(succ(c,sigma[0],c_), Not(And(x>=0, x<=2))),
                And(succ(c,sigma[1],c_), And(x>=0, x<=2)))

    # return Or(  And(succ(c,sigma[0],c_), sigma0),
    #             And(succ(c,sigma[1],c_), sigma1),
    #             # And(succ(c,sigma[2],c_, k), sigma[2]),
    #             # And(succ(c,sigma[3],c_, k), sigma[3])
    #             )

# print(Succ(c_,x__,c__))

# def Succ(c, x, c_, k):
#     return Or(  And(succ(c,sigma[0],c_, k)),
#                 And(succ(c,sigma[1],c_, k)),
#                 And(succ(c,sigma[2],c_, k)),
#                 And(succ(c,sigma[3],c_, k)))

# solve(And(c_[0]==0, c_[1]==-1, c_[2]==1, c_[3]==-1, c_[4]==2, c_[5]==1, Succ(c,x,c_, k), x== 2))
# solve(And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==1, c[4]==1, c[5]==-1, Succ(c,x,c_, k), x== 2))
# solve(And(c_[0]==1, c_[1]==0, Succ(c,x,c_, k), And(x>=0, x<=10)))
# solve(And(c[0]==0, c[1]==-1, Succ(c,x,c_), Not(And(x>=0, x<=10))))
# exit()
# X = Array('x', IntSort(), IntSort())
# 2. More efficient solution

#Vector of z3 variables

# X = IntVector('x', 3)
# print(X[0] + X[1] + X[2] >= 0)
# print(Sum(X) >= 0)
# solve(Exists([X[0]], Succ(c, x, c_, k)))

# solve(Exists([X], Succ(c, x, c_, k)))

# Example where where we bound array variables and where projection also works
# X = Array('x', IntSort(), IntSort())
# array_example = Exists([X], And(X[0] == 3, X[0] != 3))
# g =Goal()
# g.add(array_example)
# array_example_projected = tactic_qe_fixpoint(g).as_expr()
# print(array_example_projected)

# Shows Succ with c and c_ as arrays give a solution
# solve(Succ(c, x, c_))
# uf_example = Exists([c,x], And(c[0]==0, c[1]==-1, Succ(c, x, c_)))
# g =Goal()
# g.add(uf_example)
# print("Printing uf")
# uf_example_projected = tactic_qe_fixpoint(g).as_expr()
# print(uf_example_projected)

# Checking extensibility of arrays. Z3 can't find sat directly but can find unsat.
# s = Solver()
# f = ForAll([c,c_], Implies(ForAll(x, c[x] == c_[x]), c == c_))
# s.add(Not(f))
# # s.add(f)
# s.check()
# print(s.check())

# g =Goal()
# g.add(f)
# print("Using projection")
# f = tactic_qe_fixpoint(g).as_expr()
# print(f)

# f1 = And(Or(c[0] == 0, c[0] == 1), Or(c[1] == 0, c[1] == 1), Or(c[2] == 0, c[2] == 1) )
# solve(Not(f1))
# f2 = ForAll(x, Implies(And(x>=0, x<=2), Or(c[x] == 0, c[x] == 1) ))
# solve(Not(f2))
# exit()

# My use case
wpAssertion = Exists([x_, c_], And(controller(x,x_), Succ(c,x,c_), guarantee(x_,c_), ForAll([x__, c__], Implies(And(environment(x_,x__), Succ(c_,x_,c__)), guarantee(x__,c__)))))

# for_part = Or(ForAll([x__, c__], Implies(And(environment(x_,x__), succ(c_,sigma[0],c__), Not(And(x>=0, x<=2)) ), guarantee(x__,c__))), 
#     ForAll([x__, c__], Implies(And(environment(x_,x__), succ(c_,sigma[1],c__), And(x>=0, x<=2) ), guarantee(x__,c__))))

# wpAssertion = Exists([x_, c_], And(controller(x,x_), Succ(c,x,c_), guarantee(x_,c_), for_part))

# print(wpAssertion)

# # Wrapper for allowing Z3 ASTs to be stored into Python Hashtables. 
# class AstRefKey:
#     def __init__(self, n):
#         self.n = n
#     def __hash__(self):
#         return self.n.hash()
#     def __eq__(self, other):
#         return self.n.eq(other.n)
#     def __repr__(self):
#         return str(self.n)

# def askey(n):
#     assert isinstance(n, AstRef)
#     return AstRefKey(n)

# def get_vars(f):
#     r = set()
#     def collect(f):
#       if is_const(f): 
#           if f.decl().kind() == Z3_OP_UNINTERPRETED and not askey(f) in r:
#               r.add(askey(f))
#       else:
#           for c in f.children():
#               collect(c)
#     collect(f)
#     return r

# g =Goal()
# y = Int('y')
# g.add(Exists([y], x == y + y))
# wp = tactic_qe_fixpoint(g).as_expr()
# print(wp)
# # exit()
# g =Goal()
# g.add(wpAssertion)
# wp = tactic_qe_fixpoint(g).as_expr()
# print(wp)
# W = And(wp, guarantee(x, c))
# F = guarantee(x, c)

# s = Solver()
# s.add(wp)
# state_model = []
# count = 0
# print(s.check())
# print(s.model())
# # exit()

# while s.check() == sat:
# #   print("e")
#   count +=1
#   m = s.model()
#   # print(m)
#   # print("q : {}".format(m[q]))

#   print("c:")
#   c_list = []
#   for i in range(nQ):
#     c_list.append((i, m.evaluate(c[i])))
#   c_list.sort()
#   print(c_list)

#   print("")
  
#   constraints = Or(False)
#   for i in range(nQ):
#     constraints = Or(constraints, c[i] != m.evaluate(c[i]))
#   s.add(constraints)
# #   s.add(Or(constraints, x!=m[x]))

# #   s.add()

# # exit()
# i = 0
# print("Iteration", i )
# # valid(Implies(F, W))
# # exit()
# while(not valid(Implies(F, W))):
#     temp = W
#     #Substitute current variables with post variables
#     W = substitute(W, (x, x__), (c, c__))

#     #Macros become useless here as substitute W directly here. See some form of dynamic function assignment and then calling like guarantee() = return W. Update in this line. else unnecessary formula repetition

#     wpAssertion = Exists([x_, c_], And(controller(x,x_), Succ(c,x,c_), guarantee(x_,c_), ForAll([x__, c__], Implies(And(environment(x_,x__), Succ(c_,x_,c__)), W))))

#     # for_part = Or(ForAll([x__, c__], Implies(And(environment(x_,x__), succ(c_,sigma[0],c__), Not(And(x>=0, x<=2)) ), W)), 
#     #     ForAll([x__, c__], Implies(And(environment(x_,x__), succ(c_,sigma[1],c__), And(x>=0, x<=2) ), W)))

#     # wpAssertion = Exists([x_, c_], And(controller(x,x_), Succ(c,x,c_), guarantee(x_,c_), for_part))

#     g = Goal()
#     g.add(wpAssertion)
#     wp = tactic_qe_fixpoint(g).as_expr()
#     W = And(wp, guarantee(x, c))
#     # print(get_vars(W))
#     print("W ", i)
#     # print toSMT2Benchmark(W, logic="LRA")
#     F = temp
#     i=i+1
#     print("Iteration ", i )

# print("")
# print("Number of times WP computed: ", i+1)
# print("")

# if not satisfiable(F):
#     print("Invariant is Unsatisifiable i.e. False")
#     print("UNREALIZABLE")
# else:
#     print("Invariant is Satisfiable")
#     print("REALIZABLE")
#     g = Goal()
#     g.add(F)
#     F = tactic_qe_fixpoint(g).as_expr()
#     print("Invariant is: ")
#     print(F)
#     g = Goal()
#     g.add(Exists([c], F))
#     PF = tactic_qe_fixpoint(g).as_expr()
#     print("Projected invariant is: ")
#     print(PF)

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


# a = Array('a', IntSort(), IntSort())
# a_ = Array('a_', IntSort(), IntSort())
# x = Int('x')
# i = Int('i')

# lhs = ForAll([x], Implies(x<i, a[x] == 0))
# update = a_ == Store(a, i, 0)
# rhs = ForAll([x], Implies(x<=i+1, a_[x] == 0))
# practice_array_formula = Implies(And(lhs, update), rhs)

# valid(practice_array_formula)

# s = Solver()
# s.add(practice_array_formula)
# s.add(lhs)
# s.check()

# m = s.model()
# print(m)
# print(m.decls())


