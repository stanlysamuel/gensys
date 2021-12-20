// Generated from GenSys.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GenSysParser}.
 */
public interface GenSysListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GenSysParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(GenSysParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(GenSysParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#terms}.
	 * @param ctx the parse tree
	 */
	void enterTerms(GenSysParser.TermsContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#terms}.
	 * @param ctx the parse tree
	 */
	void exitTerms(GenSysParser.TermsContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#predefSymbol}.
	 * @param ctx the parse tree
	 */
	void enterPredefSymbol(GenSysParser.PredefSymbolContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#predefSymbol}.
	 * @param ctx the parse tree
	 */
	void exitPredefSymbol(GenSysParser.PredefSymbolContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#binaryOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryOperator(GenSysParser.BinaryOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#binaryOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryOperator(GenSysParser.BinaryOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#simpleSymbol}.
	 * @param ctx the parse tree
	 */
	void enterSimpleSymbol(GenSysParser.SimpleSymbolContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#simpleSymbol}.
	 * @param ctx the parse tree
	 */
	void exitSimpleSymbol(GenSysParser.SimpleSymbolContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#symbol}.
	 * @param ctx the parse tree
	 */
	void enterSymbol(GenSysParser.SymbolContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#symbol}.
	 * @param ctx the parse tree
	 */
	void exitSymbol(GenSysParser.SymbolContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#numeral}.
	 * @param ctx the parse tree
	 */
	void enterNumeral(GenSysParser.NumeralContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#numeral}.
	 * @param ctx the parse tree
	 */
	void exitNumeral(GenSysParser.NumeralContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#decimal}.
	 * @param ctx the parse tree
	 */
	void enterDecimal(GenSysParser.DecimalContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#decimal}.
	 * @param ctx the parse tree
	 */
	void exitDecimal(GenSysParser.DecimalContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(GenSysParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(GenSysParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#qual_identifier}.
	 * @param ctx the parse tree
	 */
	void enterQual_identifier(GenSysParser.Qual_identifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#qual_identifier}.
	 * @param ctx the parse tree
	 */
	void exitQual_identifier(GenSysParser.Qual_identifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#spec_constant}.
	 * @param ctx the parse tree
	 */
	void enterSpec_constant(GenSysParser.Spec_constantContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#spec_constant}.
	 * @param ctx the parse tree
	 */
	void exitSpec_constant(GenSysParser.Spec_constantContext ctx);
	/**
	 * Enter a parse tree produced by {@link GenSysParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(GenSysParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link GenSysParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(GenSysParser.TermContext ctx);
}