# from IPython.display import display
import spot
import buddy
from  gensys.util import *

#Custom print
def custom_print(aut):
    bdict = aut.get_dict()
    print("Acceptance:", aut.get_acceptance())
    print("Number of sets:", aut.num_sets())
    print("Number of states: ", aut.num_states())
    print("Initial states: ", aut.get_init_state_number())
    # print("Atomic propositions:", end='')
    # for ap in aut.ap():
    #     print(' ', ap, ' (=', bdict.varnum(ap), ')', sep='', end='')
    print()
    # Templated methods are not available in Python, so we cannot
    # retrieve/attach arbitrary objects from/to the automaton.  However the
    # Python bindings have get_name() and set_name() to access the
    # "automaton-name" property.
    name = aut.get_name()
    if name:
        print("Name: ", name)
    print("Deterministic:", aut.prop_universal() and aut.is_existential())
    print("Unambiguous:", aut.prop_unambiguous())
    print("State-Based Acc:", aut.prop_state_acc())
    print("Terminal:", aut.prop_terminal())
    print("Weak:", aut.prop_weak())
    print("Inherently Weak:", aut.prop_inherently_weak())
    print("Stutter Invariant:", aut.prop_stutter_invariant())

    for s in range(0, aut.num_states()):
        print("State {}:".format(s))
        for t in aut.out(s):
            print("  edge({} -> {})".format(t.src, t.dst))
            # bdd_print_formula() is designed to print on a std::ostream, and
            # is inconvenient to use in Python.  Instead we use
            # bdd_format_formula() as this simply returns a string.
            print("    label =", spot.bdd_format_formula(bdict, t.cond))
            print("    acc sets =", t.acc)

# Extract relevant automaton info for GenSys
def extract_aut_info(aut):
    init_state = aut.get_init_state_number()
    is_det = aut.prop_universal() and aut.is_existential()
    bdict = aut.get_dict()
    ap = aut.ap()
    vertex_list = []
    edge_list = []
    final_states = []
    for s in range(0, aut.num_states()):
        # state_is_accepting makes only sense for automata using state-based
        # acceptance, and a simple acceptance condition like Buchi or
        # co-Buchi.
        # Found in twgraph.hh
        if aut.state_is_accepting(s):
            final_states.append(s)
        vertex_list.append(s)
        for t in aut.out(s):
            edge_list.append((t.src, t.cond, t.dst))
    return (vertex_list, edge_list, init_state, final_states, is_det, ap, bdict)


#These 4 test cases are enough to test the basic LTL approaches without inputs.
print("ALTERNATING EXAMPLE")
f1 = spot.formula.Not('G (a -> X !a)')
automata1 = f1.translate('BA', 'complete', 'sbacc')
# custom_print(automata1) #Print 1
# print(spot.translate('!(G (a -> X !a))', 'BA').to_str('spin')) #Print 2
g = Graph(*extract_aut_info(automata1))
g.display() # Print 3
print()

print("SAFETY")
f2 = spot.formula.Not('G p')
automata2 = f2.translate('BA', 'complete','sbacc')
# custom_print(automata2)
g = Graph(*extract_aut_info(automata2))
g.display() # Print 3
# g.determinize(2)
print()

print("2 FLOOR EXAMPLE")
f3 = spot.formula.Not('G p & G(F x1 & F x2)')
automata3 = f3.translate('BA', 'complete', 'sbacc')
# custom_print(automata3)
g = Graph(*extract_aut_info(automata3))
g.display() # Print 3
# g.determinize(1)
print()

# determinize works for simple examples.
# For two floors and k=2, it blows up a lot! check if merge works properly
# Deletion of redundant states after merge causes some issue. Do check once.
# Add Test Case automaton graphs manually to test the determinize procedure properly.
# add the conversion step from spot formula to GenSys.

#2.4secs
print("3 FLOOR EXAMPLE")
f4 = spot.formula.Not('G p & G(F x1 & F x2 & F x3)')
automata4 = f4.translate('BA', 'complete', 'sbacc')
# custom_print(automata4)
g = Graph(*extract_aut_info(automata4))
g.display() # Print 3
# g.determinize(1)
print()

#1m17sec
# print("5 FLOOR EXAMPLE")
# f5 = spot.formula.Not('G p & G(F x1 & F x2 & F x3 & F x4 & F x5)')
# automata5 = f5.translate('BA', 'complete', 'sbacc')
# # custom_print(automata4)
# g = Graph(*extract_aut_info(automata5))
# g.display() # Print 3
# g.determinize(4)
# print()

print("REACHABILITY")
f6 = spot.formula.Not('F p')
automata6 = f6.translate('BA', 'complete','sbacc')
# custom_print(automata2)
g = Graph(*extract_aut_info(automata6))
g.display() # Print 3
# g.determinize(2)
print()

print("BUCHI")
f7 = spot.formula.Not('GF p')
automata7 = f7.translate('BA', 'complete','sbacc')
# custom_print(automata2)
g = Graph(*extract_aut_info(automata7))
g.display() # Print 3
# g.determinize(2)
print()

print("BUCHI")
f8 = spot.formula.Not('GF p0 | (GF p2 & !GF p0 & !GF p1)')
automata8 = f8.translate('BA', 'complete','sbacc')
# custom_print(automata2)
g = Graph(*extract_aut_info(automata8))
g.display() # Print 3
# g.determinize(2)
print()

print("Prop 2")
f8 = spot.formula.Not('G (r -> XF g)')
automata8 = f8.translate('BA', 'complete','sbacc')
# custom_print(automata2)
g = Graph(*extract_aut_info(automata8))
g.display() # Print 3
# g.determinize(2)
print()

#Unbeast uses Spot for symbolic bounded synthesis using BDD's. Any algorithm that can be used?

#Method to determinize a given UCW for the given k
def determinize(automaton, k):
    print("Determinize")

#Method to generate constraints from a given game graph
def constructConstraints(safetyGame):
    print("Constraints Generated")

#Creates the final game for GenSys
def createGenSysProductGame(automataConstraints, con, env):
    print("Final Game")

#Can be used to compare with the map
# ap = spot.atomic_prop_collect(f)
# print(ap)
# automata.ap() is also enough

# print(automata.to_str())
# print(automata.is_deterministic())

# b = buddy.bdd_ithvar(automata.register_ap('b'))
# for e in automata.edges():
#     print(e.cond)
#     print(e.acc)
#     print(e.src)
#     print(e.dst)
#     print(e.next_succ) #Seems like the BDD succesor
#     # e.cond &= b
# # for v in automata.vertices():
# #     print(v)

# # print(automata.to_str())