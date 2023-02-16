from z3 import *

# Util functions

def min(x,y):
    return If(x < y, x, y)

def isFinal(p):
    return If(And(p <=4, p >=1), 1, 0)

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

x = Int('x')
sigma = [x == 1, x == 2, x == 3, Not(And(x>=1, x<=3))]

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

c = Function('c', IntSort(), IntSort())
c_ = Function('c_', IntSort(), IntSort())

s = Solver()

# 1. Range Constraints

range_c = And(c(q) >= -1, c(q) <= 2)
range_c_ = And(c_(q) >= -1, c_(q) <= 2)

range_q = And(q>=0, q<=5) #gets finite models

# Test 1
# s.add(And(c(0)==0, c(1)==-1, c(2)==-1, c(3)==1, c(4)==1, c(5)==-1))

# Test 2
# s.add(And(c(0)==-1, c(1)==1, c(2)==-1, c(3)==-1, c(4)==-1, c(5)==-1))

# Test 3
# s.add(And(c(0)==0, c(1)==-1, c(2)==1, c(3)==-1, c(4)==2, c(5)==1))

# Test 4: Backward direction
s.add(And(c_(0)==0, c_(1)==-1, c_(2)==1, c_(3)==-1, c_(4)==2, c_(5)==1))

# 2. Reachability constraint
p = Int('p')
# Target state number is reachable iff ( exists some transition to it on some input)
# One direction is enough. The other is implied from the determinization constraint
reach = Implies(c_(q) != -1, Exists([p,x], And(automaton(p,q,x), x==2, c(p) != -1)))

# 3. Determinization constraint

# Gives lower bound on valid states (not enough)
# s.add(ForAll([p, x], Implies(And(automaton(p,q,x), x==2, c(p) != -1), c_(q) >= min(c(p) + isFinal(q) , 2) )))

p_ = Int('p_')

# This constraint gives the count on valid target states that has >1 input states.
det1 = ForAll([p,p_,x], Implies(And(automaton(p,q,x), x==2, c(p) != -1, automaton(p_,q,x), x==2, c(p_) <= c(p), c(p_) != -1, p!=p_), c_(q) == min(c(p) + isFinal(q) , 2)))

# This constraint gives the count on valid target states that has 1 input state.
det2 = ForAll([p,x], Implies(And(automaton(p,q,x), x==2, c(p) != -1, Not(Exists([p_], And(automaton(p_,q,x), x==2, c(p_) != -1, p!=p_)))), c_(q) == min(c(p) + isFinal(q) , 2)))

s.add(ForAll([q], Implies(range_q, And(range_c, range_c_, reach, det1, det2))))
# s.add(Exists([c_], ForAll([q], Implies(range_q, And(range_c, range_c_, reach, det1, det2)))))
# s.add(And(q==2, c_(q) == 2))
# s.add(q==1)

# This code prints the free variables i,e. c and c_
state_model = []
while s.check() == sat:
  m = s.model()
  # print(m)
  # print("q : {}".format(m[q]))

  print("c_:")
  c_list = []
  for i in range(6):
    c_list.append((i, m.evaluate(c_(i))))
  c_list.sort()
  print(c_list)

  print("c:")
  c_list = []
  for i in range(6):
    c_list.append((i, m.evaluate(c(i))))
  c_list.sort()
  print(c_list)

  print("")
  # state_model.append((m[q].as_long(), m[c_].eval(c_(q))))
  # models.append(s.model()[q])
  # s.add(Or(q != m[q], c_(q) != m.evaluate(c_(q))))

  # This code blocks an entire valuation of an uninterpreted function, for i values.
  constraints = Or(False)
  for i in range(6):
    constraints = Or(constraints, c(i) != m.evaluate(c(i)))
  s.add(constraints)
#   s.add(q != s.model()[q])

# state_model.sort() 
# print(state_model)