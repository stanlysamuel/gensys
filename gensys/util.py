# Viewing automaton as a graph with edges labelled with boolean formulae.
# Represented as an adjacency list.
# Regular adjacency lists use dict+set. We use dict+dict as we need to index into destination vertex to get the edge label.
# Author: Stanly Samuel

import spot

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

    def determinize(self, k):
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
                print("("+spot.bdd_to_formula(self.adj_list[src_vertex][dest_vertex],self.bdict).to_str()+", "+ str(dest_vertex)+")", end =" ")
            print()