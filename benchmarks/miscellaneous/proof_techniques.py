from z3 import *

# Factorization
# pubkey = product of two primes
x, y = Ints("x y") # These are mathematical integers (unbounded, unlike variables in C/C++ etc)
pubkey = 3 * 7
solve(x * y == pubkey, x>1, y>1)

# # Factorization (Intractability example)
# x, y = Ints("x y")
# pubkey = 1000000993 * 1000001011
# solve(x * y == pubkey, x>1, y>1)

# De Morgan's law
p, q = Bools("p q")
prove(Implies(And(p,q), Not(Or(Not(p), Not(q)))))

# Sum of 2 consecutive integers is odd

k, s = Ints("k s")
LHS = And(x==y+1, s == x+y)
RHS = Exists(k, s == 2*k + 1)
prove(Implies(LHS, RHS))

# Proof that induction is true.
# Z3 cannot solve inductive proofs in general (Deciding Validity of formulas in First Order Logic is undecidable in general).

# 1. 
# S(n) is a predicate declared as a function with signature Int -> Bool
statement = Function('statement', IntSort(), BoolSort())
n = Int("n")
# Base Case: S(0) is true 
base_case = statement(0)
# Induction Step: S(n) => S(n+1) , forall n>=0
induction_step = ForAll(n, Implies(n>=0, Implies(statement(n), statement(n+1))))
# Conclusion: S(n) is true, forall n>=0 
conclusion = ForAll(n, Implies(n>=0, statement(n)))
# Induction Correctness Theorem
induction_theorem = Implies(And(base_case, induction_step), conclusion)
prove(induction_theorem)

# 2. 
# Z3 cannot solve inductive proofs in general. Can take a bound though (In this case n ranges from 0 t0 10)
statement = Function('statement', IntSort(), BoolSort())
n = Int("n")
base_case = statement(0)
# Induction Step: S(n) => S(n+1) , forall 0<=n<=10
induction_step = ForAll(n, Implies(And(n>=0, n<=10), Implies(statement(n), statement(n+1))))
# Conclusion: S(n) is true , forall 0<=n<=10
conclusion = ForAll(n, Implies(And(n>=0, n<=10), statement(n)))
induction_theorem = Implies(And(base_case, induction_step), conclusion)
prove(induction_theorem)
