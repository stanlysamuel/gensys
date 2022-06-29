grammar task;
/* 
prog    : (identifier identifier2)*;

identifier      : Identifier_Var ; 
identifier2     :  Identifier_Var2;

Identifier_Var      : [a-zA-Z0-9_]+;
Identifier_Var2     : [a-zA-Z0-9_]+;
WS                  : [ \r\n\t]+ -> skip;


prog            :	(expr identifier identifier2)* ;
expr            :	expr ('*'|'/') expr
                |	expr ('+'|'-') expr
                |	'(' expr ')'
                ;
identifier      : Identifier_Var ; 
identifier2     :  Identifier_Var2;

Identifier_Var      : [a-zA-Z0-9_]+;
Identifier_Var2     : [a-zA-Z0-9_]+;
WS      : [ \r\n\t]+ -> skip;

*/

prog    : (expr)*;
expr    : IDENTIFIER
        |  decl
        | IDENTIFIER
        ;

IDENTIFIER  : [a-zA-Z0-9_]+;
decl        : IDENTIFIER;
WS          : [ \r\n\t]+ -> skip;
