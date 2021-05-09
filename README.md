# GenSys
This repository hosts the code for the tool: GenSys and is currently at version 0.1.0.

## Introduction 

GenSys is a scalable fixpoint engine for the synthesis of strategies in inifinite state games. GenSys currently supports safety as the winning condition. GenSys uses the Z3 theorem prover by Microsoft Research for solving SMT formulae. GenSys is scalable and is validated on two benchmark suites.

## Authors

- Stanly Samuel, Indian Institute of Science, Bangalore
- Deepak D'Souza, Indian Institute of Science, Bangalore
- Raghavan Komondoor, Indian Institute of Science, Bangalore

### Installation
You should have installed Python 2/3 on your system. We successfully ran GenSys with Python 2.7.1.

**Install Python packages**

```
pip install z3-solver
```

**Add base project directory to PYTHONPATH**

```
export PYTHONPATH = ${PYTHONPATH}:/path/to/gensys
```

### Usage

**Setup GenSys**

```
git clone https://github.com/stanlysamuel/gensys.git

cd benchmarks
```

**Run Benchmarks**

The benchmarks are contained in gensys/benchmarks/. 
The GenSys library and helper functions are contained in gensys/gensys/.

***Program Repair example***

The benchmarks are python files that invoke the GenSys API. They can be executed as a regular python program.

For example, you can run the program Repair example by running:

```
python repairLock.py
```
You will get the following output

```
('Iteration', 0)
('Iteration ', 1)
('Iteration ', 2)
('Iteration ', 3)

('Number of times projection is done: ', 4)

Invariant is Satisfiable
REALIZABLE
EXTRACTING CONTROLLER...

Condition for the controller action: move1
And(pc == 0, l <= 0)

Condition for the controller action: move2
And(pc == 0, Or(l >= 1, gl == 0))

Condition for the controller action: move3
And(l <= 0, pc == 2)

Condition for the controller action: move4
And(pc == 4, l >= 1, Not(0 == gl))

Condition for the controller action: move5
And(gl == 0, pc == 4)

Condition for the controller action: move6
And(l >= 1, pc == 5)

Condition for the controller action: move7
pc == 6
```
This tells us that the fixed-point algorithm took 4 iterations to terminate, the game is realizable and returns the controller i.e. the conditions under which each move can be played.

Each controller move is a function definition in **repairLock.py**.

***Cinderella example***

The cinderella example takes as input a parameter for the bucket size of size greater than zero. To run the example for bucket size 1.99999:

```
python cinderella 1.99999
```

This returns the output:

```
('Iteration', 0)
('Iteration ', 1)
('Iteration ', 2)
('Iteration ', 3)
('Iteration ', 4)
('Iteration ', 5)
('Iteration ', 6)
('Iteration ', 7)
('Iteration ', 8)
('Iteration ', 9)
('Iteration ', 10)
('Iteration ', 11)
('Iteration ', 12)
('Iteration ', 13)
('Iteration ', 14)
('Iteration ', 15)
('Iteration ', 16)
('Iteration ', 17)
('Iteration ', 18)

('Number of times projection is done: ', 19)

Invariant is Unsatisifiable i.e. False
UNREALIZABLE

```

Cinderella has no winning strategy for the bucket size of 1.99999 and GenSys witnesses this fact in 19 iterations. It shows that the returns the invariant False and hence returns UNREALIZABLE.

***Other Benchmarks***

Benchmarks from the DTSynth paper can be found in the gensys/benchmarks/dtsynth.

**Rules for creating your own game**

- The safety game consists of three parts: envrionment, controller and guarantee which is to be passed to the safety_fixpoint function as:
```
safety_fixedpoint(controller_moves, environment, guarantee)
```
- Let s be the state of the game. In cinderella.py, s={b1, b2, b3, b4, b5}.
- Let s_ be the post variables after a transition. Thus, in cinderella.py, s_={b1_, b2_, b3_, b4_, b5_}
- **environment** is a python definition of the form function(s,s_). It is important to name the post variables with an underscore in this version of GenSys.
- **guarantee** is a python definition of the form function(s).
- The controller moves are specified separately here and then stored in a list. This is because the **safety_fixpoint** procedure extracts the strategy for each move. Each move is also of the form function(s,s_). As you can see in cinderella.py, there are five definitions denoting 5 moves which are stored in a list **controller_moves**.
- s should follow the same order in every function.
- s and s_ should not mix orders as well. For example, if s = {b1_, b2_, b3_, b4_, b5_}, s_ cannot be {b2_, b3_, b4_, b5_, b1_}. This will give unsound results in the initial version of GenSys.
- Error handling for the above cases is left to be handled.
- Environment can be equal to skip i.e. it performs no updates. Refer to the non-cinderella examples for the same.