from z3 import *

# Util functions

def min(x,y):
    return If(x < y, x, y)

# def isFinal(p):
#     return If(And(p <=4, p >=1), 1, 0)

def isFinal(p):
    return If(p==1, 1, 0)

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

nQ = 2
def automaton(q, q_, x):
    return Or(
            And(q == 0, q_==1, Or(x<0, x>10)),
            And(q == 0, q_==0),
            And(q == 1, q_==1),
            )

x = Int('x')


# Code to get the output states from given state and input
q = Int('q')
q_ = Int('q_')
s = Solver()
# s.add(And(automaton(0,q_,x), Not(And(x>=1, x<=3))))
s.add(Exists([q,x], And(automaton(q,q_,x), x==2)))

models = []
while s.check() == sat:
  models.append(s.model()[q_])
  s.add(q_ != s.model()[q_])

# print(models)

# Determinization constraints using uninterpreted functions

c = Array('c', IntSort(), IntSort())
c_ = Array('c_', IntSort(), IntSort())

s = Solver()

# Test 1
# s.add(And(c(0)==0, c(1)==-1, c(2)==-1, c(3)==1, c(4)==1, c(5)==-1))

# Test 2
# s.add(And(c(0)==-1, c(1)==1, c(2)==-1, c(3)==-1, c(4)==-1, c(5)==-1))

# Test 3
# s.add(And(c(0)==0, c(1)==-1, c(2)==1, c(3)==-1, c(4)==2, c(5)==1))

# Test 4: Backward direction
# s.add(And(c_[0]==0, c_[1]==-1, c_[2]==1, c_[3]==-1, c_[4]==2, c_[5]==1))

k = 0

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

    return ForAll([q], Implies(range_q, And(range_c, range_c_, reach, det1, det2)))

# def succ(c, x, c_):
#     p = Int('p')
#     q = Int('q')

#     # 1. Range Constraints

#     range_q = And(q>=0, q< nQ) #gets finite models

#     range_c = And(c[q] >= -1, c[q] <= k+1)
#     range_c_ = And(c_[q] >= -1, c_[q] <= k+1)

#     # 2. Reachability constraint
#     # Target state number is reachable iff ( exists some transition to it on some input)
#     # One direction is enough. The other is implied from the determinization constraint
    
#     reach = Implies(c_[q] != -1, Exists([p,x], And(automaton(p,q,x), c[p] != -1)))

#     # 3. Determinization constraint
#     p_ = Int('p_')

#     # This constraint gives the count on valid target states that has >1 input states.
#     det1 = ForAll([p,p_,x], Implies(And(automaton(p,q,x), c[p] != -1, automaton(p_,q,x), c[p_] <= c[p], c[p_] != -1, p!=p_), c_[q] == min(c[p] + isFinal(q) , k+1)))

#     # This constraint gives the count on valid target states that has 1 input state.
#     det2 = ForAll([p,x], Implies(And(automaton(p,q,x), c[p] != -1, Not(Exists([p_], And(automaton(p_,q,x), c[p_] != -1, p!=p_)))), c_[q] == min(c[p] + isFinal(q) , k+1)))

#     return ForAll([q], Implies(range_q, And(range_c, range_c_, reach, det1, det2)))

# sigma = [x == 1, x == 2, x == 3, Not(And(x>=1, x<=3))]
sigma = [Not(And(x>=0, x<=10)), And(x>=0, x<=10)]
# sigma_x = sigma[1]
sigma_x = And(True)

s.add(c_[0]==0, c_[1]==1, succ(c, sigma_x, c_), sigma_x)



# This code prints the free variables i,e. c and c_
state_model = []
count1 = 0
while s.check() == sat:
  count1 +=1
  m = s.model()
  # print(m)
  # print("q : {}".format(m[q]))

  print("c_:")
  c_list = []
  for i in range(nQ):
    c_list.append((i, m.evaluate(c_[i])))
  c_list.sort()
  print(c_list)

  print("c:")
  c_list = []
  for i in range(nQ):
    c_list.append((i, m.evaluate(c[i])))
  c_list.sort()
  print(c_list)

  print("")
  # state_model.append((m[q].as_long(), m[c_].eval(c_(q))))
  # models.append(s.model()[q])
  # s.add(Or(q != m[q], c_(q) != m.evaluate(c_(q))))

  # This code blocks an entire valuation of an uninterpreted function, for i values.
  constraints = Or(False)
  for i in range(nQ):
    constraints = Or(constraints, c[i] != m.evaluate(c[i]))
  s.add(constraints)

print(count1)
#   s.add(q != s.model()[q])

# state_model.sort() 
# print(state_model)

# array_example = Exists([c_], And(c_[0]==0, c_[1]==-1, c_[2]==1, c_[3]==-1, c_[4]==2, c_[5]==1, ForAll([q], Implies(range_q, And(range_c, range_c_, reach, det1, det2)))))

# To verify projection. Verified

# array_example = Exists([c], And(cons, ForAll([q], Implies(range_q, And(range_c, range_c_, reach, det1, det2)))))

# tactic_qe_fixpoint = Tactic('qe') #C=2.0 and C=3.0 this works faster
# g =Goal()
# g.add(array_example)
# array_example_projected = tactic_qe_fixpoint(g).as_expr()
# print(array_example_projected)

# s = Solver()
# s.add(array_example_projected)

# count2 = 0
# while s.check() == sat:
#   count2 += 1
#   m = s.model()

#   print("c_:")
#   c_list = []
#   for i in range(nQ):
#     c_list.append((i, m.evaluate(c_[i])))
#   c_list.sort()
#   print(c_list)

#   print("")

#   # This code blocks an entire valuation of an uninterpreted function, for i values.
#   constraints = Or(False)
#   for i in range(nQ):
#     constraints = Or(constraints, c_[i] != m.evaluate(c_[i]))
#   s.add(constraints)
# print(count2)

# print(count1 == count2)
# print("Number of valuations before projection and after projection are the same. Thus, projection is giving the right values")