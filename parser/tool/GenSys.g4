grammar GenSys;

/*
 * Parser Rules
 */

//  root        : '(goals' SPACES '(goal' SPACES  formula SPACES ':precision precise :depth' SPACES NUMBER')' SPACES ')' WHITESPACE* EOF;
// root        : '(goals' SPACES '(goal' SPACES  term SPACES ':precision precise :depth' SPACES NUMBER')' SPACES ')' WHITESPACE* EOF;

// formula     : formula SPACES (relOpFormula | binOpFormula) | (relOpFormula | binOpFormula) ;
// //  relOpFormulae: relOpFormulae SPACES relOpFormula | relOpFormula;
//  relOpFormula: '('relOp SPACES IDENTIFIER SPACES NUMBER ')';
//  binOpFormula: '('binOp SPACES formula SPACES NUMBER ')'; 
//  relOp       : '>=' | '<=';
//  binOp       : 'or' | 'and';

root        : '(goals' '(goal' terms ':precision precise :depth' numeral')' ')' EOF;

// formula     : formula (relOpFormula | binOpFormula) | (relOpFormula | binOpFormula) ;
// //  relOpFormulae: relOpFormulae SPACES relOpFormula | relOpFormula;
//  relOpFormula: '('relOp IDENTIFIER NUMBER ')';
//  binOpFormula: '('binOp formula NUMBER ')'; 
//  relOp       : '>=' | '<=';
//  binOp       : 'or' | 'and';

// SMTLIB parser rules

terms: term+
     ;
predefSymbol
    : PS_Not
    | binaryOperator
    // | PS_Bool
    // | PS_ContinuedExecution
    // | PS_Error
    // | PS_False
    // | PS_ImmediateExit
    // | PS_Incomplete
    // | PS_Logic
    // | PS_Memout
    // | PS_Sat
    // | PS_Success
    // | PS_Theory
    // | PS_True
    // | PS_Unknown
    // | PS_Unsupported
    // | PS_Unsat
    ;

binaryOperator
    : PS_And
    | PS_Or
    | PS_LessEq
    | PS_GreatEq
    ;
    
simpleSymbol
    : predefSymbol
    | UndefinedSymbol
    ;

symbol
    : simpleSymbol
    // | quotedSymbol
    ;

numeral
    : Numeral
    ;

decimal
    : Decimal
    ;

// Identifiers

identifier
    : symbol
    // | ParOpen GRW_Underscore symbol index+ ParClose
    ;

// Terms and Formulas

qual_identifier
    : identifier
    // | ParOpen GRW_As identifier sort ParClose
    ;

// S-expression

spec_constant
    : numeral
    | decimal
    // | hexadecimal
    // | binary
    // | string
    ;

 term
    : spec_constant
    | qual_identifier
    | ParOpen qual_identifier term+ ParClose;

/*
 * Lexer Rules
 */
// fragment LOWERCASE  : [a-z] ;
// fragment UPPERCASE  : [A-Z] ;
// WORD                : (LOWERCASE | UPPERCASE | '_')+ ;
// IDENTIFIER          : WORD (WORD | DIGIT)*; 
// SPACES              : (WHITESPACE | NEWLINE)+;
// WHITESPACE          : (' ' | '\t') ;
// NEWLINE             : ('\r'?'\n' | '\r') ;

// fragment DIGIT : [0-9] ;
// NUMBER         : DIGIT+ ([.,] DIGIT+)? ;

//SMTLIB lexer rules

Numeral
    : '0'
    | [1-9] Digit*
    ;

Decimal
    : Numeral '.' '0'* Numeral
    ;

fragment Digit
    : [0-9]
    ;

fragment Sym
    : 'a'..'z'
    | 'A' .. 'Z'
    | '+'
    | '='
    | '/'
    | '*'
    | '%'
    | '?'
    | '!'
    | '$'
    | '-'
    | '_'
    | '~'
    | '&'
    | '^'
    | '<'
    | '>'
    | '@'
    | '.'
    ;

ParOpen
    : '('
    ;

ParClose
    : ')'
    ;

// Predefined Symbols

PS_Not
    : 'not'
    ;

PS_And
    : 'and'
    ;

PS_Or
    : 'or'
    ;

PS_LessEq
    : '<='
    ;

PS_GreatEq
    : '>='
    ;

UndefinedSymbol:        //Should be last in order
    Sym (Digit | Sym)*;

// Skip comments and whitespaces, else will have to place them in between the grammar. Neat.
WS  :  [ \t\r\n]+ -> skip
    ;

Comment
    : Semicolon ~[\r\n]* -> skip
    ;

Semicolon
    : ';'
    ;