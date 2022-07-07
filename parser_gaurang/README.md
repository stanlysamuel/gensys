# Instructions to build the parser
- Run `make setup` to add the classpath
- Edit gsl.g4 and run `make run FILE=../benchmarks/test/test1.gsl` to generate base lexer, parser and visitor for gsl and then    run on the given file.
- If you want to see the tree, run `make get_ps FILE=../benchmarks/test/test1.gsl`
- This phase is used when you want to update the grammar and build the parser and test on a given file

# Instructions to use the parser
- Edit gslToZ3Visitor.py (which inherently extends gslVisitor.py) to create the intended visitor
- Use gslToZ3.py that would convert gsl to Z3.