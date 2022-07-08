// Generated from /mnt/d/gensys/parser_gaurang/gsl/gsl.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class gslParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, COMMENT=31, 
		LINE_COMMENT=32, IDENTIFIER=33, NUM=34, WS=35;
	public static final int
		RULE_prog = 0, RULE_declList = 1, RULE_declList1 = 2, RULE_decl = 3, RULE_declList2 = 4, 
		RULE_identifierList = 5, RULE_expr = 6, RULE_op = 7, RULE_cmoveList = 8, 
		RULE_cmove = 9, RULE_environmentMove = 10, RULE_specification = 11, RULE_type = 12, 
		RULE_z3Formula = 13, RULE_predicateList = 14, RULE_ltlformula = 15, RULE_predicate = 16, 
		RULE_relOp = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "declList", "declList1", "decl", "declList2", "identifierList", 
			"expr", "op", "cmoveList", "cmove", "environmentMove", "specification", 
			"type", "z3Formula", "predicateList", "ltlformula", "predicate", "relOp"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "','", "'+'", "'-'", "'cmove '", "':'", "'environment: '", 
			"'specification:'", "'Int'", "'Real'", "'And('", "')'", "'('", "'G'", 
			"'F'", "'!'", "'X'", "'and'", "'xor'", "'|'", "'->'", "'<->'", "'U'", 
			"'W'", "'&'", "'>='", "'<='", "'=='", "'>'", "'<'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "COMMENT", "LINE_COMMENT", 
			"IDENTIFIER", "NUM", "WS"
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
	public String getGrammarFileName() { return "gsl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gslParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public CmoveListContext cmoveList() {
			return getRuleContext(CmoveListContext.class,0);
		}
		public EnvironmentMoveContext environmentMove() {
			return getRuleContext(EnvironmentMoveContext.class,0);
		}
		public SpecificationContext specification() {
			return getRuleContext(SpecificationContext.class,0);
		}
		public List<DeclListContext> declList() {
			return getRuleContexts(DeclListContext.class);
		}
		public DeclListContext declList(int i) {
			return getRuleContext(DeclListContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(36);
				declList();
				}
				}
				setState(39); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__8 || _la==T__9 );
			setState(41);
			cmoveList(0);
			setState(42);
			environmentMove();
			setState(43);
			specification();
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

	public static class DeclListContext extends ParserRuleContext {
		public DeclList1Context declList1() {
			return getRuleContext(DeclList1Context.class,0);
		}
		public DeclList2Context declList2() {
			return getRuleContext(DeclList2Context.class,0);
		}
		public DeclListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declList; }
	}

	public final DeclListContext declList() throws RecognitionException {
		DeclListContext _localctx = new DeclListContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declList);
		try {
			setState(47);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				declList1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(46);
				declList2();
				}
				break;
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

	public static class DeclList1Context extends ParserRuleContext {
		public DeclContext decl() {
			return getRuleContext(DeclContext.class,0);
		}
		public DeclList1Context declList1() {
			return getRuleContext(DeclList1Context.class,0);
		}
		public DeclList1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declList1; }
	}

	public final DeclList1Context declList1() throws RecognitionException {
		DeclList1Context _localctx = new DeclList1Context(_ctx, getState());
		enterRule(_localctx, 4, RULE_declList1);
		try {
			setState(53);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(49);
				decl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(50);
				decl();
				setState(51);
				declList1();
				}
				break;
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

	public static class DeclContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(gslParser.IDENTIFIER, 0); }
		public DeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl; }
	}

	public final DeclContext decl() throws RecognitionException {
		DeclContext _localctx = new DeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			type();
			setState(56);
			match(IDENTIFIER);
			setState(57);
			match(T__0);
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

	public static class DeclList2Context extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public IdentifierListContext identifierList() {
			return getRuleContext(IdentifierListContext.class,0);
		}
		public DeclList2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declList2; }
	}

	public final DeclList2Context declList2() throws RecognitionException {
		DeclList2Context _localctx = new DeclList2Context(_ctx, getState());
		enterRule(_localctx, 8, RULE_declList2);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			type();
			setState(60);
			identifierList();
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

	public static class IdentifierListContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(gslParser.IDENTIFIER, 0); }
		public IdentifierListContext identifierList() {
			return getRuleContext(IdentifierListContext.class,0);
		}
		public IdentifierListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierList; }
	}

	public final IdentifierListContext identifierList() throws RecognitionException {
		IdentifierListContext _localctx = new IdentifierListContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_identifierList);
		try {
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(62);
				match(IDENTIFIER);
				setState(63);
				match(T__0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(64);
				match(IDENTIFIER);
				setState(65);
				match(T__1);
				setState(66);
				identifierList();
				}
				break;
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

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(gslParser.IDENTIFIER, 0); }
		public TerminalNode NUM() { return getToken(gslParser.NUM, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				setState(70);
				match(IDENTIFIER);
				}
				break;
			case NUM:
				{
				setState(71);
				match(NUM);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(80);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(74);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(75);
					op();
					setState(76);
					expr(2);
					}
					} 
				}
				setState(82);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class OpContext extends ParserRuleContext {
		public OpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op; }
	}

	public final OpContext op() throws RecognitionException {
		OpContext _localctx = new OpContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_la = _input.LA(1);
			if ( !(_la==T__2 || _la==T__3) ) {
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

	public static class CmoveListContext extends ParserRuleContext {
		public CmoveContext cmove() {
			return getRuleContext(CmoveContext.class,0);
		}
		public CmoveListContext cmoveList() {
			return getRuleContext(CmoveListContext.class,0);
		}
		public CmoveListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cmoveList; }
	}

	public final CmoveListContext cmoveList() throws RecognitionException {
		return cmoveList(0);
	}

	private CmoveListContext cmoveList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		CmoveListContext _localctx = new CmoveListContext(_ctx, _parentState);
		CmoveListContext _prevctx = _localctx;
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_cmoveList, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(86);
			cmove();
			}
			_ctx.stop = _input.LT(-1);
			setState(92);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CmoveListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_cmoveList);
					setState(88);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(89);
					cmove();
					}
					} 
				}
				setState(94);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class CmoveContext extends ParserRuleContext {
		public Z3FormulaContext z3Formula() {
			return getRuleContext(Z3FormulaContext.class,0);
		}
		public TerminalNode NUM() { return getToken(gslParser.NUM, 0); }
		public TerminalNode IDENTIFIER() { return getToken(gslParser.IDENTIFIER, 0); }
		public CmoveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cmove; }
	}

	public final CmoveContext cmove() throws RecognitionException {
		CmoveContext _localctx = new CmoveContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_cmove);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(T__4);
			setState(96);
			_la = _input.LA(1);
			if ( !(_la==IDENTIFIER || _la==NUM) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(97);
			match(T__5);
			setState(98);
			z3Formula();
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

	public static class EnvironmentMoveContext extends ParserRuleContext {
		public Z3FormulaContext z3Formula() {
			return getRuleContext(Z3FormulaContext.class,0);
		}
		public EnvironmentMoveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_environmentMove; }
	}

	public final EnvironmentMoveContext environmentMove() throws RecognitionException {
		EnvironmentMoveContext _localctx = new EnvironmentMoveContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_environmentMove);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(T__6);
			setState(101);
			z3Formula();
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

	public static class SpecificationContext extends ParserRuleContext {
		public LtlformulaContext ltlformula() {
			return getRuleContext(LtlformulaContext.class,0);
		}
		public SpecificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_specification; }
	}

	public final SpecificationContext specification() throws RecognitionException {
		SpecificationContext _localctx = new SpecificationContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(T__7);
			setState(104);
			ltlformula(0);
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

	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			_la = _input.LA(1);
			if ( !(_la==T__8 || _la==T__9) ) {
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

	public static class Z3FormulaContext extends ParserRuleContext {
		public PredicateListContext predicateList() {
			return getRuleContext(PredicateListContext.class,0);
		}
		public Z3FormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_z3Formula; }
	}

	public final Z3FormulaContext z3Formula() throws RecognitionException {
		Z3FormulaContext _localctx = new Z3FormulaContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_z3Formula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(T__10);
			setState(109);
			predicateList();
			setState(110);
			match(T__11);
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

	public static class PredicateListContext extends ParserRuleContext {
		public PredicateContext predicate() {
			return getRuleContext(PredicateContext.class,0);
		}
		public PredicateListContext predicateList() {
			return getRuleContext(PredicateListContext.class,0);
		}
		public PredicateListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predicateList; }
	}

	public final PredicateListContext predicateList() throws RecognitionException {
		PredicateListContext _localctx = new PredicateListContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_predicateList);
		try {
			setState(117);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(112);
				predicate(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(113);
				predicate(0);
				setState(114);
				match(T__1);
				setState(115);
				predicateList();
				}
				break;
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

	public static class LtlformulaContext extends ParserRuleContext {
		public LtlformulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ltlformula; }
	 
		public LtlformulaContext() { }
		public void copyFrom(LtlformulaContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class UnaryOpContext extends LtlformulaContext {
		public LtlformulaContext ltlformula() {
			return getRuleContext(LtlformulaContext.class,0);
		}
		public UnaryOpContext(LtlformulaContext ctx) { copyFrom(ctx); }
	}
	public static class BracketFormulaContext extends LtlformulaContext {
		public LtlformulaContext ltlformula() {
			return getRuleContext(LtlformulaContext.class,0);
		}
		public BracketFormulaContext(LtlformulaContext ctx) { copyFrom(ctx); }
	}
	public static class BinaryLogicOpContext extends LtlformulaContext {
		public List<LtlformulaContext> ltlformula() {
			return getRuleContexts(LtlformulaContext.class);
		}
		public LtlformulaContext ltlformula(int i) {
			return getRuleContext(LtlformulaContext.class,i);
		}
		public BinaryLogicOpContext(LtlformulaContext ctx) { copyFrom(ctx); }
	}
	public static class AtomContext extends LtlformulaContext {
		public PredicateContext predicate() {
			return getRuleContext(PredicateContext.class,0);
		}
		public AtomContext(LtlformulaContext ctx) { copyFrom(ctx); }
	}
	public static class BinaryOpContext extends LtlformulaContext {
		public List<LtlformulaContext> ltlformula() {
			return getRuleContexts(LtlformulaContext.class);
		}
		public LtlformulaContext ltlformula(int i) {
			return getRuleContext(LtlformulaContext.class,i);
		}
		public BinaryOpContext(LtlformulaContext ctx) { copyFrom(ctx); }
	}

	public final LtlformulaContext ltlformula() throws RecognitionException {
		return ltlformula(0);
	}

	private LtlformulaContext ltlformula(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		LtlformulaContext _localctx = new LtlformulaContext(_ctx, _parentState);
		LtlformulaContext _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_ltlformula, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				_localctx = new BracketFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(120);
				match(T__12);
				setState(121);
				ltlformula(0);
				setState(122);
				match(T__11);
				}
				break;
			case 2:
				{
				_localctx = new UnaryOpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(124);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(125);
				ltlformula(4);
				}
				break;
			case 3:
				{
				_localctx = new AtomContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(126);
				predicate(0);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(137);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(135);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
					case 1:
						{
						_localctx = new BinaryLogicOpContext(new LtlformulaContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_ltlformula);
						setState(129);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(130);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__17) | (1L << T__18) | (1L << T__19))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(131);
						ltlformula(4);
						}
						break;
					case 2:
						{
						_localctx = new BinaryOpContext(new LtlformulaContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_ltlformula);
						setState(132);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(133);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(134);
						ltlformula(3);
						}
						break;
					}
					} 
				}
				setState(139);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class PredicateContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public RelOpContext relOp() {
			return getRuleContext(RelOpContext.class,0);
		}
		public List<PredicateContext> predicate() {
			return getRuleContexts(PredicateContext.class);
		}
		public PredicateContext predicate(int i) {
			return getRuleContext(PredicateContext.class,i);
		}
		public PredicateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predicate; }
	}

	public final PredicateContext predicate() throws RecognitionException {
		return predicate(0);
	}

	private PredicateContext predicate(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PredicateContext _localctx = new PredicateContext(_ctx, _parentState);
		PredicateContext _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_predicate, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
			case NUM:
				{
				setState(141);
				expr(0);
				setState(142);
				relOp();
				setState(143);
				expr(0);
				}
				break;
			case T__15:
				{
				setState(145);
				match(T__15);
				setState(146);
				predicate(3);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(157);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(155);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
					case 1:
						{
						_localctx = new PredicateContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_predicate);
						setState(149);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(150);
						match(T__24);
						setState(151);
						predicate(3);
						}
						break;
					case 2:
						{
						_localctx = new PredicateContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_predicate);
						setState(152);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(153);
						match(T__19);
						setState(154);
						predicate(2);
						}
						break;
					}
					} 
				}
				setState(159);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class RelOpContext extends ParserRuleContext {
		public RelOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relOp; }
	}

	public final RelOpContext relOp() throws RecognitionException {
		RelOpContext _localctx = new RelOpContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_relOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__28) | (1L << T__29))) != 0)) ) {
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 6:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 8:
			return cmoveList_sempred((CmoveListContext)_localctx, predIndex);
		case 15:
			return ltlformula_sempred((LtlformulaContext)_localctx, predIndex);
		case 16:
			return predicate_sempred((PredicateContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean cmoveList_sempred(CmoveListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean ltlformula_sempred(LtlformulaContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 3);
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean predicate_sempred(PredicateContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 2);
		case 5:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%\u00a5\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\6\2(\n\2\r\2\16\2)\3\2\3\2\3\2\3\2\3\3\3\3\5\3\62\n\3\3"+
		"\4\3\4\3\4\3\4\5\48\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3"+
		"\7\5\7F\n\7\3\b\3\b\3\b\5\bK\n\b\3\b\3\b\3\b\3\b\7\bQ\n\b\f\b\16\bT\13"+
		"\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\7\n]\n\n\f\n\16\n`\13\n\3\13\3\13\3\13"+
		"\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\20"+
		"\3\20\3\20\3\20\3\20\5\20x\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\5\21\u0082\n\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u008a\n\21\f\21\16"+
		"\21\u008d\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0096\n\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\7\22\u009e\n\22\f\22\16\22\u00a1\13\22\3\23"+
		"\3\23\3\23\2\6\16\22 \"\24\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$"+
		"\2\t\3\2\5\6\3\2#$\3\2\13\f\3\2\20\23\3\2\24\26\3\2\27\32\3\2\34 \2\u00a1"+
		"\2\'\3\2\2\2\4\61\3\2\2\2\6\67\3\2\2\2\b9\3\2\2\2\n=\3\2\2\2\fE\3\2\2"+
		"\2\16J\3\2\2\2\20U\3\2\2\2\22W\3\2\2\2\24a\3\2\2\2\26f\3\2\2\2\30i\3\2"+
		"\2\2\32l\3\2\2\2\34n\3\2\2\2\36w\3\2\2\2 \u0081\3\2\2\2\"\u0095\3\2\2"+
		"\2$\u00a2\3\2\2\2&(\5\4\3\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2\2"+
		"*+\3\2\2\2+,\5\22\n\2,-\5\26\f\2-.\5\30\r\2.\3\3\2\2\2/\62\5\6\4\2\60"+
		"\62\5\n\6\2\61/\3\2\2\2\61\60\3\2\2\2\62\5\3\2\2\2\638\5\b\5\2\64\65\5"+
		"\b\5\2\65\66\5\6\4\2\668\3\2\2\2\67\63\3\2\2\2\67\64\3\2\2\28\7\3\2\2"+
		"\29:\5\32\16\2:;\7#\2\2;<\7\3\2\2<\t\3\2\2\2=>\5\32\16\2>?\5\f\7\2?\13"+
		"\3\2\2\2@A\7#\2\2AF\7\3\2\2BC\7#\2\2CD\7\4\2\2DF\5\f\7\2E@\3\2\2\2EB\3"+
		"\2\2\2F\r\3\2\2\2GH\b\b\1\2HK\7#\2\2IK\7$\2\2JG\3\2\2\2JI\3\2\2\2KR\3"+
		"\2\2\2LM\f\3\2\2MN\5\20\t\2NO\5\16\b\4OQ\3\2\2\2PL\3\2\2\2QT\3\2\2\2R"+
		"P\3\2\2\2RS\3\2\2\2S\17\3\2\2\2TR\3\2\2\2UV\t\2\2\2V\21\3\2\2\2WX\b\n"+
		"\1\2XY\5\24\13\2Y^\3\2\2\2Z[\f\3\2\2[]\5\24\13\2\\Z\3\2\2\2]`\3\2\2\2"+
		"^\\\3\2\2\2^_\3\2\2\2_\23\3\2\2\2`^\3\2\2\2ab\7\7\2\2bc\t\3\2\2cd\7\b"+
		"\2\2de\5\34\17\2e\25\3\2\2\2fg\7\t\2\2gh\5\34\17\2h\27\3\2\2\2ij\7\n\2"+
		"\2jk\5 \21\2k\31\3\2\2\2lm\t\4\2\2m\33\3\2\2\2no\7\r\2\2op\5\36\20\2p"+
		"q\7\16\2\2q\35\3\2\2\2rx\5\"\22\2st\5\"\22\2tu\7\4\2\2uv\5\36\20\2vx\3"+
		"\2\2\2wr\3\2\2\2ws\3\2\2\2x\37\3\2\2\2yz\b\21\1\2z{\7\17\2\2{|\5 \21\2"+
		"|}\7\16\2\2}\u0082\3\2\2\2~\177\t\5\2\2\177\u0082\5 \21\6\u0080\u0082"+
		"\5\"\22\2\u0081y\3\2\2\2\u0081~\3\2\2\2\u0081\u0080\3\2\2\2\u0082\u008b"+
		"\3\2\2\2\u0083\u0084\f\5\2\2\u0084\u0085\t\6\2\2\u0085\u008a\5 \21\6\u0086"+
		"\u0087\f\4\2\2\u0087\u0088\t\7\2\2\u0088\u008a\5 \21\5\u0089\u0083\3\2"+
		"\2\2\u0089\u0086\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b"+
		"\u008c\3\2\2\2\u008c!\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\b\22\1\2"+
		"\u008f\u0090\5\16\b\2\u0090\u0091\5$\23\2\u0091\u0092\5\16\b\2\u0092\u0096"+
		"\3\2\2\2\u0093\u0094\7\22\2\2\u0094\u0096\5\"\22\5\u0095\u008e\3\2\2\2"+
		"\u0095\u0093\3\2\2\2\u0096\u009f\3\2\2\2\u0097\u0098\f\4\2\2\u0098\u0099"+
		"\7\33\2\2\u0099\u009e\5\"\22\5\u009a\u009b\f\3\2\2\u009b\u009c\7\26\2"+
		"\2\u009c\u009e\5\"\22\4\u009d\u0097\3\2\2\2\u009d\u009a\3\2\2\2\u009e"+
		"\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0#\3\2\2\2"+
		"\u00a1\u009f\3\2\2\2\u00a2\u00a3\t\b\2\2\u00a3%\3\2\2\2\20)\61\67EJR^"+
		"w\u0081\u0089\u008b\u0095\u009d\u009f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}