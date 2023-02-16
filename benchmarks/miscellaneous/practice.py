# from z3 import *

# state = Int('state')
# state_d = Function('state_d', IntSort(), IntSort())
# s = Solver()
# s.add(state>=1, state<=4, state_d(state)>=-1, state_d(state)<=0)
# s.check()

# z3.set_param('model.compact', True)

# print(s.model())
# print(s.model()[state_d])

# while s.check() == sat:
#   print(s.model())
#   s.add(Or(state_d != s.model()[state_d]))

from ast import For
from rsa import PublicKey
from z3 import *

x = Int('x')
s = Solver()
s.add(x>=0, x<=3)
s.check()

# print(s.model())
# print(s.model()[x])

while s.check() == sat:
  print(s.model())
  s.add(Or(x != s.model()[x]))


i_0 = Bool('i_0')
i_1 = Bool('i_1')

lhs = Exists([i_1], Or(i_0, i_1))
rhs = Or(i_0, False)
s = Solver()
s.add(lhs == rhs)
s.check()

# print(s.model())
# print(s.model()[x])

while s.check() == sat:
  print(s.model())
  s.add(Or(i_0 != s.model()[i_0]))

p = Bool('p')
q = Bool('q')

bf = And(p,q)

tactic = Tactic('aig')

g = Goal()
g.add(bf)
t = tactic(g).as_expr()
print(t)
print(bf.sexpr())

x = Int('x')
x_ = Int('x_')
c = Int('c')
c_ = Int('c_')

tactic = Then(Tactic('qe2'),Repeat(Tactic('ctx-simplify')))
# F = ForAll(x_, Implies(Or(x_ == x + 1, x_ == x + 5), x_>=5))
# F = Or(ForAll(x_, Implies(x_ == x + 1, x_>=5)), ForAll(x_, Implies(x_ == x + 5, x_>=5))) 
# F = ForAll(x_, Implies(Or(And(x == 1, x_ == x + 1), And(x>=0, x_ == x + 2)), x_>=5))
# F = ForAll(x_, Implies(Or(And(x < 0, x_ == x + 1), And(x>=0, x_ == x - 2)), x_==0))

# move1 = And(c==0,x==2,x_==x, c_==1)
# move2 = And(c==0,x==1,x_==x, c_==2)
# move3 = And(c==0,And(x!=2, x!=1),x_==x, c_==3)
# F = And(ForAll([x_,c_], Implies(Or(move1, move2, move3)), c_==3), c==0)

# move1 = And(c==0,x<0,x_==x+1, c_==1)
# move2 = And(c==0,x>=0,x_==x-2, c_==2)
# F = And(ForAll([x_,c_], Implies(Or(move1,move2), And( x_ == 0) ) ), c==0)

# move1 = And(c==0,x<0,Or(x_==x+1, x_==x-2), c_==1)
# move2 = And(c==0,x>=0,x_==x-2, c_==2)
# F = And(ForAll([x_,c_], Implies(Or(move1,move2), And(x_ == 0) ) ), c==0)

# move1 = And(c==0,x>0, x_==x+1, c_==2)
# move2 = And(c==1,x<=0,x_==x, c_==2)
# #Move 3 and 4 are needed for complete graphs else forall is unsound
# move3 = And(c==0,x<=0,c_==1)
# move4 = And(c==1,x>0,c_==0)
# F = And(ForAll([x_,c_], Implies(Or(move1,move2, move3, move4), And(c_ == 2,x_ == 0) ) ), c>=0, c<=1)

# F = Exists([x_,c_], Or(And(c==0,x==1,Or(x_==x+1, x_==x-1), c_==1, x_==2), And(c==2,x>=1,x<=3,Or(x_==x+1, x_==x-1), c_==1, x_==2)))

G = Or(And(c_==3, x_==2), And(c_==4, x_==0))
move1 = And(c==2, x==1,c_==3, Or(x_==x+1, x_==x-1))
move2 = And(c==2, x==1,c_==4, Or(x_==x+1))
F = Exists([x_,c_],And(Or(move1, move2), G) )

G = Or(And(c_==0, x_>=4, x_<=5), And(c_==1, x_>=3, x_<=4))
env = Or(x_==x, x_==x+1)
move1 = And(c==2, x==3,c_==0)
move2 = And(c==3, x==3,c_==1)
omega = Or(move1, move2)

# This is wrong
# F = Exists(x_, Exists(c_, And(omega, env, G)))

F = Exists(c_, And(omega, ForAll(x_, Implies(env, G))))

g = Goal()
g.add(F)
t = tactic(g).as_expr()
print(t)

prove(t == Or(And(c==2,  Or(x==1, x==3)), And(c==0,  x==1)))


# Factorization
# pubkey = product of two primes
x, y = Ints("x y")
pubkey = 3 * 7
solve(x * y == pubkey, x>1, y>1)

# x, y = Ints("x y")
# pubkey = 1000000993 * 1000001011
# solve(x * y == pubkey, x>1, y>1)

p, q = Bools("p q")
prove(Implies(And(p,q), Not(Or(Not(p), Not(q)))))

#Sum of 2 consecutive integers is odd

k, s = Ints("k s")

prove(Implies(And(x==y+1, s == x+y), Exists(k, s == 2*k + 1)))

# Proof that induction is true.
# Z3 cannot solve inductive proofs in general. Can take a bound though.
# threshold for eager quantifier instantiation
# set_option(eager_threshold=100)
statement = Function('statement', IntSort(), BoolSort())
n = Int("n")
base_case = statement(0)
induction_step = ForAll(n, Implies(And(n>=0, n<=10), Implies(statement(n), statement(n+1))))
conclusion = ForAll(n, Implies(And(n>=0, n<=10), statement(n)))

prove(Implies(And(base_case, induction_step), conclusion))
