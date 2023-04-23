
#  GenSys v2.0

#  Copyright (C) 2021 Stanly Samuel

#  This software is available under the MIT license. Please see LICENSE in the
#  top-level directory for details.

#  This file is part of gensys.

#-----------------------------------------------------------------------------------#
# GenSys: A tool for synthesis of controllers for logical games over infinite state spaces with LTL specifications.
# Author: Stanly Samuel
# Date: 14/03/2023
# Description: This file contains 8 fixpoint procedures for temporal specifications of different types.
#
# 1. Fixpoint Procedures for predicate specifications (G(formula), F(formula), GF(formula), and FG(formula))
# 1.1. Safety Fixpoint Procedure
# 1.2. Reachability Fixpoint Procedure
# 1.3. Buchi Fixpoint Procedure
# 1.4. Co-Buchi Fixpoint Procedure
# 
# 2. Fixpoint Procedures for general LTL specifications
# 2.1. Buchi Fixpoint Procedure (Deterministic Buchi Automaton)
# 2.2. Co-Buchi Fixpoint Procedure (Deterministic Co-Buchi Automaton)
# 2.3. Bounded Fixpoint Procedures (Non deterministic Automaton)
#   2.3.1. On-The-Fly Determinization based Fixpoint Procedure
#   2.3.2. Antichain based Fixpoint Procedure
#-----------------------------------------------------------------------------------#

from  gensys.helper import *
from z3 import *
# describe_tactics()
# print(tactics())
# exit()
#-------------------------------------------------------------------#
#Initialize the three tactics required for the tool. Assume user cannot control them now
#-------------------------------------------------------------------#
# Tactics for fixedpoint algorithm (use 1. if you need heavy simplification. 2. Suffices and scales well for most cases, Use some form of simplification if you need to extract the controller well)
# tactic_qe_fixpoint = Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Then(Then(Then(Tactic('collect-statistics'), Tactic('skip')), Tactic('qe2')), With('simplify',  arith_lhs=True, arith_ineq_lhs = True, som = True, som_blowup = 1, sort_sums = True,  cache_all = True, push_to_real = False, elim_to_real = True, local_ctx = True, local_ctx_limit = 10000, flat = False, flat_and_or = False))
# tactic_qe_fixpoint = Then(Tactic('qe2'), With('simplify',  arith_lhs=True, arith_ineq_lhs = True, som = True, som_blowup = 1, sort_sums = True,  cache_all = True, push_to_real = False, elim_to_real = True, local_ctx = True, local_ctx_limit = 10000, flat = False, flat_and_or = False))
# tactic_qe_fixpoint = Then(Tactic('qe2'), Repeat('ctx-solver-simplify'))
# tactic_qe_fixpoint = Tactic('qe2')

#Sort sums gave 4 second improvement.
# With('simplify' , arith_lhs=True, arith_ineq_lhs = True, som = True, som_blowup = 1, sort_sums = True,  cache_all = True, push_to_real = False, elim_to_real = True, local_ctx = True, local_ctx_limit = 10000, flat = False, flat_and_or = False')

#Parallel Tactic
tactic_qe_fixpoint = Then(Tactic('skip') , ParOr(Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify')), Then(Tactic('qe2'), Tactic('simplify'))))
# tactic_qe_fixpoint = Then(Tactic('collect-statistics') , ParOr(Then(Tactic('qe_rec'), Repeat('ctx-solver-simplify')), Then(Tactic('qe2'), With('simplify', arith_lhs=True, arith_ineq_lhs = True, som = True, som_blowup = 1, sort_sums = True,  cache_all = True, push_to_real = False, elim_to_real = True, local_ctx = True, local_ctx_limit = 10000, flat = False, flat_and_or = False))))

#Controller Extraction: Use same tactic as fixpoint and use ctx-solver-simplify to make the controller readable.
tactic_qe_controller = tactic_qe_fixpoint
tactic_simplification = Repeat('ctx-solver-simplify')
# tactic_simplification = Repeat('simplify')

# t1 = Tactic("qe2")
# t2 = Tactic("simplify")
# t3 = Tactic("propagate-ineqs")
# t4 = Tactic("propagate-values")
# t5 = Tactic("solve-eqs")
# t7 = Tactic("split-clause")
# t8 = Tactic("skip")
# tactic_qe_fixpoint = Then(t1, Repeat(Then(t2, t3, t4, t5, ParOr(t7, t8)), 10))

#-------------------------------------------------------------------#

#Options for printing in Z3
set_option(max_depth=100000, rational_to_decimal = True, precision =40, max_lines=10000)
#Options for parallel processing in Z3
set_param("parallel.enable", True)
# set_param("parallel.threads.max", 5)
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# 1. Fixpoint Procedures for non-LTL safety specifications (predicate over game states)
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Formulation for the game where envrionment plays first
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
            #Dynamic variable declaration
            #Issue: Can't use variable s in the code because it will get redeclared in this scope.
            exec(str(var) +"= "+game_type+"('"+str(var) +"')")
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
    print("Invariant is")
    print(W0)
    #3. Output: Controller Extraction or Unrealizable
    if not (valid(Implies(init(*s), W0),0) and satisfiable(W0,0)):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")

        print("EXTRACTING CONTROLLER...")
        # In the invariant, substitute with post variables
        #Take backup of invariant to analyse in the end
        Invariant = W0
        F = substitute(W0, *substList)

        disjunction_of_conditions = False

        with open("controller.txt", "w") as text_file:
            print("Controller Logic", file=text_file)

        for move_i in controller_moves:
            #Get AE/EA Formula with postcondition F
            condition_move_i = And(getFormulation(s_, s__, move_i(*contransitionVars), environment(*envtransitionVars), guarantee(*s_), F, "safety"), guarantee(*s))

            #Move i condition extraction
            #Eliminate quantifiers and simplify to get the conditions for each move
            g = Goal()
            g.add(condition_move_i)
            condition_move_i = tactic_qe_controller(g).as_expr()

            with open("controller.txt", "a") as text_file:
                print("\nCondition for the controller action: "+ str(move_i.__name__), file=text_file)
                print(condition_move_i, file=text_file)

            # close the file
            text_file.close()
            print("Controller printed in controller.txt file in the form 'condition_i -> move_i'")

            #For final sanity check
            disjunction_of_conditions = Or(condition_move_i, disjunction_of_conditions)

        #Sanity check: Disjunction of controller conditions is equal to Invariant
        formula = disjunction_of_conditions == Invariant

        assert(valid(formula,0))


# -----------------------------------------------------------------------------------------
# 1.2. Reachability Fixpoint Procedure
# -----------------------------------------------------------------------------------------

def reachability_fixedpoint_gensys(controller_moves, environment, guarantee, mode, game_type, init):
    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variable s in the code because it will get redeclared in this scope.
            exec(str(var) +"= "+game_type+"('"+str(var) +"')")
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
        print("EXTRACTING CONTROLLER...")
        # In the invariant, substitute with post variables
        #Take backup of invariant to analyse in the end
        Invariant = W0

        disjunction_of_conditions = False
        assert (len(C) == iterations+1)

        with open("controller.txt", "w") as text_file:
            print("Controller Logic", file=text_file)

        for move_i in controller_moves:
            
            condition_move_i = False
            C_Union = False
            for j in range(1, iterations+1):
                #Get AE/EA Formula with postcondition C[j-1]
                C_Union = Or(C[j-1], C_Union)
                c_ = substitute(C_Union, *substList)
                wp = getFormulation(s_, s__, move_i(*contransitionVars), environment(*envtransitionVars), guarantee(*s_), c_ , "reachability")

                if satisfiable(And(wp, C[j]),0):
                    condition_move_i = Or(condition_move_i, And(wp, C[j]))
                    #Move i condition extraction
                    #Eliminate quantifiers and simplify to get the conditions for each move
                    g = Goal()
                    g.add(condition_move_i)
                    condition_move_i = tactic_qe_fixpoint(g).as_expr()

            with open("controller.txt", "a") as text_file:
                print("\nCondition for the controller action: "+ str(move_i.__name__), file=text_file)
                print(condition_move_i, file=text_file)

            # close the file
            text_file.close()
            print("Controller printed in controller.txt file in the form 'condition_i -> move_i'")

            #For final sanity check
            disjunction_of_conditions = Or(condition_move_i, disjunction_of_conditions)

        #Sanity check: Disjunction of controller conditions is equal to Invariant without guarantee
        formula = disjunction_of_conditions == And(Invariant, Not(guarantee(*s)))

        assert(valid(formula,0))

# -----------------------------------------------------------------------------------------
# 1.3. Buchi Fixpoint Procedure
# -----------------------------------------------------------------------------------------

def buchi_fixedpoint_gensys(controller_moves, environment, guarantee, mode, game_type, init):
    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variable s in the code because it will get redeclared in this scope.
            exec(str(var) +"= "+game_type+"('"+str(var) +"')")
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

    # Weaken guarantee by adjusting for the environment states

    odd_length_con_states = Exists(s_, And(controller, guarantee(*s_)))
    g =Goal()
    g.add(odd_length_con_states)
    odd_length_con_states = tactic_qe_fixpoint(g).as_expr()

    weakened_guarantee = Or(odd_length_con_states, guarantee(*s))

    i = 1

    W0 = And(True)
    W1 = And(True)

    while True:
        print("Iteration", i )
        W0 = W1
        #Substitute current variables with post variables
        W0__ = substitute(W0, *substList)

        WPW = And(getFormulation(s_, s__, controller, environment(*envtransitionVars), And(False), W0__, "general"), weakened_guarantee)
        g =Goal()
        g.add(WPW)
        WPW = tactic_qe_fixpoint(g).as_expr()
        j = 1

        H0 = And(False)
        H1 = And(False)

        # Map for controller states
        C = []
        C.append(H0)

        while True:
            print("Sub-Iteration", j )
            H0 = H1
            #Substitute current variables with post variables
            H0__ = substitute(H0, *substList)
            WPH = getFormulation(s_, s__, controller, environment(*envtransitionVars), And(False), H0__, "general")
            H1 = Not(And(Not(WPH), Not(WPW)))
            # H1 = Or(WPH, WPW)
            g =Goal()
            g.add(H1)
            H1 = tactic_qe_fixpoint(g).as_expr()

            C.append(And(H1, Not(H0)))
            
            j = j + 1
            iterations = j-1
            if valid(Implies(H1, H0),0):
                break

        W1 = H0
        i = i + 1
        print()
        if valid(Implies(W0, W1),0):
            break

    print("")
    print("Number of iterations: ", i-1)
    print("")

    print("Invariant: ")
    print(W0)

    #3. Output: Controller Extraction or Unrealizable
    if not (valid(Implies(init(*s), W0),0) and satisfiable(W0,0)):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")

        # In the invariant, substitute with post variables
        # Take backup of invariant to analyse in the end
        Invariant = W0

        with open("controller.txt", "w") as text_file:
            print("Controller Logic", file=text_file)

        assert (len(C) == iterations+1)

        disjunction_of_conditions = False
        for move_i in controller_moves:
            
            condition_move_i = False

            C_Union = False
            for j in range(2, iterations+1):
                # Must reach union of all previous states
                C_Union = Or(C_Union, C[j-1])
                print("Iteration:", j)
                #Get AE/EA Formula with postcondition C[j-1]
                c_ = substitute(C_Union, *substList)
                wp = getFormulation(s_, s__, move_i(*contransitionVars), environment(*envtransitionVars), And(False), c_ , "general")
                if satisfiable(And(wp, C[j]),0):
                    print("Entered")
                    condition_move_i = Or(condition_move_i, And(wp, C[j]))
                    #Move i condition extraction
                    #Eliminate quantifiers and simplify to get the conditions for each move
                    g = Goal()
                    g.add(condition_move_i)
                    condition_move_i = tactic_qe_fixpoint(g).as_expr()

            # Add the last move condition, specific to Buchi: WP(G, W0) and C[1]
            W0__ = substitute(W0, *substList)
            wp = getFormulation(s_, s__, move_i(*contransitionVars), environment(*envtransitionVars), And(False), W0__ , "general")
            if satisfiable(And(wp, And(C[1], guarantee(*s))),0):
                print("eneterd")
                condition_move_i = Or(condition_move_i, And(wp, And(C[1], guarantee(*s))))
                g = Goal()
                g.add(condition_move_i)
                condition_move_i = tactic_qe_fixpoint(g).as_expr()

            # Adjust for odd moves
            substList_ = []
            for (var, var_) in zip(s,s_):
                substList_ = substList_+[(var,var_)]
            W0_ = substitute(And(C[1], guarantee(*s)), *substList_)

            wp = Exists(s_, And(move_i(*contransitionVars), W0_))
            if satisfiable(And(wp, W0),0):
                print("eneterd")
                condition_move_i = Or(condition_move_i, And(wp, W0))
                g = Goal()
                g.add(condition_move_i)
                condition_move_i = tactic_qe_fixpoint(g).as_expr()

            with open("controller.txt", "a") as text_file:
                print("\nCondition for the controller action: "+ str(move_i.__name__), file=text_file)
                print(condition_move_i, file=text_file)

            # close the file
            text_file.close()
            print("Controller printed in controller.txt file in the form 'condition_i -> move_i'")

            #For final sanity check
            disjunction_of_conditions = Or(condition_move_i, disjunction_of_conditions)

        #Sanity check: Disjunction of controller conditions is equal to Invariant without guarantee
        formula = Invariant == disjunction_of_conditions

        assert(valid(formula,0))


# -----------------------------------------------------------------------------------------
# 1.4. Co-Buchi Fixpoint Procedure
# -----------------------------------------------------------------------------------------

def cobuchi_fixedpoint_gensys(controller_moves, environment, guarantee, mode, game_type, init):
    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variable s in the code because it will get redeclared in this scope.
            exec(str(var) +"= "+game_type+"('"+str(var) +"')")
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

    # Safety followed by Reachability
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

    if not satisfiable(W0,0):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
        return

    W_Safety = W0
    W0 = W0
    W1 = W0
    
    # Map for controller states
    C = []
    C.append(W0)

    reach_count = 1

    while True:
        print("Iteration", i )
        W0 = W1
        # Substitute current variables with post variables
        W0_ = substitute(W0, *substList)
        
        # Game Formulation for the safety game
        W1 = Or(getFormulation(s_, s__, controller, environment(*envtransitionVars), guarantee(*s_), W0_, "general"), guarantee(*s))
        g = Goal()
        g.add(W1)
        W1 = tactic_qe_fixpoint(g).as_expr()
        C.append(And(W1, Not(W0)))

        i = i + 1
        reach_count = reach_count + 1

        if valid(Implies(W1, W0),0):
            break

    
    print("")
    print("Number of iterations: ", i-1)
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

        print("EXTRACTING CONTROLLER...")
        # In the invariant, substitute with post variables
        #Take backup of invariant to analyse in the end
        Invariant = W0
        F = substitute(W_Safety, *substList)

        disjunction_of_conditions = False
        assert (len(C) == reach_count)

        with open("controller.txt", "w") as text_file:
            print("Controller Logic", file=text_file)

        for move_i in controller_moves:

            #1. Add Safety constraints for controller move i
            #Get AE/EA Formula with postcondition F
            condition_move_i = And(getFormulation(s_, s__, move_i(*contransitionVars), environment(*envtransitionVars), guarantee(*s_), F, "safety"), guarantee(*s))

            #Move i condition extraction
            #Eliminate quantifiers and simplify to get the conditions for each move
            g = Goal()
            g.add(condition_move_i)
            condition_move_i = tactic_qe_controller(g).as_expr()

            #2. Add Reachability constraints for controller move i
            C_Union = False
            for j in range(1, reach_count):
                #Get AE/EA Formula with postcondition C[j-1]
                C_Union = Or(C[j-1], C_Union)
                C_Union_ = substitute(C_Union, *substList)
                wp = getFormulation(s_, s__, move_i(*contransitionVars), environment(*envtransitionVars), guarantee(*s_), C_Union_ , "general")

                if satisfiable(And(wp, C[j]),0):
                    condition_move_i = Or(condition_move_i, And(wp, C[j]))
                    #Move i condition extraction
                    #Eliminate quantifiers and simplify to get the conditions for each move
                    g = Goal()
                    g.add(condition_move_i)
                    condition_move_i = tactic_qe_fixpoint(g).as_expr()

            with open("controller.txt", "a") as text_file:
                print("\nCondition for the controller action: "+ str(move_i.__name__), file=text_file)
                print(condition_move_i, file=text_file)

            # close the file
            text_file.close()
            print("Controller printed in controller.txt file in the form 'condition_i -> move_i'")

            #For final sanity check
            disjunction_of_conditions = Or(condition_move_i, disjunction_of_conditions)

        #Sanity check: Disjunction of controller conditions is equal to Invariant
        formula = disjunction_of_conditions == Invariant

        assert(valid(formula,0))

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# 2. LTL Fixed-Point Procedures (On The Fly Determinization, Antichain):
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

# def gensys_ltl(controller_moves, environment, guarantee, mode, automaton, isFinal, sigma, nQ, game_type, approach):
    
#     if approach == "otfd":
#         function = otfd_fixedpoint
#     elif approach == "antichain":
#         function = antichain_fixedpoint
#     else:
#         print("Invalid approach")
#         return


# ---------------------------------------------------------
# 2.1. On The Fly Determinization Approach (OTFD) for LTL specs
# ---------------------------------------------------------

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

def otfd_fixedpoint(controller_moves, environment, guarantee, mode, automaton, isFinal, sigma, nQ, k, game_type):

    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variables s,g in the code because it will get redeclared in this scope. This is a problem.
            exec(str(var) +"= "+game_type+"('"+str(var) +"')") in globals(), locals()
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
    init = And(c[0] == 0, And([c[q] == -1 for q in range(1,nQ)]))
    init = c[0]!=-1
    if not satisfiable(And(F, init),0):
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


# --------------------------------------------
# 2.2. Antichain Approach for LTL specs
# --------------------------------------------

def max(x,y):
        return If(x > y, x, y)
        
def omega(c_, sigma_x, c, automaton, isFinal, s):

    # 1. Determinization constraint

    # det = ForAll([q,x], Implies(And(automaton(p,q,x), sig, c_(q) != -1), c(p) <= max(c_(q) - isFinal(q) , -1) ))
    det = And([And([ForAll(s, Implies(And(automaton(p,q, *s), sigma_x), c[p] <= max(c_[q] - isFinal(q) , -1) )) for q in range(0, len(c_))]) for p in range(0, len(c)) ])
    
    # 2. Reachability constraint

    # reach = Exists([q,x], And(automaton(p,q,x), sig, c(p) == max(c_(q) - isFinal(q) , -1) ))
    reach = And([Or([Exists(s, And(automaton(p,q,*s), sigma_x, c[p] == max(c_[q] - isFinal(q) , -1) )) for q in range(0, len(c_))]) for p in range(0, len(c))])

    return And(det, reach)

def maximal(W, v, v_, c, c_, nQ):
        # Input: W(v,c)
        # Ouput: M(v,c) representing the maximal states in W(v,c)
        # v_ and c_ represent the temporary variables to be replaced with.

        # Create a list for substitution of game states
        substList_vv_ = []
        for (var, var_) in zip(v,v_):
            substList_vv_ = substList_vv_+[(var,var_)]

        # Create W_ = W(v_,c_)
        W_ = substitute(W, *substList_vv_+[(c[j], c_[j]) for j in range(nQ)])

        # s_dominates(v, c, v', c') is the predicate that states that c' strictly dominates c and v == v'
        s_dominates = And(And([c[q] <= c_[q] for q in range(0, len(c))]), Or([c[q] < c_[q] for q in range(0, len(c))]), And([v[k] == v_[k] for k in range(0,len(v))]))
        
        # dominated(c) := Exists v', c'. W(v,c) and W(v_,c_) and sDominates(v,c,v',c')
        dominated = Exists(v_+c_, And(W, W_, s_dominates))

        # Eliminate dominated states from W(v,c).
        # maximal_states(v,c) = W(v,c) and !dominated(v, c)
        maximal_states = And(W, Not(dominated))

        # Project formula to get dominating (may not be needed)
        maximal_states = project(maximal_states)

        return maximal_states

def glb(W1, W2, v, c, nQ, game_type):
        # Input: W1(V, c), W2(V,c)
        # Ouput: L(V, c) representing the lowerbounds antichain of W1 and W2.

        # Declare and define v1
        v1 = []
        for var in v:
            exec(str(var)+"1" +" = "+game_type+"('"+str(var)+"1" +"')") in globals(), locals()
            v1.append(locals()[str(var)+"1"])

        # Declare and define v2
        v2 = []
        for var in v:
            exec(str(var)+"2" +" = "+game_type+"('"+str(var)+"2" +"')") in globals(), locals()
            v2.append(locals()[str(var)+"2"])
        c1 = IntVector('c1', nQ)
        c2 = IntVector('c2', nQ)

        # Create a list for substitution of game states
        substList_vv1 = []
        for (var, var1) in zip(v,v1):
            substList_vv1 = substList_vv1+[(var,var1)]
        
        substList_vv2 = []
        for (var, var2) in zip(v,v2):
            substList_vv2 = substList_vv2+[(var,var2)]

        # Create W1(v1,c1) from W1(v,c)
        W1 = substitute(W1, *substList_vv1+[(c[j], c1[j]) for j in range(len(c))])

        # Create W2(v1,c1) from W2(v,c)
        W2 = substitute(W2, *substList_vv2+[(c[j], c2[j]) for j in range(len(c))])
        # Find the glb L(v,c) of W1(v1, c1) and W2(v2, c2).
        L = Exists(v1+c1+v2+c2, And(W1, W2, And(And([And(v[k] == v1[k], v[k] == v2[k])  for k in range(0,len(v))]), And([And(c[k] == min(c1[k], c2[k])) for k in range(0, len(c))]))))
        L = project(L)

        # # Create L(v1,c1)
        # L_ = substitute(L, *substList_vv1+[(c[j], c1[j]) for j in range(len(c))])

        # # Find greatest lower bound G(V,c). It must exist. (Just taking maximal should suffice I think)
        # G = Not(Exists(v1+c1, And(L_, L, And([v[k] == v1[k] for k in range(0,len(v))]), And([c1[k] > c[k] for k in range(0, len(c))]))))
        # G = And(W,G)
        # G = project(G)
        # # print(G)
        # # exit()

        # return G
        return L

def antichain_fixedpoint(controller_moves, environment, guarantee, mode, automaton, isFinal, sigma, nQ, k, game_type):

    # Define Omega function for determinization (depends on omega (depends on max))
    
    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variable s in the code because it will get redeclared in this scope.
            exec(str(var) +"= "+game_type+"('"+str(var) +"')") in globals(), locals()
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

    # Retrive determinized predicate list
    sigma = sigma(*s)
    
    print("Projecting Omega to store")
    # Stores projected omega in a different array (indexed by the same index as sigma) so that project is not called always again and again.
    # This improves the speed by 2X
    projected_omega = [project(omega(c_,sigma[i],c, automaton, isFinal, s)) for i in range(len(sigma))]

    def Omega(c__subst, x_subst, c_subst):
        #Project quantifers in Omega before forwarding to wpAssertion.
        return Or([And( substitute(sigma[i], [(s[j], x_subst[j]) for j in range(len(s))] ), substitute(projected_omega[i], [(c[j], c_subst[j]) for j in range(len(c))] + [(c_[j], c__subst[j]) for j in range(len(c_))] ) ) for i in range(len(sigma))])

    # Define the guarantee that we will use

    # Gurantee over the deterministic automaton states for a given k, using antichains
    def guarantee_automaton_antichain(c):
        # Bounds on the range of the deterministic automaton states (functions)
        init = And([c[q] == k for q in range(0, len(c))])
        return And(init)

    # Combine above constraint with the optional safety guarantee, if any
    def guarantee_antichain_(s, c):
        return And(guarantee(*s), guarantee_automaton_antichain(c))

    print("Getting Formulation")
    # Decide formulation based on game mode
    # Declare and define transition variables list for controller and environment, depending on the mode
    if(mode == 1):
        # getFormulation = getFormulationAE_omega
        contransitionVars = s_+s__
        envtransitionVars = s+s_
    else: 
        if(mode == 0):
            # getFormulation = getFormulationEA_omega
            envtransitionVars = s_+s__
            contransitionVars = s+s_
        else:
            print("Wrong mode entered. Please enter 1 (for AE mode) and 0 (for EA mode) as the second argument.")
            return
    
    #1. Create Controller
    # See if List Comprehension (or some better way can make it a single Or formula)
    controller = False
    for move in controller_moves:
        controller = Or(move(*contransitionVars), controller)
        
    #2. Fixed Point Computation
    
    #Create list of tuples for substitution pre variables with post
    substList = []
    for (var, var__) in zip(s,s__):
        substList = substList+[(var,var__)]

    # Environment Pre Computation
    # Compute envPre for each move separately.
    envPre = And(True)
    for move in range(0, len(sigma)):
        projected_omega_i = substitute(projected_omega[move], [(c[j], c_[j]) for j in range(len(c))] + [(c_[j], c__[j]) for j in range(len(c_))] )
        sigma_i = substitute(sigma[move], [(s[j], s_[j]) for j in range(len(s))] )
        envPre_ = Exists(c__, And(projected_omega_i, ForAll(s__, Implies(And(sigma_i, environment(*envtransitionVars)), guarantee_antichain_(s__,c__)))) )
        g =Goal()
        g.add(envPre_)
        envPre_ = tactic_qe_fixpoint(g).as_expr()
        envPre = glb(envPre, envPre_, s_, c_, nQ, game_type)
    g =Goal()
    g.add(envPre)
    conPost = tactic_qe_fixpoint(g).as_expr()
    # print_automaton_states(conPost, c_, nQ)

    # Controller Pre Computation
    wp = Exists(s_+c_, And(Omega(c_, s, c), controller, conPost))
    wp = maximal(wp, s, s_, c, c_, nQ)
    g =Goal()
    g.add(wp)
    wp = tactic_qe_fixpoint(g).as_expr()
    # print_automaton_states(wp, c, nQ)
    # exit()
    W = wp
    F = guarantee_antichain_(s,c)

    i = 1
    print("Iteration", i )
    i = i + 1

    while(not valid(Implies(F, W),0)):
        temp = W
        W = substitute(W, *substList+[(c[j], c__[j]) for j in range(nQ)])

        # Environment Pre Computation
        # Compute envPre for each move separately.
        envPre = And(True)
        for move in range(0, len(sigma)):
            projected_omega_i = substitute(projected_omega[move], [(c[j], c_[j]) for j in range(len(c))] + [(c_[j], c__[j]) for j in range(len(c_))] )
            sigma_i = substitute(sigma[move], [(s[j], s_[j]) for j in range(len(s))] )
            # print(sigma_i)
            envPre_ = Exists(c__, And(projected_omega_i, ForAll(s__, Implies(And(sigma_i, environment(*envtransitionVars)), W))) )
            g =Goal()
            g.add(envPre_)
            envPre_ = tactic_qe_fixpoint(g).as_expr()
            envPre = glb(envPre, envPre_, s_, c_, nQ, game_type)
        g =Goal()
        g.add(envPre)
        conPost = tactic_qe_fixpoint(g).as_expr()
        # print_automaton_states(conPost, c_, nQ)

        # Controller Pre Computation
        wp = Exists(s_+c_, And(Omega(c_, s, c), controller, conPost))
        g =Goal()
        g.add(wp)
        wp = tactic_qe_fixpoint(g).as_expr()
        wp = maximal(wp, s, s_, c, c_, nQ)
        # print_automaton_states(wp, c, nQ)
        W = wp
        F = temp
        print("Iteration", i )
        i = i + 1 
        # exit()

    # The winning region in the antichain computation must contain states where c[0] is non-negative, for realizability. 0 is the start state of the automaton.
    init = c[0]!=-1

    if not satisfiable(And(F, init),0):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")
        # print("Winning region is:")
        # print_automaton_states(And(F, init), c, nQ)

    print("")
    print("Number of iterations: ", i-1)
    print("")


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

def buchi_fixedpoint(controller_moves, environment, guarantee, mode, automaton, isFinal, nQ, game_type):
    print("Buchi Fixed Point Computation")

    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variables s,g in the code because it will get redeclared in this scope. This is a problem.
            exec(str(var) +"= "+game_type+"('"+str(var) +"')") in globals(), locals()
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

    # # Guarantee over the deterministic automaton states for a given k
    def guarantee_automaton(q):
        #Hard coded for now
        return q==0 

    # Combine above constraint with the optional safety guarantee, if any
    # def guarantee_(s, q):
    #     return And(guarantee(*s), guarantee_automaton(q))
    # def guarantee_(s, q):
    #     return And(True, guarantee(q))
    
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

    # i = 1

    # W0 = And(True)
    # W1 = And(True)

    # while True:
    #     print("Iteration", i )
    #     W0 = W1
    #     #Substitute current variables with post variables
    #     W0_ = substitute(W0, *substList)
    #     j = 1

    #     H0 = And(False)
    #     H1 = And(False)

    #     while True:
    #         print("Sub-Iteration", j )
    #         H0 = H1
    #         #Substitute current variables with post variables
    #         H0_ = substitute(H0, *substList)
    #         WPW = Exists(s_+[q_], And(controller, automaton(q,q_,*s), ForAll(s__+[q__], Implies(And(environment(*envtransitionVars), automaton(q_,q__,*s_)), W0_))))
    #         WPH = Exists(s_+[q_], And(controller, automaton(q,q_,*s), ForAll(s__+[q__], Implies(And(environment(*envtransitionVars), automaton(q_,q__,*s_)), H0_))))
            
    #         H1 = Or(WPH, And(WPW, guarantee_(s, q)))
    #         g =Goal()
    #         g.add(H1)
    #         H1 = tactic_qe_fixpoint(g).as_expr()
    #         # print(H1)
    #         # print_q_automaton_states(H1, q, nQ)
    #         # exit()
        
    #         j = j + 1
    #         # print_q_automaton_states(WPW, q, nQ)
    #         if valid(Implies(H1, H0),0):
    #         # if j == 6:
    #             break
    #     # exit()
    #     W1 = H0
    #     i = i + 1
    #     if valid(Implies(W0, W1),0):
    #         break


    i = 1

    W0 = And(True)
    W1 = And(True)

    # W0 = guarantee(*s)
    # W1 = guarantee(*s)

    while True:
        print("Iteration", i )
        W0 = W1
        #Substitute current variables with post variables
        W0__ = substitute(W0, *substList)
        W0_ = substitute(W0, *substList_)
        WPW = And(Exists(s_+[q_], And(controller, automaton(q,q_,*s), ForAll(s__+[q__], Implies(And(environment(*envtransitionVars), automaton(q_,q__,*s_)), W0__)))), guarantee_automaton(q))
        # WPW = ForAll(s__+[q__], Implies(And(environment(*envtransitionVars), automaton(q_,q__,*s_)), W0__))
        # WPW = And(getFormulation(s_, s__, controller, environment(*envtransitionVars), guarantee(*s_), W0__, "reachability"), guarantee(*s))
        g =Goal()
        g.add(And(WPW, q>=0, q<=2))
        print("Projecting H1")
        WPW = tactic_qe_fixpoint(g).as_expr()
        print(WPW)
        # print(W0_)
        # print(W0__)
        # exit()
        j = 1

        H0 = And(False)
        H1 = And(False)

        while True:
            print("Sub-Iteration", j )
            H0 = H1
            #Substitute current variables with post variables
            H0__ = substitute(H0, *substList)
            H0_ = substitute(H0, *substList_)
            print("Getting projection of WPW")
            # WPH = Exists(s_+[q_], And(controller, automaton(q,q_,*s), And(q_==2, s_[0]==1) ))
            WPH = Exists(s_+[q_], And(controller, automaton(q,q_,*s),ForAll(s__+[q__], Implies(And(environment(*envtransitionVars), automaton(q_,q__,*s_)), H0__)) ))
            # WPH = ForAll(s__+[q__], Implies(And(environment(*envtransitionVars), automaton(q_,q__,*s_)), q__ == 0))
            # WPH = getFormulation(s_, s__, controller, environment(*envtransitionVars), H0_, H0__, "reachability")
            # H1 = Not(And(Not(WPH), Not(WPW)))
            g =Goal()
            # g.add(Exists(q, And(WPH, q ==2)))
            g.add(And(WPH))
            # print("Projecting H1")
            WPH = tactic_qe_fixpoint(g).as_expr()
            # print(WPH)
            # exit()

            H1 = And(Or(WPH, WPW))

            g =Goal()
            g.add(Exists(q, And(H1, q ==2)))
            # print("Projecting H1")
            # print(tactic_qe_fixpoint(g).as_expr())

            j = j + 1
            print("Checking validity of H1")
            if valid(Implies(H1, H0),0):
            # if j == 3:
                break
        # exit()
        W1 = H0
        # W1 = And(H0, W1)
        i = i + 1
        print("Checking validity of W1")
        if valid(Implies(W0, W1),0):
            break

    print("")
    print("Number of iterations: ", i-1)
    print("")

    g =Goal()
    g.add(Exists(q, And(W0, q ==1)))
    W0 = tactic_qe_fixpoint(g).as_expr()

    print("Invariant: ", W0)
    #3. Output: Controller Extraction or Unrealizable

    if not satisfiable(W0,0):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")

    print("")
    print("Number of iterations: ", i-1)
    print("")

def cobuchi_fixedpoint(controller_moves, environment, guarantee, mode, automaton, isFinal, nQ, game_type):
    print("Co-Buchi Fixed Point Computation")

    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variables s,g in the code because it will get redeclared in this scope. This is a problem.
            exec(str(var) +"= "+game_type+"('"+str(var) +"')") in globals(), locals()
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

    # # Guarantee over the deterministic automaton states for a given k
    # def guarantee_automaton(q):
    #     #Hard coded for now
    #     return q==0 

    # Combine above constraint with the optional safety guarantee, if any
    # def guarantee_(s, q):
    #     return And(guarantee(*s), guarantee_automaton(q))
    def guarantee_(s, q):
        return And(True, guarantee(q))
    
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
    
    i = 1

    W0 = guarantee_(*s, q)
    W1 = guarantee_(*s, q)

    while True:
        print("Iteration", i )
        W0 = W1
        # Substitute current variables with post variables
        W0_ = substitute(W0, *substList)
        
        # Game Formulation for the safety game
        # W1 = And(getFormulation(s_, s__, controller, environment(*envtransitionVars), guarantee(*s_), W0_, "safety"), guarantee(*s))
        W1 = Exists(s_+[q_], And(controller, automaton(q,q_,*s), guarantee_(*s_, q_), ForAll(s__+[q__], Implies(And(environment(*envtransitionVars), automaton(q_,q__,*s_)), W0_))))
        g = Goal()
        g.add(W1)
        W1 = tactic_qe_fixpoint(g).as_expr()

        i = i + 1
        if valid(Implies(W0, W1),0):
            break

    W0 = W0
    W1 = W0

    while True:
        print("Iteration", i )
        W0 = W1
        # Substitute current variables with post variables
        W0_ = substitute(W0, *substList)
        
        # Game Formulation for the safety game
        # W1 = Or(getFormulation(s_, s__, controller, environment(*envtransitionVars), guarantee(*s_), W0_, "reachability"), guarantee(*s))
        W1 = Exists(s_+[q_], And(controller, automaton(q,q_,*s), Or(guarantee_(*s_, q_), ForAll(s__+[q__], Implies(And(environment(*envtransitionVars), automaton(q_,q__,*s_)), W0_))) ))
        g = Goal()
        g.add(W1)
        W1 = tactic_qe_fixpoint(g).as_expr()

        i = i + 1
        if valid(Implies(W1, W0),0):
            break

    #3. Output: Controller Extraction or Unrealizable

    if not satisfiable(W0,0):
        print("Invariant is Unsatisifiable i.e. False")
        print("UNREALIZABLE")
    else:
        print("Invariant is Satisfiable")
        print("REALIZABLE")

    print("")
    print("Number of iterations: ", i-1)
    print("")

    # print("Invariant: ")
    # g = Goal()
    # g.add(Exists(q, And(W0, q == 1)))
    # W1 = tactic_qe_fixpoint(g).as_expr()
    # print(W1)


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# 2. LTL Fixed-Point Procedures without Sigma (On The Fly Determinization, Antichain):
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
# 2.1. On The Fly Determinization Approach (OTFD) for LTL specs: Non-sigma version
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

def otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, mode, automaton, isFinal, sigma, nQ, k, game_type):

    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variables s,g in the code because it will get redeclared in this scope. This is a problem.
            exec(str(var) +"= "+game_type+"('"+str(var) +"')") in globals(), locals()
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
    init = And(c[0] == 0, And([c[q] == -1 for q in range(1,nQ)]))

    if not satisfiable(And(F, init),0):
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

# --------------------------------------------
# 2.2. Antichain Approach for LTL specs: non sigma
# --------------------------------------------
        
def omega_nonsigma(c_, s, c, automaton, isFinal):

    # 1. Determinization constraint

    # det = ForAll([q,x], Implies(And(automaton(p,q,x), sig, c_(q) != -1), c(p) <= max(c_(q) - isFinal(q) , -1) ))
    det = And([And([Implies(automaton(p,q, *s), c[p] <= max(c_[q] - isFinal(q) , -1) ) for q in range(0, len(c_))]) for p in range(0, len(c)) ])
    
    # 2. Reachability constraint

    # reach = Exists([q,x], And(automaton(p,q,x), sig, c(p) == max(c_(q) - isFinal(q) , -1) ))
    reach = And([Or([And(automaton(p,q,*s), c[p] == max(c_[q] - isFinal(q) , -1) ) for q in range(0, len(c_))]) for p in range(0, len(c))])

    return And(det, reach)

def antichain_fixedpoint_nonsigma(controller_moves, environment, guarantee, mode, automaton, isFinal, sigma, nQ, k, game_type):

    # Define Omega function for determinization (depends on omega (depends on max))
    
    #Get states from environment
    s=[]
    for var in environment.__code__.co_varnames:
        if not str(var).__contains__("_"):
            #Dynamic variable declaration
            #Issue: Can't use variable s in the code because it will get redeclared in this scope.
            exec(str(var) +"= "+game_type+"('"+str(var) +"')") in globals(), locals()
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

    # Retrive determinized predicate list
    # sigma = sigma(*s)
    
    # print("Projecting Omega to store")
    # # Stores projected omega in a different array (indexed by the same index as sigma) so that project is not called always again and again.
    # # This improves the speed by 2X
    # projected_omega = [project(omega(c_,sigma[i],c, automaton, isFinal, s)) for i in range(len(sigma))]

    # def Omega(c__subst, x_subst, c_subst):
    #     #Project quantifers in Omega before forwarding to wpAssertion.
    #     return Or([And( substitute(sigma[i], [(s[j], x_subst[j]) for j in range(len(s))] ), substitute(projected_omega[i], [(c[j], c_subst[j]) for j in range(len(c))] + [(c_[j], c__subst[j]) for j in range(len(c_))] ) ) for i in range(len(sigma))])

    # Define the guarantee that we will use

    # Gurantee over the deterministic automaton states for a given k, using antichains
    def guarantee_automaton_antichain(c):
        # Bounds on the range of the deterministic automaton states (functions)
        init = And([c[q] == k for q in range(0, len(c))])
        return And(init)

    # Combine above constraint with the optional safety guarantee, if any
    def guarantee_antichain_(s, c):
        return And(guarantee(*s), guarantee_automaton_antichain(c))

    print("Getting Formulation")
    # Decide formulation based on game mode
    # Declare and define transition variables list for controller and environment, depending on the mode
    if(mode == 1):
        # getFormulation = getFormulationAE_omega
        contransitionVars = s_+s__
        envtransitionVars = s+s_
    else: 
        if(mode == 0):
            # getFormulation = getFormulationEA_omega
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

    envPre = And(True)
    # print_automaton_states(guarantee_antichain_(s__,c__), c__, nQ)
    # for move in range(0, len(sigma)):
    # projected_omega_i = substitute(projected_omega[move], [(c[j], c_[j]) for j in range(len(c))] + [(c_[j], c__[j]) for j in range(len(c_))] )
    # sigma_i = substitute(sigma[move], [(s[j], s_[j]) for j in range(len(s))] )
    # envPre_ = Exists(c__, And( Exists(s__, And(projected_omega_i, guarantee_antichain_(s__,c__)) ) , ForAll(s__, Implies(And(sigma_i, environment(*envtransitionVars)), guarantee_antichain_(s__,c__)) )))
    # envPre_ = ForAll(c__+s__, Implies(And(projected_omega_i, sigma_i, environment(*envtransitionVars)), guarantee_antichain_(s__,c__)) )
    envPre_ = Exists(c__, And(omega_nonsigma(c__, s_, c_, automaton, isFinal), ForAll(s__, Implies(environment(*envtransitionVars), guarantee_antichain_(s__,c__)))) )
    g =Goal()
    g.add(envPre_)
    envPre_ = tactic_qe_fixpoint(g).as_expr()
    envPre = glb(envPre, envPre_, s_, c_, nQ, game_type)
    
    # envPre = And(envPre, guarantee_antichain_(s_,c_))
    envPre = maximal(envPre,s_, s__, c_, c__, nQ)
    #Project envPre(s_,c_)
    g =Goal()
    g.add(envPre)
    conPost = tactic_qe_fixpoint(g).as_expr()
    # print_automaton_states(conPost, c_, nQ)
    # exit()
    wp = Exists(s_+c_, And(omega_nonsigma(c_, s, c, automaton, isFinal), controller, conPost))
    wp = maximal(wp, s, s_, c, c_, nQ)
    g =Goal()
    g.add(wp)
    wp = tactic_qe_fixpoint(g).as_expr()
    # print_automaton_states(wp, c, nQ)

    W = wp
    F = guarantee_antichain_(s,c)

    i = 1
    print("Iteration", i )
    i = i + 1

    while(not valid(Implies(F, W),0)):
        temp = W
        W = substitute(W, *substList+[(c[j], c__[j]) for j in range(nQ)])

        # Compute envPre for each move separately.

        envPre = And(True)

        # for move in range(0, len(sigma)):
            # projected_omega_i = substitute(projected_omega[move], [(c[j], c_[j]) for j in range(len(c))] + [(c_[j], c__[j]) for j in range(len(c_))] )
            # sigma_i = substitute(sigma[move], [(s[j], s_[j]) for j in range(len(s))] )
            # envPre_ = Exists(c__, And( Exists(s__, And(projected_omega_i, W) ) , ForAll(s__, Implies(And(sigma_i, environment(*envtransitionVars)), W) )))
            # envPre_ = ForAll(c__+s__, Implies(And(projected_omega_i, sigma_i, environment(*envtransitionVars)), W) )
        envPre_ = Exists(c__, And(omega_nonsigma(c__, s_, c_, automaton, isFinal), ForAll(s__, Implies(environment(*envtransitionVars), W))) )
        g =Goal()
        g.add(envPre_)
        envPre_ = tactic_qe_fixpoint(g).as_expr()
        envPre = glb(envPre, envPre_, s_, c_, nQ, game_type)

        # envPre = And(envPre, guarantee_antichain_(s_,c_))
        envPre = maximal(envPre,s_, s__, c_, c__, nQ)
        #Project envPre(s_,c_)
        g =Goal()
        g.add(envPre)
        conPost = tactic_qe_fixpoint(g).as_expr()
        # print_automaton_states(conPost, c_, nQ)
        # exit()

        # # The order of disjunction and maximality doesn't matter here! Why is the extra state coming?
        # conPre = Or(False)

        # for move in range(0, len(sigma)):
        #     projected_omega_i = substitute(projected_omega[move], [(c[j], c[j]) for j in range(len(c))] + [(c_[j], c_[j]) for j in range(len(c_))] )
        #     sigma_i = substitute(sigma[move], [(s[j], s[j]) for j in range(len(s))] )
        #     # envPre_ = Exists(c__, And( Exists(s__, And(projected_omega_i, W) ) , ForAll(s__, Implies(And(sigma_i, environment(*envtransitionVars)), W) )))
        #     # envPre_ = ForAll(c__+s__, Implies(And(projected_omega_i, sigma_i, environment(*envtransitionVars)), W) )
        #     conPre_ = Exists(s_+c_, And(projected_omega_i, sigma_i, controller, conPost))
        #     g =Goal()
        #     g.add(conPre_)
        #     conPre_ = tactic_qe_fixpoint(g).as_expr()
        #     conPre = Or(conPre, conPre_)
        #     conPre = maximal(conPre, s, s_, c, c_, nQ)

        # wp = conPre

        wp = Exists(s_+c_, And(omega_nonsigma(c_, s, c, automaton, isFinal), controller, conPost))
        g =Goal()
        g.add(wp)
        wp = tactic_qe_fixpoint(g).as_expr()
        wp = maximal(wp, s, s_, c, c_, nQ)
        # print_automaton_states(wp, c, nQ)
        W = wp
        F = temp
        print("Iteration", i )
        i = i + 1
        # exit()

    # print("Invariant is")
    # wp = maximal(wp, s, s_, c, c_, nQ)
    # print_automaton_states(wp, c, nQ)

    start_val = Int('start_val')
    init = Exists(start_val, c[0]!=-1)

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
        # print(F)
        g = Goal()
        
        g.add(Exists(c, F))
        PF = tactic_qe_fixpoint(g).as_expr()
        # print("Projected invariant is: ")
        # print(PF)

        g.add(Exists(c, And(F, init)))
        PF = tactic_qe_fixpoint(g).as_expr()
        print("Projected invariant for initial state is: ")
        print(PF)

    print("")
    print("Number of iterations: ", i-1)
    print("")