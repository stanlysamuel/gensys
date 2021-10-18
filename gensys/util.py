# Viewing automaton as a graph with edges labelled with boolean formulae.
# Represented as an adjacency list.
# Regular adjacency lists use dict+set. We use dict+dict as we need to index into destination vertex to get the edge label.
# Author: Stanly Samuel

import collections
import spot
import buddy

class Graph:
    # vertex_list: Set of vertices
    # edge_list: Set of edges of the form (V, F, V)
    # init_state: Initial state
    # final_states: Final states
    # is_det: Deterministic?
    # ap: Atomic propositions. Spot formula
    # bdict: bdd dictionary for the boolean formulae
    def __init__(self, vertex_list, edge_list, init_state, final_states, is_det, ap, bdict):
        self.init_state = init_state
        self.final_states = final_states
        self.is_det = is_det
        self.adj_list = {}
        self.ap = ap #Spot formula
        self.bdict = bdict 
        for vertex in vertex_list:
            self.adj_list[vertex] = {}
        for edge in edge_list:
            self.add_edge(edge[0], edge[1], edge[2])

    def add_edge(self, v1, f, v2):
        self.adj_list[v1][v2] = f

    # Function to merge states with counters
    def merge_states(self, state1, state2):
        merged_state = state1
        for key in state2.keys():
            if key in merged_state.keys():
                merged_state[key] = max(merged_state[key], state2[key])
            else:
                merged_state[key] = state2[key]
        # print(merged_state)
        return merged_state

    # Function to check if a state is unique.
    # A unique state is the one where the key set is different from the ones in the current set.
    # If a state is not unique, then they must be merged and assigned the same number.
    # state: Int -> Int, states: Int -> Int -> Int

    # Some major error when keys are equal. Shouldn't occur in the algorithm though
    def merge_if_not_unique(self, state, states):
        # Create a copy
        new_states = {}
        for state_number in states.keys():
            if states[state_number].keys() == state.keys():
                print(new_states)
                print(state_number)
                new_states[state_number] = self.merge_states(state, states[state_number])
                print(new_states)
            else:
                new_states[state_number] = states[state_number]
        return new_states

    # Implication for spot formulae
    def implies(f, g):
        a_f = f.translate()
        a_ng = spot.formula.Not(g).translate()
        return spot.product(a_f, a_ng).is_empty()
    
    def edge_in_transition(self, edge, transition):
        a_edge = edge.translate()
        a_transition = transition.translate()
        return not spot.product(a_edge, a_transition).is_empty()

    # f = spot.formula("(a U b) U a")
    # g = spot.formula("b U a")
    # print("Equivalent" if equiv(f, g) else "Not equivalent")


    # Python3 program to find all subsets
    # by backtracking.
    
    # In the array A at every step we have two
    # choices for each element either we can
    # ignore the element or we can include the
    # element in our subset
    global transitions
    def subsetsUtil(self, A, subset, index):
        #The positive literals
        positive_literals = subset
        #Get the formulae to negate
        negative_literals = list(set(self.ap) - set(subset))
        # print(negative_literals.count)
        # Final subset
        # Here I can create the map of z3 variables and print
        final_subset = positive_literals + [spot.formula_Not(x) for x in negative_literals]
        # print(final_subset)
        self.transitions.append(spot.formula_And(final_subset))

        for i in range(index, len(A)):
            # include the A[i] in subset.
            subset.append(A[i])
            
            # move onto the next element.
            self.subsetsUtil(A, subset, i + 1)
            
            # exclude the A[i] from subset and
            # triggers backtracking.
            subset.pop(-1)
        return
    
    # below function returns the subsets of vector A.
    def subsets(self,A):
        self.transitions = []
        subset = []
        
        # keeps track of current element in vector A
        index = 0
        self.subsetsUtil(A, subset, index)
        return self.transitions
        
    # Driver Code
    
    # find the subsets of below vector.
    # array = [1, 2, 3]
    
    # # res will store all subsets.
    # # O(2 ^ (number of elements inside array))
    # # because at every step we have two choices
    # # either include or ignore.
    # subsets(array)

    def determinize(self, k):
        # In the deterministic automaton, each state is a dictionary from s -> count
        # Now dictionaries (and even lists) cannot be used as a hash key in another dictionary.
        # So create a separate dictionary that maps integers to the state dictionary. We will need this to create the constraints anyway.

        # List of dictionaries work for us as comparison of dictionaries do not assume order
        x = {0:5, 1:2}
        y = {1:2, 0:6}
        print(x==y)
        # States representation
        z = {0:x,1:y} 
        print(z)
        # print({1:2, 0:5} in z)
        # print(self.merge_states(y, x))
        print(self.merge_if_not_unique({1:3, 0:5}, z))

        #BDD Implies
        # print(buddy.bdd_implies(self.adj_list[0][1], spot.formula_to_bdd(self.ap[0], self.bdict)))
        # print(spot.bdd_to_formula(self.adj_list[0][2], self.bdict))
        
        init_state_d = {}
        final_states_d = {}
        if self.init_state in self.final_states:
            init_state_d[self.init_state] = 1
        else:
            init_state_d[self.init_state] = 0

        # States of the deterministic automaton: Int -> Counter State Dict
        states = {}
        #Initial state is numbered 0
        states[0] = init_state_d
        state_count = 1
        
        #Both contain integers only from 0 onwards.
        visited_states = []
        unprocessed_states = collections.deque()
        unprocessed_states.append(0)

        # Deterministic automaton in adjacency list format.
        # Int -> Transition set (DNF) -> Int
        # Can get Z3 formula directly from it
        # Countered states are not required here.
        adj_list_d = {}

        #Find how to check SAT in spot formula
        # are_eq = spot.implication("a", "a")
        # print("Equivalent" if are_eq else "Not equivalent")
        # spot.implies("a","a")
        #Make all combinations of transitions
        transitions = self.subsets(self.ap)
        # print(transitions)
        while unprocessed_states:
            processing_state_number = unprocessed_states.popleft()
            adj_list_d[processing_state_number] = {}
            visited_states.append(processing_state_number)
            #Create the state number in the final list
            adj_list_d[processing_state_number] = {}
            #Proceed only if non final. Else ignore.
            print("CURRENT STATE IS ", processing_state_number)
            print(states[processing_state_number])
            for src_vertex in states[processing_state_number].keys():
                print("CURRENT SOURCE STATE IS ", src_vertex)
                # For all 2^AP combinations
                for transition in transitions:
                    print("T",transition)
                    dest_vertex_d = {}
                    # print(states)
                    # print(states[processing_state_number])
                    # print(states[processing_state_number][0])
                    # print(self.adj_list[states[processing_state_number][0]])
                    # edges = self.adj_list[states[processing_state_number][src_vertex]]
                    edges = self.adj_list[src_vertex]
                    
                    # For each edge e in automata i.e. (src_vertex, e, dest_vertex)
                    for dest_vertex in edges:
                        edge = spot.bdd_to_formula(edges[dest_vertex], self.bdict)
                        print("E", edge)
                        if self.edge_in_transition(edge, transition):
                            # print("Edge present in transition")
                            if dest_vertex in self.final_states:
                                incr = 1
                            else:
                                incr = 0

                            # dest_vertex_d[dest_vertex] = max(dest_vertex_d[dest_vertex],min(k+1,processing_state_number[0]))
                            #(Q: Why not Min Max)
                            dest_vertex_d[dest_vertex] = min(k+1, states[processing_state_number][src_vertex] + incr)
                    print("Dest vertex")
                    print(dest_vertex_d)

                    #Check if generated state is unique
                    if dest_vertex_d in states.values():
                        print("Present")
                        #Get key from value dest_vertex_d
                        new_state_count = list(states.keys())[list(states.values()).index(dest_vertex_d)]
                        print(new_state_count)
                    else:
                        print("Not present")
                        #New state is generated, incrememnt state counter, add to states dict. Get the new state number. Add to unprocessed list.
                        states[state_count] = dest_vertex_d
                        new_state_count = state_count
                        #Add to unprocessed even if final state. Nah. Check is done iniitally. But add such state to final
                        unprocessed_states.append(new_state_count)
                        state_count+=1

                    # Use state number to create the transition set.
                    # Parallel transitions are possible in this graph.
                    if new_state_count not in adj_list_d[processing_state_number]:
                        adj_list_d[processing_state_number][new_state_count] = set()
                        adj_list_d[processing_state_number][new_state_count].add(transition)
                    else:
                        adj_list_d[processing_state_number][new_state_count].add(transition)
                print(states)
                print(adj_list_d)     
                # if dest_vertex_d not in visited: #(may have to create eq check)
                    # unprocessed.append(dest_vertex_d)
        # print(states)
        # print(adj_list_d)  
        return None

    def display(self):
        print("UCW details: ")
        print("Initial State: {}".format(self.init_state))
        print("Final States: {}".format(self.final_states))
        print("Is deterministic? {}".format(self.is_det))
        print("Atomic propositions: {}".format(self.ap))
        print("Transitions:")
        for src_vertex in self.adj_list:
            print(str(src_vertex) + " -> ", end =" ")
            for dest_vertex in self.adj_list[src_vertex]:
                # Edge label as BDD string
                # print("("+spot.bdd_format_formula(self.bdict,edge[0])+", "+ str(edge[1])+")", end =" ")
                # Edge label as spot.formula string
                print("("+str(dest_vertex)+", "+spot.bdd_to_formula(self.adj_list[src_vertex][dest_vertex],self.bdict).to_str()+")", end =" ")
            print()