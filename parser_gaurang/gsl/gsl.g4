grammar gsl;

prog        : declList assignmentList
            ;

declList    : decl
            | decl declList
            ;

decl        : type IDENTIFIER';'
            ;

assignmentList  : assignment 
                | assignment assignmentList
                ;

assignment  : IDENTIFIER ':=' expr ';'
            ;

expr    : IDENTIFIER 
        | NUM
        | expr op expr
        ;

// ( (IDENTIFIER | NUM | NUM IDENTIFIER) op (IDENTIFIER | NUM | NUM IDENTIFIER) op) *

op          : '+' | '-' ;

type        : 'Int'
            | 'Real'
            ; 

// Spot's LTL formula reference
formula
        : '(' formula ')'                               #BracketFormula
        | ('G' | 'F' | '!' | 'X') formula             #UnaryOp
        | formula ('&' | 'xor' | '|') formula             #BinaryLogicOp
        | formula ('->' | '<->' | 'U' | 'W') formula    #BinaryOp
        | predicate                                          #Atom
        ;

// Atoms of the LTL formula are predicates
predicate: expr relOp expr 
        | '!' predicate
        | predicate '&' predicate
        | predicate '|' predicate         
        ;

relOp : '>=' | '<=' | '==' | '>' | '<' ;

IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]*;
NUM         : [0-9]+;
WS          : [ \r\n\t]+ -> skip;