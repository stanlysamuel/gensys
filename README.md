# GenSys-LTL (GenSys 2.0)
This branch hosts the code for the tool: GenSys-LTL (i.e., [GenSys](https://github.com/stanlysamuel/gensys) Version 2.0), based on our [ASE 2023 paper](https://conf.researchr.org/details/ase-2023/ase-2023-papers/101/Symbolic-Fixpoint-Algorithms-for-Logical-LTL-Games): *Symbolic Fixpoint Algorithms for Logical LTL Games.*

For the full arXiv version of the above paper, please see [this paper](https://arxiv.org/abs/2306.02427) titled: *Towards Efficient Controller Synthesis Techniques for Logical LTL Games*.

## Introduction 

GenSys-LTL is an *infinite-state* reactive synthesis solver using LTL specifications. GenSys-LTL uses the Z3 theorem prover by Microsoft Research for solving and projecting SMT formulae. GenSys-LTL is scalable and is validated on standard benchmarks with compelling results.

## Author

- Stanly Samuel, Indian Institute of Science, Bangalore

## Mentored by

- Prof. Deepak D'Souza, Indian Institute of Science, Bangalore
- Prof. Raghavan Komondoor, Indian Institute of Science, Bangalore

## Installation
You should have Python `3` installed on your system. We successfully ran GenSys-LTL on Ubuntu `22.04.3 LTS` with Python `3.10.12` and Z3 version `4.12.1 - 64 bit`.

**Install Python packages**

```
pip install z3-solver==4.12.1.0
```

The latest version of Z3 `4.12.4` is not supported.

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

### Using Docker
The easiest way to reproduce the results is by building and running a Docker image from the Dockerfile, as follows:

```
sudo docker build -t gensys-ltl .

sudo docker run -it gensys-ltl /bin/bash

/gensys# export PYTHONPATH=${PYTHONPATH}:/gensys 

/gensys# python3 run_experiments_with_raboniel.py
```
(If you do not wish to build the docker image, you could directly pull a prebuilt GenSys-LTL image from [Dockerhub](https://hub.docker.com/r/stanlysamuel/gensys-ltl) as well, using the command `sudo docker pull stanlysamuel/gensys-ltl` instead of `sudo docker build -t gensys-ltl .`).

The script `run_experiments_with_raboniel.py` runs the tools GenSys-LTL and Raboniel over all benchmarks and takes about 5 hours to run on an i7-8700 machine with 64GB RAM.  It is easier to run Raboniel in Docker (where Raboniel is setup); otherwise the user will have to follow the instructions in `tools/raboniel/raboniel/README.md` to setup Raboniel manually. The output for the above commands should look as follows:

```
/gensys# python3 run_experiments_with_raboniel.py 
Running Raboniel on Gensys-LTL benchmarks
1_cinderella2.tsl
2_cinderella3.tsl
3_repairlock.tsl
4_repaircritical.tsl
5_synthsynchronization.tsl
6_cinderella_reach.tsl
7_cinderella_gf.tsl
8_cinderella_gen.tsl
9_cinderella1999.tsl
10_repaircritical_gen.tsl
11_elevator3.tsl
12_elevator4.tsl
13_elevator5.tsl
14_elevator8.tsl
15_elevator10.tsl
16_watertanks_double_safety.tsl
17_watertank_single_liveness.tsl
18_sort3.tsl
19_sort4.tsl
20_sort5.tsl
21_box.tsl
22_box_limited.tsl
23_diagonal.tsl
24_evasion.tsl
25_follow.tsl
26_solitary_box.tsl
27_square.tsl
Raboniel results:
['-', 'T/O', 'T/O', 3.05, 'T/O', 'T/O', 'T/O', 'T/O', 'T/O', 'T/O', 'T/O', 1.91, 2.32, 5.18, 28.13, 110.44, 20.19, 51.4, 1.94, 649.9, 'T/O', 1.82, 0.4, 7.63, 4.89, 'T/O', 5.5, 167.97]
Running ASE 2023 Benchmark Suite. View results.csv for results.
1_cinderella-C2.py simple
1_cinderella-C2.py product-buchi
1_cinderella-C2.py product-co-buchi
1_cinderella-C2.py otf
2_cinderella-C3.py simple
2_cinderella-C3.py product-buchi
2_cinderella-C3.py product-co-buchi
2_cinderella-C3.py otf
3_repair-lock.py simple
3_repair-lock.py product-buchi
3_repair-lock.py product-co-buchi
3_repair-lock.py otf
4_repair-critical-safety.py simple
4_repair-critical-safety.py product-buchi
4_repair-critical-safety.py product-co-buchi
4_repair-critical-safety.py otf
5_synth-synchronization.py simple
5_synth-synchronization.py product-buchi
5_synth-synchronization.py product-co-buchi
5_synth-synchronization.py otf
6_cinderella-environment-reach.py simple
6_cinderella-environment-reach.py product-buchi
6_cinderella-environment-reach.py product-co-buchi
6_cinderella-environment-reach.py otf
7_cinderella-buchi.py simple
7_cinderella-buchi.py product-buchi
7_cinderella-buchi.py product-co-buchi
7_cinderella-buchi.py otf
8_cinderella-genltl.py simple
8_cinderella-genltl.py product-buchi
8_cinderella-genltl.py product-co-buchi
8_cinderella-genltl.py otf
9_cinderella-scalability-test.py simple
9_cinderella-scalability-test.py product-buchi
9_cinderella-scalability-test.py product-co-buchi
9_cinderella-scalability-test.py otf
10_repair-critical-genltl.py simple
10_repair-critical-genltl.py product-buchi
10_repair-critical-genltl.py product-co-buchi
10_repair-critical-genltl.py otf
11_elevator3.py simple
11_elevator3.py product-buchi
11_elevator3.py product-co-buchi
11_elevator3.py otf
12_elevator4.py simple
12_elevator4.py product-buchi
12_elevator4.py product-co-buchi
12_elevator4.py otf
13_elevator5.py simple
13_elevator5.py product-buchi
13_elevator5.py product-co-buchi
13_elevator5.py otf
14_elevator8.py simple
14_elevator8.py product-buchi
14_elevator8.py product-co-buchi
14_elevator8.py otf
15_elevator10.py simple
15_elevator10.py product-buchi
15_elevator10.py product-co-buchi
15_elevator10.py otf
16_watertank-safety.py simple
16_watertank-safety.py product-buchi
16_watertank-safety.py product-co-buchi
16_watertank-safety.py otf
17_watertank-liveness.py simple
17_watertank-liveness.py product-buchi
17_watertank-liveness.py product-co-buchi
17_watertank-liveness.py otf
18_sort3.py simple
18_sort3.py product-buchi
18_sort3.py product-co-buchi
18_sort3.py otf
19_sort4.py simple
19_sort4.py product-buchi
19_sort4.py product-co-buchi
19_sort4.py otf
20_sort5.py simple
20_sort5.py product-buchi
20_sort5.py product-co-buchi
20_sort5.py otf
21_box.py simple
21_box.py product-buchi
21_box.py product-co-buchi
21_box.py otf
22_box-limited.py simple
22_box-limited.py product-buchi
22_box-limited.py product-co-buchi
22_box-limited.py otf
23_diagonal.py simple
23_diagonal.py product-buchi
23_diagonal.py product-co-buchi
23_diagonal.py otf
24_evasion.py simple
24_evasion.py product-buchi
24_evasion.py product-co-buchi
24_evasion.py otf
25_follow.py simple
25_follow.py product-buchi
25_follow.py product-co-buchi
25_follow.py otf
26_solitary-box.py simple
26_solitary-box.py product-buchi
26_solitary-box.py product-co-buchi
26_solitary-box.py otf
27_square.py simple
27_square.py product-buchi
27_square.py product-co-buchi
27_square.py otf
[5.26, 0.73, 0.56, 0.86, 1.78, 4.03, 112.17, 100.78, 6.47, 2030.94, 10.71, 1.82, 29.35, 28.76, 32.35, 933.17]
[869.66, 4.31, 0.44, 25.67, 56.25, 11.41, 0.02, 0.0, 21.76, 1.82, 7.31, 8.82, 2.35]
Benchmark results stored in ./results.csv

Average (arithmetic mean) speedup over Raboniel: 206.23375000000001
Average (geometric mean) speedup over Raboniel: 13.317312546280746

Average (arithmetic mean) speedup over ConSynth: 77.67846153846153
Average (geometric mean) speedup over ConSynth: 6.205507407866477
```

Assuming the container name is `loving_rubin` (use `docker ps -a` to find out), the `results.csv` file can be copied onto the host file system after exiting the container using:

```
sudo docker cp loving_rubin:/gensys/results.csv .
```

#### Light run
The script `run_experiments.py` runs GenSys-LTL over all benchmarks but the numbers for Raboniel tool are hard-coded based on the previous run shown above, over all benchmarks. This mode takes two hours to run approximately.

### Manually

Without docker running `python3 run_experiments_raboniel.py` will require a manual setup of Raboniel by following the instructions in `tools/raboniel/raboniel/README.md`. Otherwise, running the command in the root folder (assuming GenSys-LTL is set up) should suffice:

```
python3 run_experiments.py
```

will run all the benchmarks for simple, product, and otf fixpoints; the results will be stored in `./results.csv` and the average mean speedup over Consynth and Raboniel tools will be printed. This process may take few hours (2 hours on an i7-8700 machine with 64GB RAM). Documentation explaining each benchmark is present in the file.

The tool is also uploaded to [Zenodo](https://zenodo.org/records/10439578) and an image to [Dockerhub](https://hub.docker.com/r/stanlysamuel/gensys-ltl).

### Notes: 
- In the ASE 2023 paper, as mentioned, we were only able to run Raboniel, but not ConSynth and Temos. All three tools are present in the `./tools` folder, for reference.
- All benchmarks for Raboniel are present in the folder `./tools/raboniel/artifact/raboniel/examples`. We manually wrote a few benchmarks in Raboniel such as the Cinderella-Stepmother benchmarks. These benchmarks are found in `./tools/raboniel/artifact/raboniel/examples/gensys`.
- Although we require the Spot tool to convert LTL formulas into buchi automata, for this version of GenSys, this process is done manually and hence the input to GenSys-LTL is a buchi automaton and not an LTL formula. If the user wishes to encode custom LTL formulas, they must replace predicates with propositions, feed the resulting propositonal LTL formula to Spot, and replace the propositions in the resulting Buchi automaton to the corresponding predicates, manually. Future versions of GenSys will automate this. The version of Spot we used is version 2.9.8 and is present in `./tools/spot-2.9.8`.
- For the OTF results, the value of K used is the one used in the paper, where which we manually tested every value of K, until realizable for the controller.This process will be automated in a future version of GenSys.

## Rules for creating your own game

### Simple Games

GenSys-LTL provides API's to model many various versions of logical LTL games. The first version of GenSys could only model safety games and provided the following API:
```
safety_fixedpoint(controller_moves, environment, guarantee, mode)
```
The details for the above API are mentioned [in a previous version of GenSys](https://github.com/stanlysamuel/gensys/blob/main/README.md), and is extended in GenSys-LTL. In GenSys-LTL, the above safety fixpoint now has the form:
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