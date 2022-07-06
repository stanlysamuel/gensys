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

IDENTIFIER  : [a-zA-Z0-9_]+;
NUM         : [0-9]+;
WS          : [ \r\n\t]+ -> skip;
