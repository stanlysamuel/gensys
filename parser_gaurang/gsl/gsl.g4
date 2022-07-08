grammar gsl;

prog        : declList+ cmoveList environmentMove specification
            ;

declList    : declList1
            | declList2
            ;    
declList1   : decl
            | decl declList1
            ;   

decl        : type IDENTIFIER';'
            ;

// declList2   : type identifierList ';'
//             ;

// identifierList: IDENTIFIER 
//               | identifierList ',' identifierList
//               ;
declList2   : type identifierList 
            ;

identifierList: IDENTIFIER ';'
              | IDENTIFIER ',' identifierList
              ;

// assignmentList  : assignment 
//                 | assignment assignmentList
//                 ;

// assignment  : IDENTIFIER ':=' expr ';'
//             ;

expr     : IDENTIFIER 
         | NUM
         | expr op expr
         ;

// ( (IDENTIFIER | NUM | NUM IDENTIFIER) op (IDENTIFIER | NUM | NUM IDENTIFIER) op) *

op          : '+' | '-' ;

cmoveList       : cmove
                | cmoveList cmove
                ;

cmove           : 'cmove ' (NUM|IDENTIFIER) ':' formula
                ;

environmentMove : 'enviroment: ' formula 
                ;

specification   : 'specification: ' formula 
                ;

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

COMMENT     :   '/*' .*? '*/' -> skip;
LINE_COMMENT:   '//' ~[\r\n]* -> skip;
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]*;
NUM         : [0-9]+;
WS          : [ \r\n\t]+ -> skip;