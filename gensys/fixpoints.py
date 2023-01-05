
#  GenSys v0.1

#  Copyright (C) 2021 Stanly Samuel

#  This software is available under the MIT license. Please see LICENSE in the
#  top-level directory for details.

#  This file is part of gensys.


from os import W_OK
from pkgutil import ImpLoader
from  gensys.helper import *
from z3 import *
#-------------------------------------------------------------------#
#Initialize the three tactics required for the tool. Assume user cannot control them now
#-------------------------------------------------------------------#
# Tactics for fixedpoint algorithm
tactic_qe_fixpoint = Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe2'), Tactic('simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe2'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Tactic('qe2')

#Controller Extraction: Use same tactic as fixpoint and use ctx-solver-simplify to make the controller readable.
tactic_qe_controller = tactic_qe_fixpoint
tactic_simplification = Repeat('ctx-solver-simplify')
# tactic_simplification = Repeat('simplify')

#-------------------------------------------------------------------#

#Options for printing in Z3
set_option(max_depth=100000, rational_to_decimal = True, precision =40, max_lines=10000)

# Safety Fixed-Point Procedure:

def safety_fixedpoint(controller_moves, environment, guarantee, mode):
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

    # Decide formulation based on game mode
    # Declare and define transition variables list for controller and environment, depending on the mode
    if(mode == 1):
        getFormulation = getFormulationAE
        contransitionVars = s_+s__
        envtransitionVars = s+s_
    else: 
        if(mode == 0):
            getFormulation = getFormulationEA
            envtransitionVars = s_+s__
            contransitionVars = s+s_
        else:
            print("Wrong mode entered. Please enter 1 (for AE mode) and 0 (for EA mode) as the second argument.")
            return
    

    #0. Create Controller
    # See if List Comprehension (or some better way can make it a single Or formula)
    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    #1. Game Formulation

    #Get AE/EA Formula with postcondition guarantee(*s__)
    wpAssertion = getFormulation(s_, s__, controller, environment(*envtransitionVars), guarantee(*s_), guarantee(*s__))

    #2. Fixed Point Computation

    #Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]

    g =Goal()
    g.add(wpAssertion)
    wp = tactic_qe_fixpoint(g).as_expr()
    W = And(wp, guarantee(*s))
    F = guarantee(*s)
    i = 0
    print("Iteration", i )
    while(not valid(Implies(F, W),0)):
    # while(not valid(F == W)): gives same as above so => holds one way
        #Backup for F
        temp = W
        #Substitute current variables with post variables
        W = substitute(W, *substList)

        #Get AE/EA Formula with postcondition W
        wpAssertion = getFormulation(s_, s__, controller, environment(*envtransitionVars), guarantee(*s_), W)

        g = Goal()
        g.add(wpAssertion)
        wp = tactic_qe_fixpoint(g).as_expr()
        W = And(wp, guarantee(*s))
        F = temp
        i=i+1
        print("Iteration ", i )

    print("")
    print("Number of times projection is done: ", i+1)
    print("")
    print("Invariant is")
    print(F)
    #3. Output: Controller Extraction or Unrealizable
    if not satisfiable(F,0):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")
        print("EXTRACTING CONTROLLER...")
        # In the invariant, substitute with post varaibles
        #Take backup of invariant to analyse in the end
        Invariant = F
        F = substitute(F, *substList)

        disjunction_of_conditions = False
        i = 0
        for move_i in controller_moves:
            i = i + 1

            #Get AE/EA Formula with postcondition F
            condition_move_i = getFormulation(s_, s__, move_i(*contransitionVars), environment(*envtransitionVars), guarantee(*s_), F)

            #Move i condition extraction
            #Eliminate quantifiers and simplify to get the conditions for each move
            g = Goal()
            g.add(condition_move_i)
            #Eliminate qe and conjunct with guarantee
            condition_move_i = And(tactic_qe_controller(g).as_expr(), guarantee(*s))
            g = Goal()
            g.add(condition_move_i)
            #Simplify to get final condition
            condition_move_i = tactic_simplification(g).as_expr()

            #Print condition for each python function provided in the controller
            print("\nCondition for the controller action: "+ str(move_i.__name__))
            print(condition_move_i)

            #For final sanity check
            disjunction_of_conditions = Or(condition_move_i, disjunction_of_conditions)

        #Sanity check: Disjunction of controller conditions is equal to Invariant
        formula = disjunction_of_conditions == Invariant

        valid(formula,0)

#Formulation for the game where envrionment plays first
def getFormulationAE(s_, s__, controller_moves, environment_moves, guarantee_s_, postcondition):
    
    #1. Create the E Formula in the AE formulation
    ExistsFormula = Exists(s__, And(controller_moves, postcondition))

    #2. Project E-Formula
    g =Goal()
    g.add(ExistsFormula)
    ExistsFormula = tactic_qe_fixpoint(g).as_expr()

    #3. Use Projected E-Formula in AE formulation
    return ForAll(s_,Implies(environment_moves ,And(guarantee_s_, ExistsFormula)))

#Formulation for the game where controller plays first
def getFormulationEA(s_, s__, controller_moves, environment_moves, guarantee_s_, postcondition):
    return Exists(s_, And(controller_moves, guarantee_s_, ForAll(s__, Implies(environment_moves, postcondition))))

# Omega Fixed-Point Procedure:

# Plug in sigma_x and c to get c_

# Define the k for which all fixedpoints (regular + antichain) is computed
k = 3

def min(x,y):
        return If(x < y, x, y)

def succ(c, sigma_x, c_, automaton, isFinal, s):

    # 1. Range Constraints

    range_c = And([And(c[q] >= -1, c[q] <= k+1) for q in range(0, len(c))])
    range_c_ = And([And(c_[q] >= -1, c_[q] <= k+1) for q in range(0, len(c))])

    # 2. Reachability constraint
    # Target state number is reachable iff ( exists some transition to it on some input)
    # One direction is enough. The other is implied from the determinization constraint
    
    # reach = And([Implies(c_[q] != -1,  Or([Exists(s, And(automaton(p,q,*s), sigma_x, c[p] != -1)) for p in range(0, len(c))])) for q in range(0, len(c_))])

    # # 3. Determinization constraint

    # # This constraint gives the count on valid target states that has >1 input states.
    # # det1 = And([And([And([ForAll(s, Implies(And(automaton(p,q,*s), sigma_x, c[p] != -1, automaton(p_,q,*s), sigma_x, c[p_] <= c[p], c[p_] != -1, p!=p_), c_[q] == min(c[p] + isFinal(q) , k+1))) for p_ in range(0, len(c))]) for p in range(0, len(c))]) for q in range(0, len(c_))])
    
    # det1 = And([And([And([Not(Exists(s, And(And(automaton(p,q,*s), sigma_x, c[p] != -1, automaton(p_,q,*s), sigma_x, c[p_] <= c[p], c[p_] != -1, p!=p_), c_[q] != min(c[p] + isFinal(q) , k+1)))) for p_ in range(0, len(c))]) for p in range(0, len(c))]) for q in range(0, len(c_))])
    
    
    # # This constraint gives the count on valid target states that has 1 input state.
    # # det2 = And([And([ForAll(s, Implies(And(automaton(p,q,*s), sigma_x, c[p] != -1, Not(Or([ And(automaton(p_,q,*s), sigma_x, c[p_] != -1, p!=p_) for p_ in range(0, len(c))]) )), c_[q] == min(c[p] + isFinal(q) , k+1))) for p in range(0, len(c))]) for q in range(0, len(c_))])
    
    # det2 = And([And([Not(Exists(s, And(And(automaton(p,q,*s), sigma_x, c[p] != -1, Not(Or([ And(automaton(p_,q,*s), sigma_x, c[p_] != -1, p!=p_) for p_ in range(0, len(c))]) )), c_[q] != min(c[p] + isFinal(q) , k+1)))) for p in range(0, len(c))]) for q in range(0, len(c_))])
    
    # return And(range_c, range_c_, reach, det1, det2)

    # det = ForAll([p,x], Implies(And(automaton(p,q,x), sigma_x, c(p) != -1), c_(q) >= min(c(p) + isFinal(q) , k) ))
    det = And([And([ForAll(s, Implies(And(automaton(p,q,*s), sigma_x, c[p] != -1), c_[q] >= min(c[p] + isFinal(q) , k) )) for p in range(0, len(c))]) for q in range(0, len(c_))])
    # unreach = Implies(c_(q) == -1, Not(Exists([p,x], And(automaton(p,q,x), sigma_x, c(p) != -1))))
    unreach = And([Implies(c_[q] == -1, Not( Or([Exists(s, And(automaton(p,q,*s), sigma_x, c[p] != -1)) for p in range(0, len(c))]) )) for q in range(0, len(c_))])
    # reach = Implies(c_(q) != -1, Exists([p,x], And(automaton(p,q,x), sigma_x, c_(q) == min(c(p) + isFinal(q) , k) )))
    reach = And([Implies(c_[q] != -1, Or([Exists(s, And(automaton(p,q,*s), sigma_x, c[p] != -1,  c_[q] == min(c[p] + isFinal(q) , k) )) for p in range(0, len(c))]) ) for q in range(0, len(c_))])

    return And(range_c, range_c_, det, unreach, reach)

def omega_fixedpoint(controller_moves, environment, guarantee, mode, automaton, isFinal, sigma, nQ):

    # Define Succ function for determinization (depends on succ (depends on min))

    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variable s in the code because it will get redeclared in this scope.
            exec(str(var) +"= Int('"+str(var) +"')") in globals(), locals()
            s.append(locals()[var])
    
    #Declare and define s'
    s_ = []
    for var in s:
        exec(str(var)+"_" +" = Int('"+str(var)+"_" +"')") in globals(), locals()
        s_.append(locals()[str(var)+"_"])

    #Declare and define s''
    s__ = []
    for var in s:
        exec(str(var)+"__" +" = Int('"+str(var)+"__" +"')") in globals(), locals()
        s__.append(locals()[str(var)+"__"])

    # Create determinized automaton state variables as IntVectors
    c = IntVector('c', nQ)
    c_ = IntVector('c_', nQ)
    c__ = IntVector('c__', nQ)

    def project(formula):
        g =Goal()
        g.add(formula)
        return tactic_qe_fixpoint(g).as_expr()

    # Retrive determinized predicate list
    sigma = sigma(*s)
    
    print("Projecting Succ to store")
    # Stores projected succ in a different array (indexed by the same index as sigma) so that project is not called always again and again.
    # This improves the speed by 2X
    projected_succ = [project(succ(c,sigma[i],c_, automaton, isFinal, s)) for i in range(len(sigma))]

    # print(projected_succ[1])
    # exit()
    def Succ(c_subst, x_subst, c__subst):
        #Project quantifers in Succ before forwarding to wpAssertion.
        return Or([And( substitute(sigma[i], [(s[j], x_subst[j]) for j in range(len(s))] ), substitute(projected_succ[i], [(c[j], c_subst[j]) for j in range(len(c))] + [(c_[j], c__subst[j]) for j in range(len(c_))] ) ) for i in range(len(sigma))])

    # Define the guarantee that we will use

    # Gurantee over the deterministic automaton states for a given k
    def guarantee_automaton(c):
        # Bounds on the range of the deterministic automaton states (functions)
        l_bound = And([c[q] >= -1 for q in range(0, len(c))])
        u_bound = And([c[q] < k+1 for q in range(0, len(c))])
        # Encoding for the bot element i.e., where all automaton state are mapped to -1
        bot = And([c[q] == -1 for q in range(0, len(c))])

        return And(l_bound, u_bound, Not(bot))

    # Combine above constraint with the optional safety guarantee, if any
    def guarantee_(s, c):
        return And(guarantee(*s), guarantee_automaton(c))

    # Utility function to check number of determinized automaton states in a given formula F(s,c)
    def print_automaton_states(formula):
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

        # Utility function to check number of determinized automaton states in a given formula F(s,c)
    def print_automaton_states_c_s(formula, c, state):
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
            model_formula = And(True)
            for i in range(nQ):
                model.append((i, m[c[i]]))
                model_formula = And(model_formula, c[i] == m.evaluate(c[i]))
            g =Goal()
            g.add(Exists(c, And(formula, model_formula)))
            s_pred = tactic_qe_fixpoint(g).as_expr()

            print(model, s_pred)
            # Block current model
            constraints = Or(False)
            for i in range(nQ):
                constraints = Or(constraints, c[i] != m.evaluate(c[i]))
            # constraints = Or(constraints, state[0] != m.evaluate(state[0]))
            s.add(constraints)
        # Print total number of states
        print("Number of states:", count)

    print("Getting Formulation")
    # Decide formulation based on game mode
    # Declare and define transition variables list for controller and environment, depending on the mode
    if(mode == 1):
        getFormulation = getFormulationAE_omega
        contransitionVars = s_+s__
        envtransitionVars = s+s_
    else: 
        if(mode == 0):
            getFormulation = getFormulationEA_omega
            envtransitionVars = s_+s__
            contransitionVars = s+s_
        else:
            print("Wrong mode entered. Please enter 1 (for AE mode) and 0 (for EA mode) as the second argument.")
            return
    

    print("Creating controller")
    #0. Create Controller
    # See if List Comprehension (or some better way can make it a single Or formula)
    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    #1. Game Formulation

    # Get AE/EA Formula with postcondition guarantee(*s__)
    wpAssertion = getFormulation(s, s_, s__, controller, environment(*envtransitionVars), guarantee_(s_,c_), guarantee_(s__,c__), Succ, c, c_, c__)
    
    #2. Fixed Point Computation

    #Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]

    i = 1
    print("Iteration", i )
    g =Goal()
    g.add(wpAssertion)
    print("Projecting wpAssertion")
    wp = tactic_qe_fixpoint(g).as_expr()
    print("Projected wpAssertion")
    i = i + 1

    # print(wp)
    print_automaton_states_c_s(wp,c,s)

    # wp = antichain_optimization(wp, c, c_, substList, k)

    # print(wp)
    # print_automaton_states(wp)


    # exit()
    
    W = And(wp, guarantee_(s, c))
    F = guarantee_(s, c)
    while(not valid(Implies(F, W),0)):
    # while(not valid(F == W)): gives same as above so => holds one way
        #Backup for F
        temp = W
        #Substitute current variables with post variables
        W = substitute(W, *substList+[(c[j], c__[j]) for j in range(nQ)])

        print("Iteration ", i )
        #Get AE/EA Formula with postcondition W
        print("Projecting wpAssertion")
        wpAssertion = getFormulation(s, s_, s__, controller, environment(*envtransitionVars), guarantee_(s_,c_), W, Succ, c, c_, c__)
        print("Projected wpAssertion")

        g = Goal()
        g.add(wpAssertion)
        wp = tactic_qe_fixpoint(g).as_expr()
        print_automaton_states_c_s(wp,c,s)
        # wp = antichain_optimization(wp, c, c_, substList, k)
        W = And(wp, guarantee_(s, c))
        F = temp
        i=i+1

    print("")
    print("Number of times projection is done: ", i-1)
    print("")
    print("Invariant is")
    print(F)
    
    #3. Output: Controller Extraction or Unrealizable
    # Create constraint for the initial state of the automaton. 
    # For example,
    # init = And(c[0]==0, c[1]==-1) for 2 states 
    # init = And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==-1, c[4]==-1, c[5]==-1) for 6 states 
    init = And(c[0] == 0, And([c[q] == -1 for q in range(1,nQ)]))

    if not satisfiable(And(F, init),0):
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
        print_automaton_states_c_s(F,c,s)
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
        # solve(PF)
        # print(succ(init, PF, c_))
        # solve(succ(init, PF, c_))

#Formulation for the game where envrionment plays first with omega specification
def getFormulationAE_omega(s, s_, s__, controller_moves, environment_moves, guarantee_s_c_, postcondition, Succ, c, c_, c__):
    
    #1. Create the E Formula in the AE formulation
    # ExistsFormula = Exists(s__, And(controller_moves, postcondition))
    ExistsFormula = Exists(s__+c__, And(controller_moves, Succ(c_,s_,c__), postcondition))

    #2. Project E-Formula
    g =Goal()
    g.add(ExistsFormula)
    ExistsFormula = tactic_qe_fixpoint(g).as_expr()

    #3. Use Projected E-Formula in AE formulation
    # return ForAll(s_+c_, Implies(And(environment_moves, Succ(c,s,c_)), And(guarantee_s_c_, Exists(s__+c__, And(controller_moves, Succ(c_,s_,c__), postcondition)))))
    return ForAll(s_+c_, Implies(And(environment_moves, Succ(c,s,c_)), And(guarantee_s_c_, ExistsFormula)))
    return ForAll(s_,Implies(environment_moves ,And(guarantee_s_, ExistsFormula)))

#Formulation for the game where controller plays first with omega specification
def getFormulationEA_omega(s, s_, s__, controller_moves, environment_moves, guarantee_s_c_, postcondition, Succ, c, c_, c__):

    # Projecting Forall first was not fast 
    # ForAllFormula = ForAll(s__+c__, Implies(And(environment_moves, Succ(c_,s_,c__)), postcondition))
    # #2. Project FA-Formula
    # g =Goal()
    # g.add(ForAllFormula)
    # ForAllFormula = tactic_qe_fixpoint(g).as_expr()
    # return Exists(s_+c_, And(controller_moves, Succ(c,s,c_), guarantee_s_c_, ForAllFormula))
    return Exists(s_+c_, And(controller_moves, Succ(c,s,c_), guarantee_s_c_, ForAll(s__+c__, Implies(And(environment_moves, Succ(c_,s_,c__)), postcondition))))
    return Exists(s_, And(controller_moves, guarantee_s_, ForAll(s__, Implies(environment_moves, postcondition))))


# Omega Fixed-Point Procedure with antichain optimization:

#Extract omega outside for unit testing

def max(x,y):
        return If(x > y, x, y)
        
# Plug in sigma_x and c_ to get c
def omega(c_, sigma_x, c, automaton, isFinal, s):

    # 1. Range Constraints

    range_c = And([And(c[q] >= -1, c[q] <= k+1) for q in range(0, len(c))])
    range_c_ = And([And(c_[q] >= -1, c_[q] <= k+1) for q in range(0, len(c))])

    # 2. Reachability constraint
    # Target state number is reachable iff ( exists some transition to it on some input)
    # One direction is enough. The other is implied from the determinization constraint
    
    # reach = And([Implies(c_[q] != -1,  Or([Exists(s, And(automaton(p,q,*s), sigma_x, c[p] != -1)) for p in range(0, len(c))])) for q in range(0, len(c_))])

    # 3. Determinization constraint

    # This constraint gives the count on valid target states that has >1 input states.
    # det1 = And([And([And([ForAll(s, Implies(And(automaton(p,q,*s), sigma_x, c[p] != -1, automaton(p_,q,*s), sigma_x, c[p_] <= c[p], c[p_] != -1, p!=p_), c_[q] == min(c[p] + isFinal(q) , k+1))) for p_ in range(0, len(c))]) for p in range(0, len(c))]) for q in range(0, len(c_))])
    
    # det1 = And([And([And([Not(Exists(s, And(And(automaton(p,q,*s), sigma_x, c[p] != -1, automaton(p_,q,*s), sigma_x, c[p_] <= c[p], c[p_] != -1, p!=p_), c_[q] != min(c[p] + isFinal(q) , k+1)))) for p_ in range(0, len(c))]) for p in range(0, len(c))]) for q in range(0, len(c_))])
    
    
    # This constraint gives the count on valid target states that has 1 input state.
    # det2 = And([And([ForAll(s, Implies(And(automaton(p,q,*s), sigma_x, c[p] != -1, Not(Or([ And(automaton(p_,q,*s), sigma_x, c[p_] != -1, p!=p_) for p_ in range(0, len(c))]) )), c_[q] == min(c[p] + isFinal(q) , k+1))) for p in range(0, len(c))]) for q in range(0, len(c_))])
    
    # det2 = And([And([Not(Exists(s, And(And(automaton(p,q,*s), sigma_x, c[p] != -1, Not(Or([ And(automaton(p_,q,*s), sigma_x, c[p_] != -1, p!=p_) for p_ in range(0, len(c))]) )), c_[q] != min(c[p] + isFinal(q) , k+1)))) for p in range(0, len(c))]) for q in range(0, len(c_))])
    
    # This constraint gives count for p where p -> q and p-> q'
    # det1 = ForAll([q,q_,s], Implies(And(automaton(p,q,*s), sigma_x, automaton(p,q_,*s), sigma_x, q!=q_, c_(q) - isFinal(q) <= c_(q_) - isFinal(q_) ), c(p) == max(c_(q) - isFinal(q) , -1) ) )
        
    # det1 = And([And([And([ForAll(s, Implies(And(automaton(p,q,*s), sigma_x, automaton(p,q_,*s), sigma_x, q!=q_, c_[q] - isFinal(q) <= c_[q_] - isFinal(q_) ), c[p] == max(c_[q] - isFinal(q) , -1) ) ) for q_ in range(0, len(c_))]) for q in range(0, len(c_))]) for p in range(0,len(c)) ])

    # This constraint gives count for p where p -> q
    # det2 = ForAll([q,s], Implies(And(automaton(p,q,*s), sigma_x, Not(Exists([q_], And(automaton(p,q_,*s), sigma_x, q!=q_)))), c(p) == max(c_(q) - isFinal(q) , -1) ))
    # det2 = And([And([ForAll(s, Implies(And(automaton(p,q,*s), sigma_x, Not( Or([And(automaton(p,q_,*s), sigma_x, q!=q_) for q_ in range(0,len(c_))]) ) ), c[p] == max(c_[q] - isFinal(q) , -1) )) for q in range(0, len(c_))]) for p in range(0,len(c))])

    # Quantifiers are only over game variables. Rest are blasted are the domain and range is finite (expensive)
    # return And( det1, det2)

    # det = ForAll([q,x], Implies(And(automaton(p,q,x), sig, c_(q) != -1), c(p) <= max(c_(q) - isFinal(q) , -1) ))
    det = And([And([ForAll(s, Implies(And(automaton(p,q, *s), sigma_x, c_[q] != -1), c[p] <= max(c_[q] - isFinal(q) , -1) )) for q in range(0, len(c_))]) for p in range(0, len(c)) ])
    # unreach = Implies(c(p) == -1, Not(Exists([q,x], And(automaton(p,q,x), sig, c_(q) != -1))))
    unreach = And([Implies(c[p] == -1, Not( Or([Exists(s, And(automaton(p,q,*s), sigma_x, c_[q] != -1)) for q in range(0, len(c_)) ]) )) for p in range(0, len(c))])
    # reach = Implies(c(p) != -1, Exists([q,x], And(automaton(p,q,x), sig, c(p) == max(c_(q) - isFinal(q) , -1) )))
    reach = And([Implies(c[p] != -1, Or([Exists(s, And(automaton(p,q,*s), sigma_x, c[p] == max(c_[q] - isFinal(q) , -1) )) for q in range(0, len(c_))]) ) for p in range(0, len(c))])

    # s.add(ForAll([p], Implies(range_p, And(det, reach, unreach))))

    # return And(range_c, range_c_, det1, det2)
    return And(range_c, range_c_, det, reach, unreach)

def omega_fixedpoint_antichain(controller_moves, environment, guarantee, mode, automaton, isFinal, sigma, nQ):

    # Define Omega function for determinization (depends on omega (depends on max))
    
    def project(formula):
        g =Goal()
        g.add(formula)
        return tactic_qe_fixpoint(g).as_expr()

    def glb(W, c, c_):
        # Input: W(c)
        # Ouput: G(c) representing the maximal states in W(v,c)
        # c_ represent the temporary variables to be replaced with.

        # Create W(c_)
        W_ = substitute(W, [(c[j], c_[j]) for j in range(len(c))])

        # Find all the lower bounds L(c) of W(c)
        L = ForAll(c_, Implies(W_, And([And(c[k] <= c_[k], c[k]>=-1) for k in range(0, len(c))])))
        L = project(L)

        # Create L(c_)
        L_ = substitute(L, [(c[j], c_[j]) for j in range(len(c))])

        # Find greatest lower bound G(c). It must exist.
        G = ForAll(c_, Implies(L_, And(L, And([c[k] >= c_[k] for k in range(0, len(c))]))))
        G = project(G)

        return G

    def maximal(W, v, v_, c, c_):
        # Input: W(v,c)
        # Ouput: M(v,c) representing the maximal states in W(v,c)
        # v_ and c_ represent the temporary variables to be replaced with.

        # Create a list for substitution of game states
        substList_vv_ = []
        for (var, var_) in zip(v,v_):
            substList_vv_ = substList_vv_+[(var,var_)]

        # Create W_ = W(v_,c_)
        W_ = substitute(W, *substList_vv_+[(c[j], c_[j]) for j in range(nQ)])

        # s_dominates(c,c') is the predicate that states that c' strictly dominates c.
        # s_dominates(c,c') := ForAll q. c[q] <= c_[q] and Exists q. c[q] < c_[q]

        # s_dominates(v, c, v', c') is the predicate that states that c' strictly dominates c and v == v'
        s_dominates = And(And([c[q] <= c_[q] for q in range(0, len(c))]), Or([c[q] < c_[q] for q in range(0, len(c))]), v == v_)

        # dominated(c) := Exists v. W(v,c) and W(v_,c_) and sDominates(c,c')
        dominated = Exists(v+v_+c_, And(W, W_, s_dominates))
        
        # Eliminate dominated states from W(v,c). This will also remove the corresponding predicate associated with the states.
        # maximal_states(v,c) = W(v,c) and !dominated(c)
        maximal_states = And(W, Not(dominated))

        # Project formula to get dominating 
        maximal_states = project(maximal_states)
        return maximal_states

    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variable s in the code because it will get redeclared in this scope.
            exec(str(var) +"= Int('"+str(var) +"')") in globals(), locals()
            s.append(locals()[var])
    
    #Declare and define s'
    s_ = []
    for var in s:
        exec(str(var)+"_" +" = Int('"+str(var)+"_" +"')") in globals(), locals()
        s_.append(locals()[str(var)+"_"])

    #Declare and define s''
    s__ = []
    for var in s:
        exec(str(var)+"__" +" = Int('"+str(var)+"__" +"')") in globals(), locals()
        s__.append(locals()[str(var)+"__"])

    # Create determinized automaton state variables as IntVectors
    c = IntVector('c', nQ)
    c_ = IntVector('c_', nQ)
    c__ = IntVector('c__', nQ)

    # Retrive determinized predicate list
    sigma = sigma(*s)
    
    print("Projecting Omega to store")
    # Stores projected omega in a different array (indexed by the same index as sigma) so that project is not called always again and again.
    # This improves the speed by 2X
    projected_omega = [project(omega(c_,sigma[i],c, automaton, isFinal, s)) for i in range(len(sigma))]

    # print(projected_succ[1])
    # exit()
    def Omega(c__subst, x_subst, c_subst):
        #Project quantifers in Omega before forwarding to wpAssertion.
        return Or([And( substitute(sigma[i], [(s[j], x_subst[j]) for j in range(len(s))] ), substitute(projected_omega[i], [(c[j], c_subst[j]) for j in range(len(c))] + [(c_[j], c__subst[j]) for j in range(len(c_))] ) ) for i in range(len(sigma))])

    # Define the guarantee that we will use

    # Gurantee over the deterministic automaton states for a given k, using antichains
    def guarantee_automaton_antichain(c):
        # Bounds on the range of the deterministic automaton states (functions)
        init = And([c[q] == k for q in range(0, len(c))])
        # init = And(c[0] == 1, c[1] == 1, c[2] == 1, c[3] == 1, c[4] == 2 )
        return And(init)

    # Combine above constraint with the optional safety guarantee, if any
    def guarantee_antichain_(s, c):
        return And(guarantee(*s), guarantee_automaton_antichain(c))

    # Utility function to check number of determinized automaton states in a given formula F(s,c)
    def print_automaton_states_c(formula, c):
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

    # Utility function to check number of determinized automaton states in a given formula F(s,c)
    def print_automaton_states_c_s(formula, c, state):
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
            model_formula = And(True)
            for i in range(nQ):
                model.append((i, m[c[i]]))
                model_formula = And(model_formula, c[i] == m.evaluate(c[i]))
            g =Goal()
            g.add(Exists(c, And(formula, model_formula)))
            s_pred = tactic_qe_fixpoint(g).as_expr()

            print(model, s_pred)
            # Block current model
            constraints = Or(False)
            for i in range(nQ):
                constraints = Or(constraints, c[i] != m.evaluate(c[i]))
            # constraints = Or(constraints, state[0] != m.evaluate(state[0]))
            s.add(constraints)
        # Print total number of states
        print("Number of states:", count)

    print("Getting Formulation")
    # Decide formulation based on game mode
    # Declare and define transition variables list for controller and environment, depending on the mode
    if(mode == 1):
        getFormulation = getFormulationAE_omega
        contransitionVars = s_+s__
        envtransitionVars = s+s_
    else: 
        if(mode == 0):
            getFormulation = getFormulationEA_omega
            envtransitionVars = s_+s__
            contransitionVars = s+s_
        else:
            print("Wrong mode entered. Please enter 1 (for AE mode) and 0 (for EA mode) as the second argument.")
            return
    
    #0. Create Controller
    # See if List Comprehension (or some better way can make it a single Or formula)
    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    #1. Game Formulation

    # Get AE/EA Formula with postcondition guarantee(*s__)
    # wpAssertion = getFormulation(s, s_, s__, controller, environment(*envtransitionVars), guarantee_(s_,c_), guarantee_(s__,c__), Succ, c, c_, c__)
        
    #2. Fixed Point Computation
    
    #Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]

    i = 0
    print("Iteration", i )
    
    #Decide more if ForAll needed and how the intersection is computed
    # envPre = Exists(s__, Exists(c__, And(Omega(c__, s_, c_), environment(*envtransitionVars), guarantee_antichain_(s__,c__))))
    envPre = Exists(c__, And(Omega(c__, s_, c_), ForAll(s__, Implies(environment(*envtransitionVars), guarantee_antichain_(s__,c__)))))
    #Project envPre(s_,c_) 
    g =Goal()
    g.add(envPre)
    conPost = tactic_qe_fixpoint(g).as_expr()
    # print(conPost)
    #Seems expensive and it also seems like glb is needed.
    # conPost = maximal(conPost,s_, s__, c_, c__)
    conPost = And(Exists(c_, conPost), glb(Exists(s_, conPost), c_, c__))
    # After removing non-maximal and after taking glb
    # conPost = And(And([c_[k] ==0 for k in range(0,5)]), c_[5] == 1, s_[0] >=1, s_[0] <=3)
    # print(conPost)
    # print_automaton_states_c(conPost, c_)
    print_automaton_states_c_s(conPost, c_, s_)
    # exit()

    # wp = Exists(s_, Exists(c_, And(Omega(c_, s, c), controller, conPost)))
    wp = Exists(s_+c_, And(Omega(c_, s, c), controller, conPost))
    # print(wp)
    g =Goal()
    g.add(wp)
    wp = tactic_qe_fixpoint(g).as_expr()
    # print(wp)
    wp = maximal(wp, s, s_, c, c_)
    # controller maximal solution
    print_automaton_states_c_s(wp, c, s)
    print(wp)
    # exit()
    W = wp
    F = guarantee_antichain_(s,c)

    i = i + 1
    print("Iteration", i )
    while(not valid(Implies(F, W),0)):
        temp = W
        W = substitute(W, *substList+[(c[j], c__[j]) for j in range(nQ)])

        #Decide more if ForAll needed and how the intersection is computed
        # envPre = Exists(s__, Exists(c__, And(Omega(c__, s_, c_), environment(*envtransitionVars), W)))

        envPre = Exists(c__, And(Omega(c__, s_, c_), ForAll(s__, Implies(environment(*envtransitionVars), guarantee_antichain_(s__,c__)))))
        #Project envPre(s_,c_) 
        g =Goal()
        g.add(envPre)
        conPost = tactic_qe_fixpoint(g).as_expr()
        # print(conPost)
        conPost = maximal(conPost,s_, s__, c_, c__)
        conPost = And(Exists(c_, conPost), glb(Exists(s_, conPost), c_, c__))
        # print_automaton_states_c(conPost, c_)
        print_automaton_states_c_s(conPost, c_, s_)

        wp = Exists(s_, Exists(c_, And(Omega(c_, s, c), controller, conPost)))
        g =Goal()
        g.add(wp)
        wp = tactic_qe_fixpoint(g).as_expr()
        # print(wp)
        wp = maximal(wp, s, s_, c, c_)
        # controller maximal solution
        # print_automaton_states_c(wp, c)
        print_automaton_states_c_s(wp, c, s)

        W = wp
        F = temp
        i = i + 1
        print("Iteration ", i )
    print("")
    print("Number of iterations: ", i+1)
    print("")
    print("Invariant is")
    print_automaton_states_c_s(F, c, s)
    # exit()

    # # Antichain Testing Zone STARTS

    # # Exists(s_+c_, And(controller_moves, Succ(c,s,c_), guarantee_s_c_, ForAll(s__+c__, Implies(And(environment_moves, Succ(c_,s_,c__)), postcondition))))

    # # wpAssertion = ForAll(s_+c_, Implies(And(environment(*envtransitionVars), Succ(c,s,c_)), guarantee_(s_,c_)))

    # # wpAssertion = And(ForAll(s_+c_, Implies(succ(c, sigma[0], c_), guarantee_(s_,c_))), guarantee_(s,c))
    # # wpAssertion = ForAll(s__+c__, Implies(And(environment(*envtransitionVars), omega(c__, sigma[0], c_)), guarantee_antichain_(s__,c__)))
    # # wpAssertion = ForAll(c__, Implies(Omega(c__,s_,c_), guarantee_antichain_(s__,c__)))
    # # wpAssertion = Exists(s__, Exists(c__, And(And(Omega(c__,s_,c_), environment(*envtransitionVars)), guarantee_antichain_(s__,c__))))
    # # wpAssertion = Exists(s__, Exists(c__, And(And(projected_omega[0], sigma[0], environment(*envtransitionVars)), guarantee_antichain_(s__,c__))))
    # # wpAssertion = Exists(c__, ForAll(s__, Implies(And(environment(*envtransitionVars),Omega(c__,s_,c_)), guarantee_antichain_(s__,c__))))

    # wpAssertion = Exists(s_, Exists(c_, And(Omega(c_, s, c), controller, guarantee_antichain_(s_,c_))))

    # g =Goal()
    # g.add(wpAssertion)
    # print("Projecting wpAssertion")
    # wp = tactic_qe_fixpoint(g).as_expr()
    # print(wp)
    # wp = keep_maximal(wp, c, c_, substList, k)
    # # controller maximal solution
    # print_automaton_states_c(wp, c)

    # wp = substitute(wp, *substList+[(c[j], c__[j]) for j in range(nQ)])

    # print(wp)

    # #Understand this. Why ForAll is not needed (if)
    # wpAssertion = Exists(s__, Exists(c__, And(Omega(c__, s_, c_), environment(*envtransitionVars), wp)))
    # wpAssertion_backup = Exists(s__, Exists(c__, And(Omega(c__, s_, c_), environment(*envtransitionVars), wp)))
    # #Here exists c_ takes care of which are the valid inputs to take. So take the union of them?

    # #Implement glb here
    # # wp = And(Exists(c_, wpAssertion), glb())

    # #Let's say glb gives this here:
    # wp = And(Exists(c_, wpAssertion), c_[0] == 0, c_[1] == 0, c_[2] == 0,c_[3] == 0,c_[4] == 2) 

    # wpAssertion = Exists(s_, Exists(c_, And(Omega(c_, s, c), controller, wp)))

    # g =Goal()
    # g.add(wpAssertion)
    # print("Projecting wpAssertion")
    # wp = tactic_qe_fixpoint(g).as_expr()
    # print(wp)
    # wp = keep_maximal(wp, c, c_, substList, k)
    # # controller maximal solution
    # print_automaton_states_c(wp, c)

    # wp = substitute(wp, *substList+[(c[j], c__[j]) for j in range(nQ)])

    # print(wp)

    # #Understand this. Why ForAll is not needed (if)
    # wpAssertion = Exists(s__, Exists(c__, And(Omega(c__, s_, c_), environment(*envtransitionVars), wp)))

    # # wp = substitute(wp, *substList+[(c[j], c__[j]) for j in range(nQ)])

    # # print(wp)
    # # wpAssertion1 = Exists(s_, Exists(c__, And(Omega(c__, s_, c_), Exists(s__, wp))))

    # # sigma_env_product = Or([And( substitute(sigma[i], [(s[j], s_[j]) for j in range(len(s))] ), environment(*envtransitionVars) ) for i in range(len(sigma))])

    # # wpAssertion2 = ForAll(s__, And( sigma_env_product, Exists(c__, wp)))
    # # wpAssertion = Exists(c_, wpAssertion)
    # # print(wpAssertion2)
    # g =Goal()
    # g.add(wpAssertion)
    # print("Projecting wpAssertion")
    # wp = tactic_qe_fixpoint(g).as_expr()
    # print(wp)
    # print_automaton_states_c(wp, c_)
    # prove(wpAssertion_backup == wp)

    # # Antichain Testing Zone ENDS
    # exit()

    # wpAssertion =Exists(s_+c_, And(controller, Succ(c,s,c_), wp ))

    # g =Goal()
    # g.add(wpAssertion)
    # print("Projecting wpAssertion")
    # wp = tactic_qe_fixpoint(g).as_expr()
    # print(wp)
    # wp = keep_maximal(wp, c, c_, substList, k)
    # print_automaton_states(wp)

    # # Antichain Testing Zone
    # exit()

    # g =Goal()
    # g.add(wpAssertion)
    # print("Projecting wpAssertion")
    # wp = tactic_qe_fixpoint(g).as_expr()

    # # print(wp)
    # # print_automaton_states(wp)

    # # wp = antichain_optimization(wp, c, c_, substList, k)

    # # print(wp)
    # # print_automaton_states(wp)


    # # exit()
    # print("Projected wpAssertion")
    # W = And(wp, guarantee_(s, c))
    # F = guarantee_(s, c)
    # i = 0
    # print("Iteration", i )
    # while(not valid(Implies(F, W),0)):
    # # while(not valid(F == W)): gives same as above so => holds one way
    #     #Backup for F
    #     temp = W
    #     #Substitute current variables with post variables
    #     W = substitute(W, *substList+[(c[j], c__[j]) for j in range(nQ)])

    #     #Get AE/EA Formula with postcondition W
    #     wpAssertion = getFormulation(s, s_, s__, controller, environment(*envtransitionVars), guarantee_(s_,c_), W, Succ, c, c_, c__)

    #     g = Goal()
    #     g.add(wpAssertion)
    #     wp = tactic_qe_fixpoint(g).as_expr()
    #     # wp = antichain_optimization(wp, c, c_, substList, k)
    #     W = And(wp, guarantee_(s, c))
    #     F = temp
    #     i=i+1
    #     print("Iteration ", i )

    # print("")
    # print("Number of times projection is done: ", i+1)
    # print("")
    # print("Invariant is")
    # print(F)
    
    #3. Output: Controller Extraction or Unrealizable
    # Create constraint for the initial state of the automaton. 
    # For example,
    # init = And(c[0]==0, c[1]==-1) for 2 states 
    # init = And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==-1, c[4]==-1, c[5]==-1) for 6 states 
    # init = And(c[0] == 0, And([c[q] >= -1 for q in range(1,nQ)]))

    # exit()
    start_val = Int('start_val')
    init = Exists(start_val, c[0]==0)

    if not satisfiable(And(F, init),0):
    # if not satisfiable(And(F),0):
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
        # print_automaton_states(F)
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
        # solve(PF)
        # print(succ(init, PF, c_))
        # solve(succ(init, PF, c_))