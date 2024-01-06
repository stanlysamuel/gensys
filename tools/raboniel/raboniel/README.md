# Raboniel

Reactive synthesis tool for temporal stream logic (TSL) modulo theories. This tool can be used to synthesis programs from tsl specifications using theories for integers and reals.

## Usage
To synthesize a system from a given specification you can execute `./raboniel --spec <PATH_TO_TSL_FILE>`
If raboniel is able to find a realizing system it will report:
```
Synthesis successful!
The system can be found in <PATH_TO_PROGRAM>
```
If raboniel determines that the specification is unrealizable it reports: `Unrealizible!`

However, raboniel is not guaranteed to terminate due to the unrealizability of the TSL-T synthesis problem.

In addition to the messages above the console output also shows some information about the counter examples analyzed in each iteration. A complete execution looks something like:
```
./raboniel --spec examples/example1/counter.tsl
Starting Iteration 0
#States:4
#Trans:48
Starting Iteration 1
#States:3
#Trans:27
Starting Iteration 2
#States:3
#Trans:11
Learned 4 new predicates (includes duplicates).
Starting Iteration 3
#States:6
#Trans:18
Starting Iteration 4
Synthesis successful!
Minimizing system states.
The system can be found in examples/example1/counter.py
```

*Important:* When starting raboniel the current directory must always be the same directory that contains the configuration files `check.sh`, `synth.sh`, and `synth_mini.sh` i.e. the directory containing this readme.

### Options
Raboniel supports the following options to influence it's execution:
```
Available options:
  -h,--help                Show this help text
  --minimize MINIMIZE      Minimize machine states (Always | Never | System)
                           default: System
  --keep KEEPTMP           Keep temporary files (All | TSL | None) default: None
  --simplify               Simplify the final system.
  --noStateExpansion       Do not expand non determinism in states.
  --output OUTPUTFORMAT    Output format (Python | PseudoCode) default: Python
  --spec STRING            TSL specification file
```
- minimize
LTL Synthesis tools can provide an option to minimize the states of the systems they create. This is used to control when this is enabled. In case `System` is selected we will restart LTL synthesis with minimization for the last LTL specification, thereby minimizing the states of the system, but not of the intermediate counter strategies.

- keep
Whether to immediatly delete the files used for LTL synthesis and during the iterations. `All` does not delete anything it keeps the `.tlsf` (LTL synthesis input), `.kiss` (Boolean Mealy or Moore machine), `.tsl` (TSL-T specifications) for all iterations. The `TSL` option only keeps the `.tsl` files but deletes the files from LTL synthesis.

- simplify
If enabled applies some heuristics to get more compact guard expressions in the resulting program.

- output
The synthesized program can be written either as a Python script or as a non executable pseudo code that resembles the TSL specification.

- spec
Required paramter. Path to the TSL specification.

A call using all option might look like:
`./raboniel --minimize Never --keep All --output Python --simplify --spec examples/example1/counter.tsl`

### TSL-T Input Language
The used input language is the TSL format used by `tsltools` (https://github.com/reactive-systems/tsltools), but extended by some annotations and integers and reals.

A simple example looks like:
```
//-- State: counter
//-- Inputs: i

assume {
  ge counter i0();
  le counter i100();
}

always assume {
  ge i i0();
  le i i5();
}

always guarantee {
  ge counter i0();  /* INV */
  le counter i100(); /* INV */

  [ counter <- add counter i ] || [ counter <- sub counter i ];
}
```

The state variables have to be declared in a comment in the first line. It must start with `//-- State: ` followed by the variables separated by `,`.
The input variables have to declared likewise in the second line starting with `//-- Inputs: `.

The type of a variable is encoded as part of its name. Variables starting with `r_` are reals every other variable is an integer.

Numerical constants are written as zero argument functions `i10()` for integers and `r4.2()` for reals. Negative numbers are written `im10()` and `rm4.2()`.

Arithmetic uses a prefix notation where paramters are separated by spaces.
The following functions and predicates are supported:
```
add         addition
sub         subtraction
mul         multiplication
div         interger division
mod         modulus

eq          equals
le          less than or equal
ge          greater than or equal
lt          less than
gt          greater than
```

All logic and temporal operators from TSL are supported.
Logic operators (e.g. `&&` and `||`) are written infix.
The temporal operators are written prefix (`F`, `G`, and `X`) or infix (`U` and `W`) and are the same as in LTL.
Updates are written `[<state_var> <- <expr>]`.

The file is organized in multiple blocks: `assume`, `always assume`, `guarantee`, and `always guarantee`. Multiple properties can be written in one block and separted by `,` they are then combined using conjunction. The assume blocks are assumption of the environment while guarantees must be met by the system. For more details please see the `tsl-tools` documentation.


### Python Output

The python output contains a function `run(init, inputs)` that takes a dictionary of inital values for all state variables and an iterator of dictionaries of input variables, it produces an iterator of dictionaries of state variables.

This function can be embeded in a larger application.
Alternatively when the file is launched directly it opens a simple interactive mode that prompts the user to type in the inputs.

```
python3 examples/example1/counter.py           
initial state: {"counter":99}
inputs: {"i":3}
state:  {'counter': 96}
-----
inputs: {"i":4}
state:  {'counter': 100}
-----
inputs: {"i":5}
state:  {'counter': 95}
-----
inputs: exit
```

### Configuration
This tools relies on several other tools that are used as external programs to read, write and process well defined file formats.
The calls to these tools are encapsulated in small shell scripts.
- Raboniel requires a tool to validate the syntax of a `tsl` file. This is defined in `check.sh` the default uses `tsltools`.
- A tool to synthesize `tsl` specification to `kiss` machines needs to provided in `synth.sh` and `synth_mini.sh`. The default uses a combination of `tsltools`, `strix`, and `syfco`.
