from  gensys.helper import *
from  gensys.fixpoints import *
from z3 import *

# Test case for 2 floor elevator automaton with k = 2

class TestOmegaElevator2Floor:
    k = 2
    nQ = 5
    def automaton(self, q, q_, x):
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

    def isFinal(self,p):
        return If(And(p <=3, p >=1), 1, 0)

    c = IntVector('c', nQ)
    c_ = IntVector('c_', nQ)

    x = Int('x')
    sigma = [x == 1, x == 2, Not(And(x>=1, x<=2))]
    state=[]
    state.append(x)

    def omega_function(self, c_post, sigma):
        formula = omega(self.c_, sigma, self.c, self.automaton, self.isFinal, self.state)
        s = Solver()
        s.add(formula)
        # s.add(And(c_[0]==0, c_[1]==-1, c_[2]==-1, c_[3]==1, c_[4]==1))
        for i in range(len(c_post)):
            s.add(self.c_[c_post[i][0]] == c_post[i][1])
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
            for i in range(self.nQ):
                c_list.append((i, m.evaluate(self.c[i])))
            c_list.sort()
            print(c_list)

            print("")
            # state_model.append((m[q].as_long(), m[c_].eval(c_(q))))
            # models.append(s.model()[q])
            # s.add(Or(q != m[q], c_(q) != m.evaluate(c_(q))))

            # This code blocks an entire valuation of a function, for i values.
            constraints = Or(False)
            for i in range(self.nQ):
                constraints = Or(constraints, self.c[i] != m.evaluate(self.c[i]))
            s.add(constraints)
        return c_list

    def test_1(self):
        assert self.omega_function([(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)], self.x == 1) == [(0, 0), (1, -1), (2, 1), (3, 0), (4, 1)]
    def test_2(self):
        assert self.omega_function([(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)], self.x == 2) == [(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)]
    def test_3(self):
        assert self.omega_function([(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)], Not(And(self.x>=1, self.x<=2))) == [(0, -1), (1, -1), (2, -1), (3, 0), (4, 1)]

    def test_4(self):
        assert self.omega_function([(0, 0), (1, -1), (2, 1), (3, -1), (4, 1)], self.x == 1) == [(0, 0), (1, -1), (2, 1), (3, -1), (4, 1)]
    def test_5(self):
        assert self.omega_function([(0, 0), (1, -1), (2, 1), (3, -1), (4, 1)], self.x == 2) == [(0, 0), (1, -1), (2, 0), (3, 1), (4, 1)]
    def test_6(self):
        assert self.omega_function([(0, 0), (1, -1), (2, 1), (3, -1), (4, 1)], Not(And(self.x>=1, self.x<=2))) == [(0, -1), (1, -1), (2, 0), (3, -1), (4, 1)]

    def test_7_bot(self):
        assert self.omega_function([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)], self.x == 1) == [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)]
    def test_8_bot(self):
        assert self.omega_function([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)], self.x == 2) == [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)]
    def test_9_bot(self):
        assert self.omega_function([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)], Not(And(self.x>=1, self.x<=2))) == [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)]

    def test_10_top(self):
        assert self.omega_function([(0, self.k), (1, self.k), (2, self.k), (3, self.k), (4, self.k)], self.x == 1) == [(0, 1), (1, 1), (2, 2), (3, 1), (4, 2)]
    def test_11_top(self):
        assert self.omega_function([(0, self.k), (1, self.k), (2, self.k), (3, self.k), (4, self.k)], self.x == 2) == [(0, 1), (1, 1), (2, 1), (3, 2), (4, 2)]
    def test_12_top(self):
        assert self.omega_function([(0, self.k), (1, self.k), (2, self.k), (3, self.k), (4, self.k)], Not(And(self.x>=1, self.x<=2))) == [(0, 1), (1, 1), (2, 1), (3, 1), (4, 2)]

    def test_12_top(self):
        assert self.omega_function([(0, 0), (1, 0), (2, 0), (3, 0), (4, 1)], self.x == 1) == [(0, -1), (1, -1), (2, 1), (3, -1), (4, 1)]


# Test case for 3 floor elevator automaton with k = 2

class TestOmegaElevator3Floor:
    k = 3
    nQ = 6
    def automaton(self, q, q_, x):
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

    def isFinal(self, p):
        return If(And(p <=4, p >=1), 1, 0)

    c = IntVector('c', nQ)
    c_ = IntVector('c_', nQ)

    x = Int('x')
    sigma = [x == 1, x == 2, x == 3, Not(And(x>=1, x<=3))]
    state=[]
    state.append(x)

    def omega_function(self, c_post, sigma):
        formula = omega(self.c_, sigma, self.c, self.automaton, self.isFinal, self.state)
        s = Solver()
        s.add(formula)
        # s.add(And(c_[0]==0, c_[1]==-1, c_[2]==-1, c_[3]==1, c_[4]==1))
        for i in range(len(c_post)):
            s.add(self.c_[c_post[i][0]] == c_post[i][1])
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
            for i in range(self.nQ):
                c_list.append((i, m.evaluate(self.c[i])))
            c_list.sort()
            print(c_list)

            print("")
            # state_model.append((m[q].as_long(), m[c_].eval(c_(q))))
            # models.append(s.model()[q])
            # s.add(Or(q != m[q], c_(q) != m.evaluate(c_(q))))

            # This code blocks an entire valuation of a function, for i values.
            constraints = Or(False)
            for i in range(self.nQ):
                constraints = Or(constraints, self.c[i] != m.evaluate(self.c[i]))
            s.add(constraints)
        return c_list

    def test_1(self):
        assert self.omega_function([(0, 0), (1, -1), (2, -1), (3, 2), (4, 3), (5,-1)], self.x == 1) == [(0, 0), (1, -1), (2, -1), (3, 1), (4, 2), (5, -1)]
    # def test_2(self):
    #     assert self.omega_function([(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)], self.x == 2) == [(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)]
    # def test_3(self):
    #     assert self.omega_function([(0, 0), (1, -1), (2, -1), (3, 1), (4, 1)], Not(And(self.x>=1, self.x<=2))) == [(0, -1), (1, -1), (2, -1), (3, 0), (4, 1)]

    # def test_4(self):
    #     assert self.omega_function([(0, -1), (1, -1), (2, 1), (3, 2), (4, 3), (5, -1)], self.x == 1) == [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, 3)]
    # def test_5(self):
    #     assert self.omega_function([(0, 0), (1, -1), (2, 1), (3, -1), (4, 1)], self.x == 2) == [(0, 0), (1, -1), (2, 0), (3, 1), (4, 1)]
    # def test_6(self):
    #     assert self.omega_function([(0, 0), (1, -1), (2, 1), (3, -1), (4, 1)], Not(And(self.x>=1, self.x<=2))) == [(0, -1), (1, -1), (2, 0), (3, -1), (4, 1)]

    # def test_7_bot(self):
    #     assert self.omega_function([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)], self.x == 1) == [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)]
    # def test_8_bot(self):
    #     assert self.omega_function([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)], self.x == 2) == [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)]
    # def test_9_bot(self):
    #     assert self.omega_function([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)], Not(And(self.x>=1, self.x<=2))) == [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1)]

    # def test_10_top(self):
    #     assert self.omega_function([(0, self.k), (1, self.k), (2, self.k), (3, self.k), (4, self.k)], self.x == 1) == [(0, 1), (1, 1), (2, 2), (3, 1), (4, 2)]
    # def test_11_top(self):
    #     assert self.omega_function([(0, self.k), (1, self.k), (2, self.k), (3, self.k), (4, self.k)], self.x == 2) == [(0, 1), (1, 1), (2, 1), (3, 2), (4, 2)]
    # def test_12_top(self):
    #     assert self.omega_function([(0, self.k), (1, self.k), (2, self.k), (3, self.k), (4, self.k)], Not(And(self.x>=1, self.x<=2))) == [(0, 1), (1, 1), (2, 1), (3, 1), (4, 2)]