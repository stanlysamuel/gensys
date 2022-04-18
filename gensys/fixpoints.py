
#  GenSys v0.1

#  Copyright (C) 2021 Stanly Samuel

#  This software is available under the MIT license. Please see LICENSE in the
#  top-level directory for details.

#  This file is part of gensys.

 
from  gensys.helper import *
from z3 import *
#-------------------------------------------------------------------#
#Initialize the three tactics required for the tool. Assume user cannot control them now
#-------------------------------------------------------------------#
# Tactics for fixedpoint algorithm
# tactic_qe_fixpoint = Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Then(Tactic('qe2'), Tactic('simplify'))
tactic_qe_fixpoint = Tactic('qe2')

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