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

declList2   : type identifierList 
            ;

identifierList: IDENTIFIER ';'
              | IDENTIFIER ',' identifierList
              ;

expr     : IDENTIFIER 
         | NUM
         | expr op expr

         ;

op          : '+' | '-' ;

cmoveList       : cmove
                | cmoveList cmove
                ;

cmove           : 'cmove ' (NUM|IDENTIFIER) ':' z3Formula
                ;

environmentMove : 'environment: ' z3Formula 
                ;

specification   : 'specification:' ltlformula 
                ;

type        : 'Int'
            | 'Real'
            ; 

//Z3 formula

z3Formula       :  'And(' predicateList ')'     
                ;

predicateList   : predicate 
                | predicate ',' predicateList
                ;

// Spot's LTL formula reference
ltlformula
        : '(' ltlformula ')'                               #BracketFormula
        | ('G' | 'F' | '!' | 'X') ltlformula             #UnaryOp
        | ltlformula ('and' | 'xor' | '|') ltlformula             #BinaryLogicOp
        | ltlformula ('->' | '<->' | 'U' | 'W') ltlformula    #BinaryOp
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