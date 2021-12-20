// Generated from /home/stanley/Projects/gensysMain/gensys/parser/tool/gensys.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class gensysParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, Numeral=4, Decimal=5, ParOpen=6, ParClose=7, PS_Not=8, 
		PS_And=9, PS_Or=10, PS_LessEq=11, PS_GreatEq=12, UndefinedSymbol=13, WS=14, 
		Comment=15, Semicolon=16;
	public static final int
		RULE_root = 0, RULE_terms = 1, RULE_predefSymbol = 2, RULE_binaryOperator = 3, 
		RULE_simpleSymbol = 4, RULE_symbol = 5, RULE_numeral = 6, RULE_decimal = 7, 
		RULE_identifier = 8, RULE_qual_identifier = 9, RULE_spec_constant = 10, 
		RULE_term = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "terms", "predefSymbol", "binaryOperator", "simpleSymbol", "symbol", 
			"numeral", "decimal", "identifier", "qual_identifier", "spec_constant", 
			"term"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'(goals'", "'(goal'", "':precision precise :depth'", null, null, 
			"'('", "')'", "'not'", "'and'", "'or'", "'<='", "'>='", null, null, null, 
			"';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "Numeral", "Decimal", "ParOpen", "ParClose", 
			"PS_Not", "PS_And", "PS_Or", "PS_LessEq", "PS_GreatEq", "UndefinedSymbol", 
			"WS", "Comment", "Semicolon"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "gensys.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gensysParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RootContext extends ParserRuleContext {
		public TermsContext terms() {
			return getRuleContext(TermsContext.class,0);
		}
		public NumeralContext numeral() {
			return getRuleContext(NumeralContext.class,0);
		}
		public List<TerminalNode> ParClose() { return getTokens(gensysParser.ParClose); }
		public TerminalNode ParClose(int i) {
			return getToken(gensysParser.ParClose, i);
		}
		public TerminalNode EOF() { return getToken(gensysParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			match(T__0);
			setState(25);
			match(T__1);
			setState(26);
			terms();
			setState(27);
			match(T__2);
			setState(28);
			numeral();
			setState(29);
			match(ParClose);
			setState(30);
			match(ParClose);
			setState(31);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermsContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public TermsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terms; }
	}

	public final TermsContext terms() throws RecognitionException {
		TermsContext _localctx = new TermsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_terms);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(33);
				term();
				}
				}
				setState(36); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Numeral) | (1L << Decimal) | (1L << ParOpen) | (1L << PS_Not) | (1L << PS_And) | (1L << PS_Or) | (1L << PS_LessEq) | (1L << PS_GreatEq) | (1L << UndefinedSymbol))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PredefSymbolContext extends ParserRuleContext {
		public TerminalNode PS_Not() { return getToken(gensysParser.PS_Not, 0); }
		public BinaryOperatorContext binaryOperator() {
			return getRuleContext(BinaryOperatorContext.class,0);
		}
		public PredefSymbolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predefSymbol; }
	}

	public final PredefSymbolContext predefSymbol() throws RecognitionException {
		PredefSymbolContext _localctx = new PredefSymbolContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_predefSymbol);
		try {
			setState(40);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PS_Not:
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				match(PS_Not);
				}
				break;
			case PS_And:
			case PS_Or:
			case PS_LessEq:
			case PS_GreatEq:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				binaryOperator();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BinaryOperatorContext extends ParserRuleContext {
		public TerminalNode PS_And() { return getToken(gensysParser.PS_And, 0); }
		public TerminalNode PS_Or() { return getToken(gensysParser.PS_Or, 0); }
		public TerminalNode PS_LessEq() { return getToken(gensysParser.PS_LessEq, 0); }
		public TerminalNode PS_GreatEq() { return getToken(gensysParser.PS_GreatEq, 0); }
		public BinaryOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryOperator; }
	}

	public final BinaryOperatorContext binaryOperator() throws RecognitionException {
		BinaryOperatorContext _localctx = new BinaryOperatorContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_binaryOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PS_And) | (1L << PS_Or) | (1L << PS_LessEq) | (1L << PS_GreatEq))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SimpleSymbolContext extends ParserRuleContext {
		public PredefSymbolContext predefSymbol() {
			return getRuleContext(PredefSymbolContext.class,0);
		}
		public TerminalNode UndefinedSymbol() { return getToken(gensysParser.UndefinedSymbol, 0); }
		public SimpleSymbolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleSymbol; }
	}

	public final SimpleSymbolContext simpleSymbol() throws RecognitionException {
		SimpleSymbolContext _localctx = new SimpleSymbolContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_simpleSymbol);
		try {
			setState(46);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PS_Not:
			case PS_And:
			case PS_Or:
			case PS_LessEq:
			case PS_GreatEq:
				enterOuterAlt(_localctx, 1);
				{
				setState(44);
				predefSymbol();
				}
				break;
			case UndefinedSymbol:
				enterOuterAlt(_localctx, 2);
				{
				setState(45);
				match(UndefinedSymbol);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SymbolContext extends ParserRuleContext {
		public SimpleSymbolContext simpleSymbol() {
			return getRuleContext(SimpleSymbolContext.class,0);
		}
		public SymbolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_symbol; }
	}

	public final SymbolContext symbol() throws RecognitionException {
		SymbolContext _localctx = new SymbolContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_symbol);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			simpleSymbol();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumeralContext extends ParserRuleContext {
		public TerminalNode Numeral() { return getToken(gensysParser.Numeral, 0); }
		public NumeralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numeral; }
	}

	public final NumeralContext numeral() throws RecognitionException {
		NumeralContext _localctx = new NumeralContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_numeral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(Numeral);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DecimalContext extends ParserRuleContext {
		public TerminalNode Decimal() { return getToken(gensysParser.Decimal, 0); }
		public DecimalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decimal; }
	}

	public final DecimalContext decimal() throws RecognitionException {
		DecimalContext _localctx = new DecimalContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_decimal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			match(Decimal);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierContext extends ParserRuleContext {
		public SymbolContext symbol() {
			return getRuleContext(SymbolContext.class,0);
		}
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			symbol();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Qual_identifierContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Qual_identifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qual_identifier; }
	}

	public final Qual_identifierContext qual_identifier() throws RecognitionException {
		Qual_identifierContext _localctx = new Qual_identifierContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_qual_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Spec_constantContext extends ParserRuleContext {
		public NumeralContext numeral() {
			return getRuleContext(NumeralContext.class,0);
		}
		public DecimalContext decimal() {
			return getRuleContext(DecimalContext.class,0);
		}
		public Spec_constantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_spec_constant; }
	}

	public final Spec_constantContext spec_constant() throws RecognitionException {
		Spec_constantContext _localctx = new Spec_constantContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_spec_constant);
		try {
			setState(60);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Numeral:
				enterOuterAlt(_localctx, 1);
				{
				setState(58);
				numeral();
				}
				break;
			case Decimal:
				enterOuterAlt(_localctx, 2);
				{
				setState(59);
				decimal();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public Spec_constantContext spec_constant() {
			return getRuleContext(Spec_constantContext.class,0);
		}
		public Qual_identifierContext qual_identifier() {
			return getRuleContext(Qual_identifierContext.class,0);
		}
		public TerminalNode ParOpen() { return getToken(gensysParser.ParOpen, 0); }
		public TerminalNode ParClose() { return getToken(gensysParser.ParClose, 0); }
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_term);
		int _la;
		try {
			setState(73);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Numeral:
			case Decimal:
				enterOuterAlt(_localctx, 1);
				{
				setState(62);
				spec_constant();
				}
				break;
			case PS_Not:
			case PS_And:
			case PS_Or:
			case PS_LessEq:
			case PS_GreatEq:
			case UndefinedSymbol:
				enterOuterAlt(_localctx, 2);
				{
				setState(63);
				qual_identifier();
				}
				break;
			case ParOpen:
				enterOuterAlt(_localctx, 3);
				{
				setState(64);
				match(ParOpen);
				setState(65);
				qual_identifier();
				setState(67); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(66);
					term();
					}
					}
					setState(69); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Numeral) | (1L << Decimal) | (1L << ParOpen) | (1L << PS_Not) | (1L << PS_And) | (1L << PS_Or) | (1L << PS_LessEq) | (1L << PS_GreatEq) | (1L << UndefinedSymbol))) != 0) );
				setState(71);
				match(ParClose);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22N\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3%\n\3\r\3\16"+
		"\3&\3\4\3\4\5\4+\n\4\3\5\3\5\3\6\3\6\5\6\61\n\6\3\7\3\7\3\b\3\b\3\t\3"+
		"\t\3\n\3\n\3\13\3\13\3\f\3\f\5\f?\n\f\3\r\3\r\3\r\3\r\3\r\6\rF\n\r\r\r"+
		"\16\rG\3\r\3\r\5\rL\n\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\3\3"+
		"\2\13\16\2H\2\32\3\2\2\2\4$\3\2\2\2\6*\3\2\2\2\b,\3\2\2\2\n\60\3\2\2\2"+
		"\f\62\3\2\2\2\16\64\3\2\2\2\20\66\3\2\2\2\228\3\2\2\2\24:\3\2\2\2\26>"+
		"\3\2\2\2\30K\3\2\2\2\32\33\7\3\2\2\33\34\7\4\2\2\34\35\5\4\3\2\35\36\7"+
		"\5\2\2\36\37\5\16\b\2\37 \7\t\2\2 !\7\t\2\2!\"\7\2\2\3\"\3\3\2\2\2#%\5"+
		"\30\r\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\5\3\2\2\2(+\7\n\2\2"+
		")+\5\b\5\2*(\3\2\2\2*)\3\2\2\2+\7\3\2\2\2,-\t\2\2\2-\t\3\2\2\2.\61\5\6"+
		"\4\2/\61\7\17\2\2\60.\3\2\2\2\60/\3\2\2\2\61\13\3\2\2\2\62\63\5\n\6\2"+
		"\63\r\3\2\2\2\64\65\7\6\2\2\65\17\3\2\2\2\66\67\7\7\2\2\67\21\3\2\2\2"+
		"89\5\f\7\29\23\3\2\2\2:;\5\22\n\2;\25\3\2\2\2<?\5\16\b\2=?\5\20\t\2><"+
		"\3\2\2\2>=\3\2\2\2?\27\3\2\2\2@L\5\26\f\2AL\5\24\13\2BC\7\b\2\2CE\5\24"+
		"\13\2DF\5\30\r\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\7"+
		"\t\2\2JL\3\2\2\2K@\3\2\2\2KA\3\2\2\2KB\3\2\2\2L\31\3\2\2\2\b&*\60>GK";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}