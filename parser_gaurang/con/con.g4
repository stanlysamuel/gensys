grammar con;
prog    : expr;
expr    : /*type*/ IDENTIFIER ':=' IDENTIFIER
        | ('+' | '-') INT
        | ('*' | '/') INT
        ;
//type    : 'Int'
//        | 'Real'
//        ;

IDENTIFIER  : [a-zA-Z0-9_]+;
INT         : [0-9]+;
WS          : [ \r\n\t]+ -> skip;
         