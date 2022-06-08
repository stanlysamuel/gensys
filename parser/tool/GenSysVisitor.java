// Generated from GenSys.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link GenSysParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface GenSysVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link GenSysParser#root}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoot(GenSysParser.RootContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#terms}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerms(GenSysParser.TermsContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#predefSymbol}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPredefSymbol(GenSysParser.PredefSymbolContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#binaryOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinaryOperator(GenSysParser.BinaryOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#simpleSymbol}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleSymbol(GenSysParser.SimpleSymbolContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#symbol}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSymbol(GenSysParser.SymbolContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#numeral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumeral(GenSysParser.NumeralContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#decimal}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecimal(GenSysParser.DecimalContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentifier(GenSysParser.IdentifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#qual_identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQual_identifier(GenSysParser.Qual_identifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#spec_constant}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSpec_constant(GenSysParser.Spec_constantContext ctx);
	/**
	 * Visit a parse tree produced by {@link GenSysParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm(GenSysParser.TermContext ctx);
}