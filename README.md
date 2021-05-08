# GenSys
This repository hosts the code for the tool: GenSys as is currently at version 0.1

## Introduction 

GenSys is a scalable fixpoint engine for the synthesis of strategies in inifinite state games. GenSys currently supports safety as the winning condition. GenSys uses the Z3 theorem prover by Microsoft Research for solving SMT formulae. GenSys is scalable and is validated on two benchmark suites.

### Installation
You should have installed Python 2/3 on your system.
Currently we can successfully run SVMRanker with Python 2.7.1.

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

***Program Repair example***

The benchmarks are python files that invoke the GenSys API. They can be executed as regular python program.

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

The cinderella example takes as input a parameter for the bucket size of size greater than zero. To run the example for bucket size 3.0:

```
python cinderella 3.0

```

This returns the output:

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
stanley@stanley-Vostro-3250:~/Projects/gensysMain/gensys/benchmarks$ python cinderella.py 3.0('Iteration', 0)
('Iteration ', 1)
('Iteration ', 2)

('Number of times projection is done: ', 3)

Invariant is Satisfiable
REALIZABLE
EXTRACTING CONTROLLER...

Condition for the controller action: move1
And(b4 <= 2,
    b5 <= 2,
    b3 <= 2,
    -3 <= -1*b5 + -1*b3,
    b1 <= 3,
    b2 <= 3,
    b1 >= 0,
    b2 >= 0,
    b3 >= 0,
    b4 >= 0,
    b5 >= 0)

Condition for the controller action: move2
And(b5 <= 2,
    b4 <= 2,
    -3 <= -1*b1 + -1*b4,
    b1 <= 2,
    b2 <= 3,
    b3 <= 3,
    b1 >= 0,
    b2 >= 0,
    b3 >= 0,
    b4 >= 0,
    b5 >= 0)

Condition for the controller action: move3
And(b1 <= 2,
    b5 <= 2,
    b2 <= 2,
    -3 <= -1*b2 + -1*b5,
    b3 <= 3,
    b4 <= 3,
    b1 >= 0,
    b2 >= 0,
    b3 >= 0,
    b4 >= 0,
    b5 >= 0)

Condition for the controller action: move4
And(b1 <= 2,
    b3 <= 2,
    b2 <= 2,
    -3 <= -1*b1 + -1*b3,
    b4 <= 3,
    b5 <= 3,
    b1 >= 0,
    b2 >= 0,
    b3 >= 0,
    b4 >= 0,
    b5 >= 0)

Condition for the controller action: move5
And(b3 <= 2,
    b4 <= 2,
    b2 <= 2,
    -3 <= -1*b4 + -1*b2,
    b1 <= 3,
    b5 <= 3,
    b1 >= 0,
    b2 >= 0,
    b3 >= 0,
    b4 >= 0,
    b5 >= 0)
```

which is interpreted the same way as the previous example.

***Other Benchmarks***

Benchmarks from the DTSynth paper can be found in the gensys/benchmarks/dtsynth.

**Rules for creating your own game**

- The safety game consists of three parts: envrionment, controller and guarantee which is to be passed to the safety_fixpoint function as:
```
safety_fixedpoint(controller_moves, environment, guarantee)
```
- **environment** is a python definition of the form function(s,s_). It is important to name the post variables with an underscore in this version of GenSys.
- **guarantee** 