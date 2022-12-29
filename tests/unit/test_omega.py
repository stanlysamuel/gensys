from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

def test_omega():
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
    formula = omega(c_, sigma[0], c, k, automaton, isFinal, state)

    s = Solver()
    s.add(formula)
    # Test 1
    # s.add(And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==1, c[4]==1))

    # Test 2
    # s.add(And(c(0)==-1, c(1)==1, c(2)==-1, c(3)==-1, c(4)==-1, c(5)==-1))

    # Test 3
    # s.add(And(c(0)==0, c(1)==-1, c(2)==1, c(3)==-1, c(4)==2, c(5)==1))

    # Test 4: Backward direction
    # s.add(And(c_(0)==0, c_(1)==0, c_(2)==2, c_(3)==0, c_(4)==2))
    s.add(And(c_[0]==0, c_[1]==-1, c_[2]==-1, c_[3]==1, c_[4]==1))
    # This code prints the free variables i,e. c and c_
    state_model = []
    c_list = []
    while s.check() == sat:
        m = s.model()
        # print(m)
        # print("q : {}".format(m[q]))

        print("c_:")
        c_list = []
        for i in range(nQ):
            c_list.append((i, m.evaluate(c_[i])))
        c_list.sort()
        print(c_list)

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

    result = [(0, 0), (1, -1), (2, 1), (3, 0), (4, 1)]
    assert c_list == result
    # assert 5 == 5