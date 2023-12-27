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

will run all the benchmarks for simple, product, and otf fixpoints; the results will be stored in `./results.csv`. This process may take few hours (~3 hours). Documentation explaining each benchmark is present in the file.

### Notes: 
- Although we require the Spot tool to convert LTL formulas into buchi automata, for this version of GenSys, this process is done manually and hence the input to GenSys-LTL is a buchi automaton and not an LTL formula. If the user wishes to encode custom LTL formulas, they must replace predicates with propositions, feed the resulting propositonal LTL formula to Spot, and replace the propositions in the resulting Buchi automaton to the corresponding predicates, manually. Future versions of GenSys will automate this. The version of Spot we used is version 2.9.8 and is present in `./tools/spot-2.9.8`.
- For the OTF results, we manually iterate to the correct value of k that is required. This process will be automated in a future version of GenSys.

## Related Papers

1. [ESEC/FSE 2021](https://github.com/stanlysamuel/gensys): *GenSys: A Scalable Fixed-Point Engine for Maximal Controller Synthesis over Infinite State Spaces*
2. [ASE 2023](https://conf.researchr.org/details/ase-2023/ase-2023-papers/101/Symbolic-Fixpoint-Algorithms-for-Logical-LTL-Games): *Symbolic Fixpoint Algorithms for Logical LTL Games*
3. [Extended arXiv version of ASE 2023 paper](https://arxiv.org/abs/2306.02427) : *Towards Efficient Controller Synthesis Techniques for Logical LTL Games*.