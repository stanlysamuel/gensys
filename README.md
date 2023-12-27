# GenSys-LTL (GenSys 2.0)
This branch hosts the code for the tool: GenSys-LTL (i.e., [GenSys](https://github.com/stanlysamuel/gensys) Version 2.0), based on our [ASE 2023 paper](https://conf.researchr.org/details/ase-2023/ase-2023-papers/101/Symbolic-Fixpoint-Algorithms-for-Logical-LTL-Games): *Symbolic Fixpoint Algorithms for Logical LTL Games.*

## Introduction 

GenSys-LTL is an *infinite-state* reactive synthesis solver using LTL specifications. GenSys-LTL uses the Z3 theorem prover by Microsoft Research for solving and projecting SMT formulae. GenSys-LTL is scalable and is validated on standard benchmarks with compelling results.

For the extended arXiv version of the [ASE 2023 paper](https://conf.researchr.org/details/ase-2023/ase-2023-papers/101/Symbolic-Fixpoint-Algorithms-for-Logical-LTL-Games), please see [this paper](https://arxiv.org/abs/2306.02427) titled: *Towards Efficient Controller Synthesis Techniques for Logical LTL Games*.

## Author

- Stanly Samuel, Indian Institute of Science, Bangalore

## Mentored by

- Prof. Deepak D'Souza, Indian Institute of Science, Bangalore
- Prof. Raghavan Komondoor, Indian Institute of Science, Bangalore

## Installation
You should have Python 3 installed on your system. We successfully ran GenSys-LTL with Python 3.10.12.

**Install Python packages**

```
pip install z3-solver
```

**Add base project directory to PYTHONPATH**

```
export PYTHONPATH=${PYTHONPATH}:/path/to/gensys
```

### Usage

**Setup GenSys-LTL**

```
git clone https://github.com/stanlysamuel/gensys.git

git checkout gensys-ltl
```

**Run Benchmarks**

The benchmarks for the ASE 2023 paper are contained in gensys/benchmarks/. 
The GenSys-LTL library and helper functions are contained in gensys/gensys/.

## Replicating Results for the ASE 2023 paper

Running the command
```
python3 run_experiments.py
```

will run all the benchmarks for simple, product, and otf fixpoints; the results will be stored in `./results.csv`. This process may take few hours (2 hours on an i7-8700 machine with 64GB RAM). Documentation explaining each benchmark is present in the file.

### Notes: 
- Although we require the Spot tool to convert LTL formulas into buchi automata, for this version of GenSys, this process is done manually and hence the input to GenSys-LTL is a buchi automaton and not an LTL formula. If the user wishes to encode custom LTL formulas, they must replace predicates with propositions, feed the resulting propositonal LTL formula to Spot, and replace the propositions in the resulting Buchi automaton to the corresponding predicates, manually. Future versions of GenSys will automate this. The version of Spot we used is version 2.9.8 and is present in `./tools/spot-2.9.8`.
- For the OTF results, we manually iterate to the correct value of k that is required. This process will be automated in a future version of GenSys.

## Rules for creating your own game

### Simple Games

GenSys-LTL provides API's to model many various versions of logical LTL games. The first version of GenSys could only model safety games and provided the following API:
```
safety_fixedpoint(controller_moves, environment, guarantee, mode)
```
The details for the above API are mentioned [here](https://github.com/stanlysamuel/gensys/blob/main/README.md), and is deprecated in this version. In GenSys-LTL, the above safety fixpoint now has the form:
```
safety_fixedpoint_gensys(controller_moves, environment, guarantee, mode, game_type, init)
```
- The API now allows the variables to have specific types and is denoted by the `game_type` variable that can range over the values `Int`, `Real`, or `Bool`. It is imperative that for the game type that we consider, quantifier elimination is decidable for the corresponding first order logic theory. At this point, all variables are assigned a single type. This restriction will be removed in future versions.
- We can now also specify initial conditions using predicates; the `init` field denotes this and is in the format similar to the `environment` field.
- Other API's are `reachability_fixedpoint_gensys`, `buchi_fixedpoint_gensys`, and `co-buchi_fixedpoint_gensys` that have the same signature as `safety_fixedpoint_gensys`, but handle LTL formulas of the form F(X), GF(X), and FG(X) respectively.
- Mode can be ignored in this version and is always filled with 0 i.e., controller plays first (Moore semantics).

### Product Games

GenSys-LTL provides the following API's to solve any LTL formula whose resulting buchi or co-buchi automaton is deterministic:

```
buchi_fixedpoint(controller_moves, environment, guarantee, mode, automaton, final_states, automaton_states, game_type, init)

co-buchi_fixedpoint(controller_moves, environment, guarantee, mode, automaton, final_states, automaton_states, game_type, init)
```

- `automaton` requires the automaton to be provided in a logical format
- `final_states` provides information regarding the final states of the automaton
- `automaton_states` is an integer representing the number of automaton states.
- These values can be manually encoded using the information from the Spot tool. Future versions of GenSys will automate this.

### General LTL Games

If the LTL formula has no deterministic automaton, we use an on-the-fly determinization based fixpoint technique. The API's are:

```
otfd_fixedpoint(controller_moves, environment, guarantee, mode, automaton, final_states, sigma, automaton_states, K, game_type, init)

otfd_fixedpoint_nonsigma(controller_moves, environment, guarantee, mode, automaton, final_states, sigma, automaton_states, K, game_type, init)
```

The new parameters are:
- `K` that computes the fixpoint based on the value of K reuired in the determinized k-safety automaton.
- `sigma` is a partition over all the predicates in the automaton. This field is only required for the first function `otfd_fixedpoint`. This is a heuristic and performance improvement varies for certain benchmarks. More investigation is required to know the reason behind this behaviour in the benchmarks.


## Related Papers

1. [ESEC/FSE 2021](https://github.com/stanlysamuel/gensys): *GenSys: A Scalable Fixed-Point Engine for Maximal Controller Synthesis over Infinite State Spaces*
2. [ASE 2023](https://conf.researchr.org/details/ase-2023/ase-2023-papers/101/Symbolic-Fixpoint-Algorithms-for-Logical-LTL-Games): *Symbolic Fixpoint Algorithms for Logical LTL Games*
3. [Extended arXiv version of ASE 2023 paper](https://arxiv.org/abs/2306.02427) : *Towards Efficient Controller Synthesis Techniques for Logical LTL Games*.