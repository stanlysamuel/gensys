grammar gsl;

prog        : (expr1)*expr2;

expr1       : type IDENTIFIER';'
            | type IDENTIFIER';'
            ;

expr2       : IDENTIFIER ':=' IDENTIFIER
            | ('+' | '-') INT
            | ('*' | '/') INT
            ;

type        : 'Int'
            | 'Real'
            ; 

IDENTIFIER  : [a-zA-Z0-9_]+;
INT         : [0-9]+;
WS          : [ \r\n\t]+ -> skip;
