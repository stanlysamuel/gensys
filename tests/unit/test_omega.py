from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Test case for 2 floor elevator automaton with k = 2

k = 2
nQ = 5
def automaton(q, q_, x):
    return Or(
            And(q == 0, q_==0, And(x>=1, x<=2)),
            And(q == 0, q_==1, Not(And(x>=1, x<=2))),
            And(q == 1, q_==1),
            And(q == 0, q_==2, And(x>=1, x<=2, x!=1)),
            And(q == 2, q_==2, x!=1),
            And(q == 2, q_==4, x==1),
            And(q == 0, q_==3, And(x>=1, x<=2, x!=2)),
            And(q == 3, q_==3, x!=2),
            And(q == 3, q_==4, x==2),
            And(q == 4, q_==4)
            )

def isFinal(p):
    return If(And(p <=3, p >=1), 1, 0)

c = IntVector('c', nQ)
c_ = IntVector('c_', nQ)

x = Int('x')
sigma = [x == 1, x == 2, Not(And(x>=1, x<=2))]
state=[]
state.append(x)

def omega_function(c_post, sigma):
    formula = omega(c_, sigma, c, k, automaton, isFinal, state)
    s = Solver()
    s.add(formula)
    # s.add(And(c_[0]==0, c_[1]==-1, c_[2]==-1, c_[3]==1, c_[4]==1))
    for i in range(len(c_post)):
        s.add(c_[c_post[i][0]] == c_post[i][1])
    # This code prints the free variables i,e. c and c_
    state_model = []
    c_list = []
    while s.check() == sat:
        m = s.model()
        # print(m)
        # print("q : {}".format(m[q]))

        # print("c_:")
        # c_list = []
        # for i in range(nQ):
        #     c_list.append((i, m.evaluate(c_[i])))
        # c_list.sort()
        # print(c_list)

        c_list = []
        print("c:")
        for i in range(nQ):
            c_list.append((i, m.evaluate(c[i])))
        c_list.sort()
        print(c_list)

        print("")
        # state_model.append((m[q].as_long(), m[c_].eval(c_(q))))
        # models.append(s.model()[q])
        # s.add(Or(q != m[q], c_(q) != m.evaluate(c_(q))))

        # This code blocks an entire valuation of a function, for i values.
        constraints = Or(False)
        for i in range(nQ):
            constraints = Or(constraints, c[i] != m.evaluate(c[i]))
        s.add(constraints)
    return c_list

def test_1():
    assert omega_function([(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)], x == 1) == [(0, 0), (1, -1), (2, 1), (3, 0), (4, 1)]
def test_2():
    assert omega_function([(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)], x == 2) == [(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)]
def test_3():
    assert omega_function([(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)], Not(And(x>=1, x<=2))) == [(0, -1), (1, -1), (2, -1), (3, 0), (4, 1)]

def test_4():
    assert omega_function([(0, 0), (1, -1), (2, 1), (3, -1), (4, 1)], x == 1) == [(0, 0), (1, -1), (2, 1), (3, -1), (4, 1)]
def test_5():
    assert omega_function([(0, 0), (1, -1), (2, 1), (3, -1), (4, 1)], x == 2) == [(0, 0), (1, -1), (2, 0), (3, 1), (4, 1)]
def test_6():
    assert omega_function([(0, 0), (1, -1), (2, 1), (3, -1), (4, 1)], Not(And(x>=1, x<=2))) == [(0, -1), (1, -1), (2, 0), (3, -1), (4, 1)]

def test_7_bot():
    assert omega_function([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)], x == 1) == [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)]
def test_8_bot():
    assert omega_function([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)], x == 2) == [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)]
def test_9_bot():
    assert omega_function([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)], Not(And(x>=1, x<=2))) == [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)]

def test_10_top():
    assert omega_function([(0, k), (1, k), (2, k), (3, k), (4, k)], x == 1) == [(0, 1), (1, 1), (2, 2), (3, 1), (4, 2)]
def test_11_top():
    assert omega_function([(0, k), (1, k), (2, k), (3, k), (4, k)], x == 2) == [(0, 1), (1, 1), (2, 1), (3, 2), (4, 2)]
def test_12_top():
    assert omega_function([(0, k), (1, k), (2, k), (3, k), (4, k)], Not(And(x>=1, x<=2))) == [(0, 1), (1, 1), (2, 1), (3, 1), (4, 2)]