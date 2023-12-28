
#  GenSys v2.0

#  Copyright (C) 2023 Stanly Samuel

#  This software is available under the MIT license. Please see LICENSE in the
#  top-level directory for details.

#  This file is part of gensys.

#--------------------------------------------------------------------------------------------------------------------------------#
# GenSys-LTL: A tool for solving Logical LTL Games (Infinite-State Reactive Synthesis)
# Author: Stanly Samuel
# Date: 14/03/2023
# Description: This file contains 8 fixpoint procedures for temporal specifications of different types.
#
# 1. Fixpoint Procedures for Simple Games (where LTL formula is of the form: G(formula), F(formula), GF(formula), or FG(formula))
# 1.1. Safety Fixpoint Procedure
# 1.2. Reachability Fixpoint Procedure
# 1.3. Buchi Fixpoint Procedure
# 1.4. Co-Buchi Fixpoint Procedure
# 
# 2. Fixpoint Procedures for general LTL specifications
# 2.1. Product Games (Deterministic Automatons)
#   2.1.1 Product Buchi Fixpoint Procedure (Deterministic Buchi Automaton)
#   2.1.2 Product Co-Buchi Fixpoint Procedure (Deterministic Co-Buchi Automaton)
# 2.2. Bounded Fixpoint Procedures (Non deterministic Automatons)
#   2.2.1. On-The-Fly Determinization (OTFD) based Fixpoint Procedure
#   2.2.2. On-The-Fly Determinization (OTFD) based Fixpoint Procedure without Predicate Partitioning
#--------------------------------------------------------------------------------------------------------------------------------#

from  gensys.helper import *
from z3 import *
#-------------------------------------------------------------------------------------------------------------#
#Initialize the tactics required for the tool. User cannot control them in this version of the tool.
#-------------------------------------------------------------------------------------------------------------#

#Parallel Tactic
tactic_qe_fixpoint = Then(Tactic('skip') , ParOr(Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify')), Then(Tactic('qe2'), Tactic('simplify'))))

#Controller Extraction: Use same tactic as fixpoint and use ctx-solver-simplify to make the controller readable.
tactic_qe_controller = tactic_qe_fixpoint
tactic_simplification = Repeat('ctx-solver-simplify')
# tactic_simplification = Repeat('simplify')
#-------------------------------------------------------------------#

#Options for printing in Z3
set_option(max_depth=100000, rational_to_decimal = True, precision =40, max_lines=10000)
#Options for parallel processing in Z3
set_param("parallel.enable", True)
# set_param("parallel.threads.max", 5)

# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# 1. Fixpoint Procedures for Simple Games (where LTL formula is of the form: G(formula), F(formula), GF(formula), or FG(formula))
# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

# Formulation for the game where envrionment plays first (not used in this version of the tool)
def getFormulationAE(s_, s__, controller_moves, environment_moves, guarantee_s_, postcondition, game):
    if(game == "safety"):
        #1. Create the E Formula in the AE formulation
        ExistsFormula = Exists(s__, And(controller_moves, postcondition))

        #2. Project E-Formula
        g =Goal()
        g.add(ExistsFormula)
        ExistsFormula = tactic_qe_fixpoint(g).as_expr()

        #3. Use Projected E-Formula in AE formulation
        return ForAll(s_,Implies(environment_moves ,And(guarantee_s_, ExistsFormula)))
    else:
        if(game == "reachability"):
            #1. Create the E Formula in the AE formulation
            ExistsFormula = Exists(s__, And(controller_moves, postcondition))

            #2. Project E-Formula
            g =Goal()
            g.add(ExistsFormula)
            ExistsFormula = tactic_qe_fixpoint(g).as_expr()

            #3. Use Projected E-Formula in AE formulation
            return ForAll(s_,Implies(environment_moves ,Or(guarantee_s_, ExistsFormula)))
        else:
            if(game == "general"):
                #1. Create the E Formula in the AE formulation
                ExistsFormula = Exists(s__, And(controller_moves, postcondition))

                #2. Project E-Formula
                g =Goal()
                g.add(ExistsFormula)
                ExistsFormula = tactic_qe_fixpoint(g).as_expr()

                #3. Use Projected E-Formula in AE formulation
                # return ForAll(s_,Implies(environment_moves , Exists(s__, And(controller_moves, postcondition))))
                return ForAll(s_,Implies(environment_moves , ExistsFormula))
            else:
                raise Exception("Wrong game type entered. Please enter 'safety', 'reachability', or 'general' as the third argument.")
    

# Formulation for the game where controller plays first
def getFormulationEA(s_, s__, controller_moves, environment_moves, guarantee_s_, postcondition, game):
    if(game == "safety"):
        return Exists(s_, And(controller_moves, guarantee_s_, ForAll(s__, Implies(environment_moves, postcondition))))
    else:
        if(game == "reachability"):
            ForAllFormula = ForAll(s__, Implies(environment_moves, postcondition))
            g =Goal()
            g.add(ForAllFormula)
            ForAllFormula = tactic_qe_fixpoint(g).as_expr()
            return Exists(s_, And(controller_moves, Or(guarantee_s_, ForAllFormula) ))
        else:
            if(game == "general"):
                # ForAllFormula = ForAll(s__, Implies(environment_moves, postcondition))
                # g =Goal()
                # g.add(ForAllFormula)
                # ForAllFormula = tactic_qe_fixpoint(g).as_expr()
                # return Exists(s_, And(controller_moves, ForAllFormula))
                return Exists(s_, And(controller_moves, ForAll(s__, Implies(environment_moves, postcondition))))
            else:
                raise Exception("Wrong game type entered. Please enter 'safety', 'reachability', or 'general' as the third argument.")

# -----------------------------------------------------------------------------------------
# 1.1. Safety Fixpoint Procedure
# -----------------------------------------------------------------------------------------

def safety_fixedpoint_gensys(controller_moves, environment, guarantee, mode, game_type, init):
    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            # Dynamic variable declaration 
            exec(str(var) +"= "+game_type+"('"+str(var) +"')")
            if var not in locals(): 
                # Implies variable is already to be used by z3 in the future. Store variable with a new name.
                exec(str(var)+"new123" +"= "+game_type+"('"+str(var)+"new123" +"')") in globals(), locals()
                s.append(locals()[str(var)+"new123"])
            else:
                s.append(locals()[var])
    
    #Declare and define s'
    s_ = []
    for var in s:
        exec(str(var)+"_" +" = "+game_type+"('"+str(var)+"_" +"')")
        s_.append(locals()[str(var)+"_"])

    #Declare and define s''
    s__ = []
    for var in s:
        exec(str(var)+"__" +" = "+game_type+"('"+str(var)+"__" +"')")
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
    

    # 1. Create Controller Constraints
    # See if List Comprehension (or some better way can make it a single Or formula)
    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    # 2. Fixed Point Computation

    # Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]

    i = 1

    W0 = guarantee(*s)
    W1 = guarantee(*s)

    while True:
        print("Iteration", i )
        W0 = W1
        # Substitute current variables with post variables
        W0_ = substitute(W0, *substList)
        
        # Game Formulation for the safety game
        W1 = And(getFormulation(s_, s__, controller, environment(*envtransitionVars), guarantee(*s_), W0_, "safety"), guarantee(*s))
        g = Goal()
        g.add(W1)
        W1 = tactic_qe_fixpoint(g).as_expr()

        i = i + 1
        if valid(Implies(W0, W1),0):
            break

    print("")
    print("Number of iterations: ", i-1)
    print("")
    # print("Invariant is")
    # print(W0)
    #3. Output: Controller Extraction or Unrealizable
    if not (valid(Implies(init(*s), W0),0) and satisfiable(W0,0)):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")

        # print("EXTRACTING CONTROLLER...")
        # # In the invariant, substitute with post variables
        # #Take backup of invariant to analyse in the end
        # Invariant = W0
        # F = substitute(W0, *substList)

        # disjunction_of_conditions = False

        # with open("controller.txt", "w") as text_file:
        #     print("Controller Logic", file=text_file)

        # for move_i in controller_moves:
        #     #Get AE/EA Formula with postcondition F
        #     condition_move_i = And(getFormulation(s_, s__, move_i(*contransitionVars), environment(*envtransitionVars), guarantee(*s_), F, "safety"), guarantee(*s))

        #     #Move i condition extraction
        #     #Eliminate quantifiers and simplify to get the conditions for each move
        #     g = Goal()
        #     g.add(condition_move_i)
        #     condition_move_i = tactic_qe_controller(g).as_expr()

        #     with open("controller.txt", "a") as text_file:
        #         print("\nCondition for the controller action: "+ str(move_i.__name__), file=text_file)
        #         print(condition_move_i, file=text_file)

        #     #For final sanity check
        #     disjunction_of_conditions = Or(condition_move_i, disjunction_of_conditions)

        # # close the file
        # text_file.close()
        # print("Controller printed in controller.txt file in the form 'condition_i -> move_i'")
        # #Sanity check: Disjunction of controller conditions is equal to Invariant
        # formula = disjunction_of_conditions == Invariant

        # assert(valid(formula,0))


# -----------------------------------------------------------------------------------------
# 1.2. Reachability Fixpoint Procedure
# -----------------------------------------------------------------------------------------

def reachability_fixedpoint_gensys(controller_moves, environment, guarantee, mode, game_type, init):
    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            # Dynamic variable declaration
            exec(str(var) +"= "+game_type+"('"+str(var) +"')")
            if var not in locals(): 
                # Implies variable is already to be used by z3 in the future. Store variable with a new name.
                exec(str(var)+"new123" +"= "+game_type+"('"+str(var)+"new123" +"')") in globals(), locals()
                s.append(locals()[str(var)+"new123"])
            else:
                s.append(locals()[var])
    
    #Declare and define s'
    s_ = []
    for var in s:
        exec(str(var)+"_" +" = "+game_type+"('"+str(var)+"_" +"')")
        s_.append(locals()[str(var)+"_"])

    #Declare and define s''
    s__ = []
    for var in s:
        exec(str(var)+"__" +" = "+game_type+"('"+str(var)+"__" +"')")
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
    

    # 1. Create Controller Constraints
    # See if List Comprehension (or some better way can make it a single Or formula)
    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    # 2. Fixed Point Computation

    # Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]

    i = 1

    W0 = guarantee(*s)
    W1 = guarantee(*s)
    
    # Map for controller states
    C = []
    C.append(W0)

    while True:
        print("Iteration", i )
        W0 = W1
        # Substitute current variables with post variables
        W0_ = substitute(W0, *substList)
        
        # Game Formulation for the safety game
        W1 = Or(getFormulation(s_, s__, controller, environment(*envtransitionVars), guarantee(*s_), W0_, "reachability"), guarantee(*s))
        g = Goal()
        g.add(W1)
        W1 = tactic_qe_fixpoint(g).as_expr()
        C.append(And(W1, Not(W0)))
        print(W1)
        i = i + 1
        if valid(Implies(W1, W0),0):
            break

    print("")
    iterations = i - 1
    print("Number of iterations: ", iterations)
    print("")
    print("Invariant is")
    print(W0)
    #3. Output: Controller Extraction or Unrealizable
    if not (valid(Implies(init(*s), W0),0) and satisfiable(W0,0)):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")
        # print("EXTRACTING CONTROLLER...")
        # # In the invariant, substitute with post variables
        # #Take backup of invariant to analyse in the end
        # Invariant = W0

        # disjunction_of_conditions = False
        # assert (len(C) == iterations+1)

        # with open("controller.txt", "w") as text_file:
        #     print("Controller Logic", file=text_file)

        # for move_i in controller_moves:
            
        #     condition_move_i = False
        #     C_Union = False
        #     for j in range(1, iterations+1):
        #         #Get AE/EA Formula with postcondition C[j-1]
        #         C_Union = Or(C[j-1], C_Union)
        #         c_ = substitute(C_Union, *substList)
        #         wp = getFormulation(s_, s__, move_i(*contransitionVars), environment(*envtransitionVars), guarantee(*s_), c_ , "reachability")

        #         if satisfiable(And(wp, C[j]),0):
        #             condition_move_i = Or(condition_move_i, And(wp, C[j]))
        #             #Move i condition extraction
        #             #Eliminate quantifiers and simplify to get the conditions for each move
        #             g = Goal()
        #             g.add(condition_move_i)
        #             condition_move_i = tactic_qe_fixpoint(g).as_expr()

        #     with open("controller.txt", "a") as text_file:
        #         print("\nCondition for the controller action: "+ str(move_i.__name__), file=text_file)
        #         print(condition_move_i, file=text_file)

        #     #For final sanity check
        #     disjunction_of_conditions = Or(condition_move_i, disjunction_of_conditions)

        # # close the file
        # text_file.close()
        # print("Controller printed in controller.txt file in the form 'condition_i -> move_i'")

        # #Sanity check: Disjunction of controller conditions is equal to Invariant without guarantee
        # formula = disjunction_of_conditions == And(Invariant, Not(guarantee(*s)))

        # assert(valid(formula,0))

# -----------------------------------------------------------------------------------------
# 1.3. Buchi Fixpoint Procedure
# -----------------------------------------------------------------------------------------

def buchi_fixedpoint_gensys(controller_moves, environment, guarantee, mode, game_type, init):
    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            # Dynamic variable declaration
            exec(str(var) +"= "+game_type+"('"+str(var) +"')")
            if var not in locals(): 
                # Implies variable is already to be used by z3 in the future. Store variable with a new name.
                exec(str(var)+"new123" +"= "+game_type+"('"+str(var)+"new123" +"')") in globals(), locals()
                s.append(locals()[str(var)+"new123"])
            else:
                s.append(locals()[var])
    
    #Declare and define s'
    s_ = []
    for var in s:
        exec(str(var)+"_" +" = "+game_type+"('"+str(var)+"_" +"')")
        s_.append(locals()[str(var)+"_"])

    #Declare and define s''
    s__ = []
    for var in s:
        exec(str(var)+"__" +" = "+game_type+"('"+str(var)+"__" +"')")
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
    

    # 1. Create Controller Constraints
    # See if List Comprehension (or some better way can make it a single Or formula)
    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    # 2. Fixed Point Computation

    # Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]

    substList_ = []
    for (var, var_) in zip(s,s_):
        substList_ = substList_+[(var,var_)]

    envtransitionVars = s+s_
    contransitionVars = s+s_

    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    i = 1

    W0e = And(True)
    W1e = And(True)

    W0c = And(True)
    W1c = And(True)

    while True:
        print("Iteration", i )
        W0e = W1e
        W0c = W1c
        
        #Substitute current variables with post variables
        W0e_ = substitute(W0e, *substList_)
        W0c_ = substitute(W0c, *substList_)

        W1e = And( ForAll(s_, Implies(environment(*envtransitionVars) , W0c_)) , guarantee(*s))
        W1c = And( Exists(s_, And(controller, W0e_)), guarantee(*s))

        g =Goal()
        g.add(W1e)
        W1e = tactic_qe_fixpoint(g).as_expr()

        g =Goal()
        g.add(W1c)
        W1c = tactic_qe_fixpoint(g).as_expr()

        j = 1

        H0e = And(False)
        H1e = And(False)

        H0c = And(False)
        H1c = And(False)

        # # Map for controller states
        # C = []
        # C.append(H0)

        while True:
            print("Sub-Iteration", j )
            H0e = H1e
            H0c = H1c

            #Substitute current variables with post variables
            H0e_ = substitute(H0e, *substList_)
            H0c_ = substitute(H0c, *substList_)

            H1e = Or( ForAll(s_, Implies(environment(*envtransitionVars) , H0c_)) , W1e)
            H1c = Or( Exists(s_, And(controller, H0e_)), W1c)
            
            g =Goal()
            g.add(H1e)
            H1e = tactic_qe_fixpoint(g).as_expr()

            g =Goal()
            g.add(H1c)
            H1c = tactic_qe_fixpoint(g).as_expr()

            # C.append(And(H1, Not(H0)))
            
            j = j + 1
            iterations = j-1

            if valid(And(Implies(H1e, H0e), Implies(H1c, H0c)),0):
                break

        W1e = H0e
        W1c = H0c

        i = i + 1
        print()
        if valid(And(Implies(W0e, W1e), Implies(W0c, W1c)),0):
            break

    W0e_ = substitute(W0e, *substList_)
    # W = Or(W0c, Exists(s_, And(controller, W0e_)))
    W = W0c

    if not (valid(Implies(init(*s), W),0) and satisfiable(W,0)):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")

# -----------------------------------------------------------------------------------------
# 1.4. Co-Buchi Fixpoint Procedure
# -----------------------------------------------------------------------------------------

def cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, mode, game_type, init):
    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            # Dynamic variable declaration
            exec(str(var) +"= "+game_type+"('"+str(var) +"')")
            if var not in locals(): 
                # Implies variable is already to be used by z3 in the future. Store variable with a new name.
                exec(str(var)+"new123" +"= "+game_type+"('"+str(var)+"new123" +"')") in globals(), locals()
                s.append(locals()[str(var)+"new123"])
            else:
                s.append(locals()[var])
    
    #Declare and define s'
    s_ = []
    for var in s:
        exec(str(var)+"_" +" = "+game_type+"('"+str(var)+"_" +"')")
        s_.append(locals()[str(var)+"_"])

    #Declare and define s''
    s__ = []
    for var in s:
        exec(str(var)+"__" +" = "+game_type+"('"+str(var)+"__" +"')")
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
    

    # 1. Create Controller Constraints
    # See if List Comprehension (or some better way can make it a single Or formula)
    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    # 2. Fixed Point Computation

    # Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]

    substList_ = []
    for (var, var_) in zip(s,s_):
        substList_ = substList_+[(var,var_)]

    envtransitionVars = s+s_
    contransitionVars = s+s_

    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    i = 1

    W0e = And(False)
    W1e = And(False)

    W0c = And(False)
    W1c = And(False)

    # # Map for controller states
    # C = []
    # C.append(W0)
    while True:
        print("Iteration", i )
        W0e = W1e
        W0c = W1c
        
        #Substitute current variables with post variables
        W0e_ = substitute(W0e, *substList_)
        W0c_ = substitute(W0c, *substList_)

        W1e = Or( ForAll(s_, Implies(environment(*envtransitionVars) , W0c_)) , guarantee(*s))
        W1c = Or( Exists(s_, And(controller, W0e_)), guarantee(*s))

        g =Goal()
        g.add(W1e)
        W1e = tactic_qe_fixpoint(g).as_expr()

        g =Goal()
        g.add(W1c)
        W1c = tactic_qe_fixpoint(g).as_expr()

        j = 1

        H0e = And(True)
        H1e = And(True)

        H0c = And(True)
        H1c = And(True)

        while True:
            print("Sub-Iteration", j )
            H0e = H1e
            H0c = H1c

            #Substitute current variables with post variables
            H0e_ = substitute(H0e, *substList_)
            H0c_ = substitute(H0c, *substList_)

            H1e = And( ForAll(s_, Implies(environment(*envtransitionVars) , H0c_)) , W1e)
            H1c = And( Exists(s_, And(controller, H0e_)), W1c)
            
            g =Goal()
            g.add(H1e)
            H1e = tactic_qe_fixpoint(g).as_expr()

            g =Goal()
            g.add(H1c)
            H1c = tactic_qe_fixpoint(g).as_expr()

            # C.append(And(H1, Not(H0)))
            
            j = j + 1
            iterations = j-1

            if valid(And(Implies(H0e, H1e), Implies(H0c, H1c)),0):
                break

        W1e = H0e
        W1c = H0c

        i = i + 1
        print()
        if valid(And(Implies(W1e, W0e), Implies(W1c, W0c)),0):
            break

    W0e_ = substitute(W0e, *substList_)
    # W = Or(W0c, Exists(s_, And(controller, W0e_)))
    W = W0c
    print(W)
    if not (valid(Implies(init(*s), W),0) and satisfiable(W,0)):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# 2. Fixpoint Procedures for general LTL specifications
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# 2.1 Deterministic Product Games (Buchi, Co-Buchi)
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Utility function to check number of determinized automaton states in a given formula F(s,c)
def print_q_automaton_states(formula, q, nQ):
    print("Printing determinized automaton states")
    #Function to check models
    s = Solver()
    s.add(formula)
    count = 0
    while s.check() == sat:
        count+=1
        # Print readable model
        m = s.model()
        aut_state = (q, m[q])
        model_formula = (q == m.evaluate(q))
        g =Goal()
        g.add(Exists(q, And(formula, model_formula)))
        s_pred = tactic_qe_fixpoint(g).as_expr()

        print(aut_state, s_pred)
        s.add(q != m.evaluate(q))
    # Print total number of states
    print("Number of states:", count)

# -----------------------------------------------------------------------------------------
# 2.1.1 Product Buchi Fixpoint Procedure (Deterministic Buchi Automaton)
# -----------------------------------------------------------------------------------------

def buchi_fixedpoint(controller_moves, environment, guarantee, mode, automaton, isFinal, nQ, game_type, init):
    print("Buchi Fixed Point Computation")

    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            # Dynamic variable declaration
            exec(str(var) +"= "+game_type+"('"+str(var) +"')") in globals(), locals()
            if var not in locals(): 
                # Implies variable is already to be used by z3 in the future. Store variable with a new name.
                exec(str(var)+"new123" +"= "+game_type+"('"+str(var)+"new123" +"')") in globals(), locals()
                s.append(locals()[str(var)+"new123"])
            else:
                s.append(locals()[var])
    
    #Declare and define s' of type game_type
    s_ = []
    for var in s:
        exec(str(var)+"_" +" = "+game_type+"('"+str(var)+"_" +"')") in globals(), locals()
        s_.append(locals()[str(var)+"_"])

    #Declare and define s'' of type game_type
    s__ = []
    for var in s:
        exec(str(var)+"__" +" = "+game_type+"('"+str(var)+"__" +"')") in globals(), locals()
        s__.append(locals()[str(var)+"__"])

    # Create automaton state variables
    q = Int("q")
    q_ = Int("q_")
    q__ = Int("q__")

    def project(formula):
        g =Goal()
        g.add(formula)
        return tactic_qe_fixpoint(g).as_expr()

    # Define the guarantee that we will use

    # Guarantee over the deterministic automaton states for a given k
    def guarantee_automaton(q):
        #Hard coded for now
        return isFinal(q)

    # Decide formulation based on game mode
    # Declare and define transition variables list for controller and environment, depending on the mode
    if(mode == 1):
        raise Exception("AE mode not supported for Buchi games")
        getFormulation = getFormulationAE_otfd
        contransitionVars = s_+s__
        envtransitionVars = s+s_
    else: 
        if(mode == 0):
            getFormulation = getFormulationEA_otfd
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

    #Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]  
    substList = substList+[(q, q__)]  

    substList_ = []
    for (var, var_) in zip(s,s_):
        substList_ = substList_+[(var,var_)]  
    substList_ = substList_+[(q, q_)]  

    envtransitionVars = s+s_
    contransitionVars = s+s_

    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    i = 1

    W0e = And(True)
    W1e = And(True)

    W0c = And(True)
    W1c = And(True)

    while True:
        print("Iteration", i )
        W0e = W1e
        W0c = W1c
        
        #Substitute current variables with post variables
        W0e_ = substitute(W0e, *substList_)
        W0c_ = substitute(W0c, *substList_)

        W1e = And( ForAll(s_+[q_], Implies(And(environment(*envtransitionVars), automaton(q,q_,*s)) , W0c_)) , guarantee_automaton(q))
        W1c = And( Exists(s_+[q_], And(And(controller, automaton(q,q_,*s)), W0e_)), guarantee_automaton(q))

        g =Goal()
        g.add(W1e)
        W1e = tactic_qe_fixpoint(g).as_expr()

        g =Goal()
        g.add(W1c)
        W1c = tactic_qe_fixpoint(g).as_expr()

        j = 1

        H0e = And(False)
        H1e = And(False)

        H0c = And(False)
        H1c = And(False)

        # # Map for controller states
        # C = []
        # C.append(H0)

        while True:
            print("Sub-Iteration", j )
            H0e = H1e
            H0c = H1c

            #Substitute current variables with post variables
            H0e_ = substitute(H0e, *substList_)
            H0c_ = substitute(H0c, *substList_)

            H1e = Or( ForAll(s_+[q_], Implies(And(environment(*envtransitionVars), automaton(q,q_,*s)) , H0c_)) , W1e)
            H1c = Or( Exists(s_+[q_], And(controller, automaton(q,q_,*s),  H0e_)), W1c)
            
            g =Goal()
            g.add(H1e)
            H1e = tactic_qe_fixpoint(g).as_expr()

            g =Goal()
            g.add(H1c)
            H1c = tactic_qe_fixpoint(g).as_expr()

            # C.append(And(H1, Not(H0)))
            
            j = j + 1
            iterations = j-1

            if valid(And(Implies(H1e, H0e), Implies(H1c, H0c)),0):
                break

        W1e = H0e
        W1c = H0c

        i = i + 1
        print()
        if valid(And(Implies(W0e, W1e), Implies(W0c, W1c)),0):
            break

    W0e_ = substitute(W0e, *substList_)
    # W = Or(W0c, Exists(s_, And(controller, W0e_)))
    W = W0c

    # Extract the winning region from the initial automaton state
    WWpre = W
    W = Exists(q, And(W, q == 0))

    WW = W

    if not (valid(Implies(init(*s), W),0) and satisfiable(W,0)):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")

# -----------------------------------------------------------------------------------------
# 2.1.2 Product Co-Buchi Fixpoint Procedure (Deterministic Co-Buchi Automaton)
# -----------------------------------------------------------------------------------------

def cobuchi_fixedpoint(controller_moves, environment, guarantee, mode, automaton, isFinal, nQ, game_type, init):
    print("Co-Buchi Fixed Point Computation")

    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            # Dynamic variable declaration
            exec(str(var) +"= "+game_type+"('"+str(var) +"')") in globals(), locals()
            if var not in locals(): 
                # Implies variable is already to be used by z3 in the future. Store variable with a new name.
                exec(str(var)+"new123" +"= "+game_type+"('"+str(var)+"new123" +"')") in globals(), locals()
                s.append(locals()[str(var)+"new123"])
            else:
                s.append(locals()[var])

    #Declare and define s' of type game_type
    s_ = []
    for var in s:
        exec(str(var)+"_" +" = "+game_type+"('"+str(var)+"_" +"')") in globals(), locals()
        s_.append(locals()[str(var)+"_"])

    #Declare and define s'' of type game_type
    s__ = []
    for var in s:
        exec(str(var)+"__" +" = "+game_type+"('"+str(var)+"__" +"')") in globals(), locals()
        s__.append(locals()[str(var)+"__"])

    # Create automaton state variables
    q = Int("q")
    q_ = Int("q_")
    q__ = Int("q__")

    def project(formula):
        g =Goal()
        g.add(formula)
        return tactic_qe_fixpoint(g).as_expr()

    # Guarantee over the deterministic automaton states for a given k
    def guarantee_automaton(q):
        return isFinal(q)
    
    # Decide formulation based on game mode
    # Declare and define transition variables list for controller and environment, depending on the mode
    if(mode == 1):
        raise Exception("AE mode not supported for CoBuchi games")
        getFormulation = getFormulationAE_otfd
        contransitionVars = s_+s__
        envtransitionVars = s+s_
    else: 
        if(mode == 0):
            getFormulation = getFormulationEA_otfd
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

    #Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]  
    substList = substList+[(q, q__)]  

    substList_ = []
    for (var, var_) in zip(s,s_):
        substList_ = substList_+[(var,var_)]  
    substList_ = substList_+[(q, q_)]  

    envtransitionVars = s+s_
    contransitionVars = s+s_

    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)

    i = 1

    W0e = And(False)
    W1e = And(False)

    W0c = And(False)
    W1c = And(False)

    while True:
        print("Iteration", i )
        W0e = W1e
        W0c = W1c
        
        #Substitute current variables with post variables
        W0e_ = substitute(W0e, *substList_)
        W0c_ = substitute(W0c, *substList_)

        W1e = Or( ForAll(s_+[q_], Implies(And(environment(*envtransitionVars), automaton(q,q_,*s)) , W0c_)) , guarantee_automaton(q))
        W1c = Or( Exists(s_+[q_], And(And(controller, automaton(q,q_,*s)), W0e_)), guarantee_automaton(q))

        g =Goal()
        g.add(W1e)
        W1e = tactic_qe_fixpoint(g).as_expr()

        g =Goal()
        g.add(W1c)
        W1c = tactic_qe_fixpoint(g).as_expr()

        j = 1

        H0e = And(True)
        H1e = And(True)

        H0c = And(True)
        H1c = And(True)

        # # Map for controller states
        # C = []
        # C.append(H0)

        while True:
            print("Sub-Iteration", j )
            H0e = H1e
            H0c = H1c

            #Substitute current variables with post variables
            H0e_ = substitute(H0e, *substList_)
            H0c_ = substitute(H0c, *substList_)

            H1e = And( ForAll(s_+[q_], Implies(And(environment(*envtransitionVars), automaton(q,q_,*s)) , H0c_)) , W1e)
            H1c = And( Exists(s_+[q_], And(controller, automaton(q,q_,*s),  H0e_)), W1c)
            
            g =Goal()
            g.add(H1e)
            H1e = tactic_qe_fixpoint(g).as_expr()

            g =Goal()
            g.add(H1c)
            H1c = tactic_qe_fixpoint(g).as_expr()

            # C.append(And(H1, Not(H0)))
            
            j = j + 1
            iterations = j-1

            if valid(And(Implies(H0e, H1e), Implies(H0c, H1c)),0):
                break

        W1e = H0e
        W1c = H0c

        i = i + 1
        print()
        if valid(And(Implies(W1e, W0e), Implies(W1c, W0c)),0):
            break

    W0e_ = substitute(W0e, *substList_)
    # W = Or(W0c, Exists(s_, And(controller, W0e_)))
    W = W0c

    # Extract the winning region from the initial automaton state
    WWpre = W
    W = Exists(q, And(W, q == 0))

    WW = W

    if not (valid(Implies(init(*s), W),0) and satisfiable(W,0)):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# 2.2. Bounded Fixpoint Procedures (Non deterministic Automatons)
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Projection function that uses the selected tactic

def project(formula):
    g =Goal()
    g.add(formula)
    return tactic_qe_fixpoint(g).as_expr()

# Utility function to check number of determinized automaton states in a given formula F(s,c)
def print_automaton_states(formula, c, nQ):
    print("Printing determinized automaton states")
    #Function to check models
    s = Solver()
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
        s.add(constraints)
    # Print total number of states
    print("Number of states:", count)


# -----------------------------------------------------------------------------------------
# 2.2.1. On-The-Fly Determinization (OTFD) based Fixpoint Procedure
# -----------------------------------------------------------------------------------------

def min(x,y):
    return If(x < y, x, y)

def succ(c, sigma_x, c_, automaton, isFinal, s, k):

    # 1. Range Constraints

    range_c = And([And(c[p] >= -1, c[p] <= k+1) for p in range(0, len(c))])
    range_c_ = And([And(c_[q] >= -1, c_[q] <= k+1) for q in range(0, len(c))])

    # 2. Determinization constraint

    # det = ForAll([p,x], Implies(And(automaton(p,q,x), sigma_x, c(p) != -1), c_(q) >= min(c(p) + isFinal(q) , k) ))
    det = And([And([ForAll(s, Implies(And(automaton(p,q,*s), sigma_x, c[p] != -1), c_[q] >= min(c[p] + isFinal(q) , k+1) )) for p in range(0, len(c))]) for q in range(0, len(c_))])
 
    # 3. Reachability constraint

    # reach = Implies(c_(q) != -1, Exists([p,x], And(automaton(p,q,x), sigma_x, c_(q) == min(c(p) + isFinal(q) , k) )))
    reach = And([Implies(c_[q] != -1, Or([Exists(s, And(automaton(p,q,*s), sigma_x, c[p] != -1,  c_[q] == min(c[p] + isFinal(q) , k+1) )) for p in range(0, len(c))]) ) for q in range(0, len(c_))])

    return And(range_c, range_c_, det,  reach)

def is_downward_closed(W, v, c, nQ, game_type):
    # Input: W(V,c)
    # Output: True if downward closed, else counterexample model.

    # Declare and define v1
    v1 = []
    for var in v:
        exec(str(var)+"1" +" = "+game_type+"('"+str(var)+"1" +"')") in globals(), locals()
        v1.append(locals()[str(var)+"1"])

    c1 = IntVector('c1', nQ)

    # Create a list for substitution of game states
    substList_vv1 = []
    for (var, var1) in zip(v,v1):
        substList_vv1 = substList_vv1+[(var,var1)]

    # Create W_(v1,c1) from W(v,c)
    W_ = substitute(W, *substList_vv1+[(c[j], c1[j]) for j in range(len(c))])

    # Find model (v,c) which is not present in W but should have been (i.e., there exists a v'c' that dominates it)
    L = Exists(v1+c1, And(W_, Not(W), And(And([v[k] == v1[k]  for k in range(0,len(v))]), And([And(c[k] <= c1[k], c[k]>=-1) for k in range(0, len(c))]))))
    s = Solver()
    if s.check(L) == unsat:
        return True
    else:
        # L = project(L)
        # print_automaton_states(L,c,nQ)
        return False

def otfd_fixedpoint(controller_moves, environment, guarantee, mode, automaton, isFinal, sigma, nQ, k, game_type, init):

    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            # Dynamic variable declaration
            exec(str(var) +"= "+game_type+"('"+str(var) +"')") in globals(), locals()
            if var not in locals(): 
                # Implies variable is already to be used by z3 in the future. Store variable with a new name.
                exec(str(var)+"new123" +"= "+game_type+"('"+str(var)+"new123" +"')") in globals(), locals()
                s.append(locals()[str(var)+"new123"])
            else:
                s.append(locals()[var])
    
    #Declare and define s' of type game_type
    s_ = []
    for var in s:
        exec(str(var)+"_" +" = "+game_type+"('"+str(var)+"_" +"')") in globals(), locals()
        s_.append(locals()[str(var)+"_"])

    #Declare and define s'' of type game_type
    s__ = []
    for var in s:
        exec(str(var)+"__" +" = "+game_type+"('"+str(var)+"__" +"')") in globals(), locals()
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
    projected_succ = [project(succ(c,sigma[i],c_, automaton, isFinal, s, k)) for i in range(len(sigma))]
    # Define Succ function for determinization (depends on projected_succ (depends on succ (depends on min)))
    def Succ(c_subst, x_subst, c__subst):
        #Project quantifers in Succ before forwarding to wpAssertion.
        return Or([And( substitute(sigma[i], [(s[j], x_subst[j]) for j in range(len(s))] ), substitute(projected_succ[i], [(c[j], c_subst[j]) for j in range(len(c))] + [(c_[j], c__subst[j]) for j in range(len(c_))] ) ) for i in range(len(sigma))])
    
    # Define the guarantee that we will use

    # Guarantee over the deterministic automaton states for a given k
    def guarantee_automaton(c):
        # Bounds on the range of the deterministic automaton states (functions)
        l_bound = And([c[q] >= -1 for q in range(0, len(c))])
        u_bound = And([c[q] < k+1 for q in range(0, len(c))])

        return And(l_bound, u_bound)

    # Combine above constraint with the optional safety guarantee, if any
    def guarantee_(s, c):
        return And(guarantee(*s), guarantee_automaton(c))
    
    # Decide formulation based on game mode
    # Declare and define transition variables list for controller and environment, depending on the mode
    if(mode == 1):
        getFormulation = getFormulationAE_otfd
        contransitionVars = s_+s__
        envtransitionVars = s+s_
    else: 
        if(mode == 0):
            getFormulation = getFormulationEA_otfd
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
    wpAssertion = getFormulation(s, s_, s__, controller, environment(*envtransitionVars), guarantee_(s_,c_), guarantee_(s__,c__), Succ, c, c_, c__)
    
    #2. Fixed Point Computation

    #Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]  
    g =Goal()
    g.add(wpAssertion)
    wp = tactic_qe_fixpoint(g).as_expr()
    # print("Maximal states are: ")
    # m =  maximal(wp,s, s_, c, c_, nQ)
    # print_automaton_states(m,c,nQ)
    # print_automaton_states(wp,c,nQ)
    # Add an assertion to be sure that all sets are downward closed. Remove this check for efficiency.
    assert is_downward_closed(wp, s, c, nQ, game_type)
    W = And(wp, guarantee_(s, c))
    F = guarantee_(s, c)
    i = 1
    print("Iteration", i )
    i = i + 1
    
    while(not valid(Implies(F, W),0)):
        temp = W
        #Substitute current variables with post variables
        W = substitute(W, *substList+[(c[j], c__[j]) for j in range(nQ)])

        #Get AE/EA Formula with postcondition W
        wpAssertion = getFormulation(s, s_, s__, controller, environment(*envtransitionVars), guarantee_(s_,c_), W, Succ, c, c_, c__)

        g = Goal()
        g.add(wpAssertion)
        wp = tactic_qe_fixpoint(g).as_expr()
        # print("Maximal states are: ")
        # m =  maximal(wp,s, s_, c, c_, nQ)
        # print_automaton_states(m,c,nQ)
        # print_automaton_states(wp,c,nQ)
        # Add an assertion to be sure that all sets are downward closed. Remove this check for efficiency.
        assert is_downward_closed(wp, s, c, nQ, game_type)
        W = And(wp, guarantee_(s, c))
        F = temp
        print("Iteration ", i )
        i=i+1

    #3. Output: Controller Extraction or Unrealizable
    # Create constraint for the initial state of the automaton. 
    # For example,
    # init = And(c[0]==0, c[1]==-1) for 2 states 
    # init = And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==-1, c[4]==-1, c[5]==-1) for 6 states 
    init_aut = And(c[0] == 0, And([c[q] == -1 for q in range(1,nQ)]))

    W0 = Exists(c, And(F, init_aut))

    if not (valid(Implies(init(*s), W0),0) and satisfiable(W0,0)):
    # if not satisfiable(And(F, init),0):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")
        # g = Goal()
        # g.add(F)
        # F = tactic_qe_fixpoint(g).as_expr()
        # print("Invariant is: ")
        # print(F)
        # print("Maximal states are: ")
        # m =  maximal(F,s, s_, c, c_, nQ)
        # print_automaton_states(And(m, init),c,nQ)
        # print_automaton_states(And(F, init),c,nQ)
        # g = Goal()
        
        # g.add(Exists(c, F))
        # PF = tactic_qe_fixpoint(g).as_expr()
        # print("Projected invariant is: ")
        # print(PF)

        # g.add(Exists(c, And(F, init)))
        # PF = tactic_qe_fixpoint(g).as_expr()
        # print("Projected invariant for initial state is: ")
        # print(PF)

    print("")
    print("Number of iterations: ", i-1)
    print("")

#Formulation for the game where envrionment plays first with LTL specification
def getFormulationAE_otfd(s, s_, s__, controller_moves, environment_moves, guarantee_s_c_, postcondition, Succ, c, c_, c__):
    
    #1. Create the E Formula in the AE formulation
    ExistsFormula = Exists(s__+c__, And(controller_moves, Succ(c_,s_,c__), postcondition))

    #2. Project E-Formula
    g =Goal()
    g.add(ExistsFormula)
    ExistsFormula = tactic_qe_fixpoint(g).as_expr()

    #3. Use Projected E-Formula in AE formulation
    # return ForAll(s_+c_, Implies(And(environment_moves, Succ(c,s,c_)), And(guarantee_s_c_, Exists(s__+c__, And(controller_moves, Succ(c_,s_,c__), postcondition)))))
    return ForAll(s_+c_, Implies(And(environment_moves, Succ(c,s,c_)), And(guarantee_s_c_, ExistsFormula)))

#Formulation for the game where controller plays first with omega specification
def getFormulationEA_otfd(s, s_, s__, controller_moves, environment_moves, guarantee_s_c_, postcondition, Succ, c, c_, c__):

    # Projecting Forall first was not fast 
    # ForAllFormula = ForAll(s__+c__, Implies(And(environment_moves, Succ(c_,s_,c__)), postcondition))
    #2. Project FA-Formula
    # g =Goal()
    # g.add(ForAllFormula)
    # ForAllFormula = tactic_qe_fixpoint(g).as_expr()
    # print("Maximal states are: ")
    # m =  maximal(And(guarantee_s_c_, ForAllFormula),s_, s__, c_, c__, 5)
    # print_automaton_states(m,c_,5)
    # print_automaton_states(And(guarantee_s_c_, ForAllFormula), c_, 5)
    # return Exists(s_+c_, And(controller_moves, Succ(c,s,c_), guarantee_s_c_, ForAllFormula))
    return Exists(s_+c_, And(controller_moves, Succ(c,s,c_), guarantee_s_c_, ForAll(s__+c__, Implies(And(environment_moves, Succ(c_,s_,c__)), postcondition))))

# -------------------------------------------------------------------------------------------------
# 2.2.2. On-The-Fly Determinization (OTFD) based Fixpoint Procedure (without predicate partitioning)
# -------------------------------------------------------------------------------------------------

# Projection function that uses the selected tactic

def project(formula):
    g =Goal()
    g.add(formula)
    return tactic_qe_fixpoint(g).as_expr()

# Utility function to check number of determinized automaton states in a given formula F(s,c)
def print_automaton_states(formula, c, nQ):
    print("Printing determinized automaton states")
    #Function to check models
    s = Solver()
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
        s.add(constraints)
    # Print total number of states
    print("Number of states:", count)

# -----------------------------------------------------------------------------------------
# On-The-Fly Determinization (OTFD) based Fixpoint Procedure: Non-sigma version
# -----------------------------------------------------------------------------------------

def succ_nonsigma(c, s, c_, automaton, isFinal, k):

    # 1. Range Constraints

    range_c = And([And(c[p] >= -1, c[p] <= k+1) for p in range(0, len(c))])
    range_c_ = And([And(c_[q] >= -1, c_[q] <= k+1) for q in range(0, len(c))])

    # 2. Determinization constraint

    # det = ForAll([p,x], Implies(And(automaton(p,q,x), sigma_x, c(p) != -1), c_(q) >= min(c(p) + isFinal(q) , k) ))
    det = And([And([Implies(And(automaton(p,q,*s), c[p] != -1), c_[q] >= min(c[p] + isFinal(q) , k+1) ) for p in range(0, len(c))]) for q in range(0, len(c_))])
 
    # 3. Reachability constraint

    # reach = Implies(c_(q) != -1, Exists([p,x], And(automaton(p,q,x), sigma_x, c_(q) == min(c(p) + isFinal(q) , k) )))
    reach = And([Implies(c_[q] != -1, Or([And(automaton(p,q,*s), c[p] != -1,  c_[q] == min(c[p] + isFinal(q) , k+1) ) for p in range(0, len(c))]) ) for q in range(0, len(c_))])

    return And(range_c, range_c_, det,  reach)

def otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, mode, automaton, isFinal, sigma, nQ, k, game_type, init):

    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            # Dynamic variable declaration
            exec(str(var) +"= "+game_type+"('"+str(var) +"')") in globals(), locals()
            if var not in locals(): 
                # Implies variable is already to be used by z3 in the future. Store variable with a new name.
                exec(str(var)+"new123" +"= "+game_type+"('"+str(var)+"new123" +"')") in globals(), locals()
                s.append(locals()[str(var)+"new123"])
            else:
                s.append(locals()[var])
    
    #Declare and define s' of type game_type
    s_ = []
    for var in s:
        exec(str(var)+"_" +" = "+game_type+"('"+str(var)+"_" +"')") in globals(), locals()
        s_.append(locals()[str(var)+"_"])

    #Declare and define s'' of type game_type
    s__ = []
    for var in s:
        exec(str(var)+"__" +" = "+game_type+"('"+str(var)+"__" +"')") in globals(), locals()
        s__.append(locals()[str(var)+"__"])

    # Create determinized automaton state variables as IntVectors
    c = IntVector('c', nQ)
    c_ = IntVector('c_', nQ)
    c__ = IntVector('c__', nQ)

    # Define the guarantee that we will use

    # Guarantee over the deterministic automaton states for a given k
    def guarantee_automaton(c):
        # Bounds on the range of the deterministic automaton states (functions)
        l_bound = And([c[q] >= -1 for q in range(0, len(c))])
        u_bound = And([c[q] < k+1 for q in range(0, len(c))])

        return And(l_bound, u_bound)

    # Combine above constraint with the optional safety guarantee, if any
    def guarantee_(s, c):
        return And(guarantee(*s), guarantee_automaton(c))

    # Decide formulation based on game mode
    # Declare and define transition variables list for controller and environment, depending on the mode
    if(mode == 1):
        getFormulation = getFormulationAE_otfd
        contransitionVars = s_+s__
        envtransitionVars = s+s_
    else: 
        if(mode == 0):
            getFormulation = getFormulationEA_otfd
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
    # wpAssertion = getFormulation(s, s_, s__, controller, environment(*envtransitionVars), guarantee_(s_,c_), guarantee_(s__,c__), succ, c, c_, c__)
    wpAssertion = Exists(s_+c_, And(controller, succ_nonsigma(c,s,c_, automaton, isFinal, k), guarantee_(s_,c_), ForAll(s__+c__, Implies(And(environment(*envtransitionVars), succ_nonsigma(c_,s_,c__, automaton, isFinal, k)), guarantee_(s__,c__)))))
    
    #2. Fixed Point Computation

    #Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]

    g =Goal()
    g.add(wpAssertion)
    wp = tactic_qe_fixpoint(g).as_expr()
    # print("Maximal states are: ")
    # m =  maximal(wp,s, s_, c, c_, nQ)
    # print_automaton_states(m,c,nQ)
    # print_automaton_states(wp,c,nQ)
    # Add an assertion to be sure that all sets are downward closed. Remove this check for efficiency.
    # assert is_downward_closed(wp, s, c, nQ, k)
    W = And(wp, guarantee_(s, c))
    F = guarantee_(s, c)
    i = 1
    print("Iteration", i )
    i = i + 1
    
    while(not valid(Implies(F, W),0)):
        temp = W
        #Substitute current variables with post variables
        W = substitute(W, *substList+[(c[j], c__[j]) for j in range(nQ)])

        
        #Get AE/EA Formula with postcondition W
        # wpAssertion = getFormulation(s, s_, s__, controller, environment(*envtransitionVars), guarantee_(s_,c_), W, succ, c, c_, c__)
        wpAssertion = Exists(s_+c_, And(controller, succ_nonsigma(c,s,c_, automaton, isFinal, k), guarantee_(s_,c_), ForAll(s__+c__, Implies(And(environment(*envtransitionVars), succ_nonsigma(c_,s_,c__, automaton, isFinal, k)), W))))

        g = Goal()
        g.add(wpAssertion)
        wp = tactic_qe_fixpoint(g).as_expr()
        # print("Maximal states are: ")
        # m =  maximal(wp,s, s_, c, c_, nQ)
        # print_automaton_states(m,c,nQ)
        # print_automaton_states(wp,c,nQ)
        # Add an assertion to be sure that all sets are downward closed. Remove this check for efficiency.
        # assert is_downward_closed(wp, s, c, nQ, k)
        W = And(wp, guarantee_(s, c))
        F = temp
        print("Iteration ", i )
        i=i+1
        # exit()

    # print("Invariant is")
    # print(F)
    # print_automaton_states(F,c,nQ)

    #3. Output: Controller Extraction or Unrealizable
    # Create constraint for the initial state of the automaton. 
    # For example,
    # init = And(c[0]==0, c[1]==-1) for 2 states 
    # init = And(c[0]==0, c[1]==-1, c[2]==-1, c[3]==-1, c[4]==-1, c[5]==-1) for 6 states 
    init_aut = And(c[0] == 0, And([c[q] == -1 for q in range(1,nQ)]))

    W0 = Exists(c, And(F, init_aut))

    if not (valid(Implies(init(*s), W0),0) and satisfiable(W0,0)):
    # if not satisfiable(And(F, init),0):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")
        # g = Goal()
        # g.add(F)
        # F = tactic_qe_fixpoint(g).as_expr()
        # print("Invariant is: ")
        # print(F)
        # print("Maximal states are: ")
        # m =  maximal(F,s, s_, c, c_, nQ)
        # print_automaton_states(m,c,nQ)
        # print_automaton_states(F,c,nQ)
        # g = Goal()
        
        # g.add(Exists(c, F))
        # PF = tactic_qe_fixpoint(g).as_expr()
        # print("Projected invariant is: ")
        # print(PF)

        # g.add(Exists(c, And(F, init)))
        # PF = tactic_qe_fixpoint(g).as_expr()
        # print("Projected invariant for initial state is: ")
        # print(PF)

    print("")
    print("Number of iterations: ", i-1)
    print("")