// Generated from /home/stanley/Projects/gensysMain/gensys/parser/tool/gensys.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class gensysLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, Numeral=4, Decimal=5, ParOpen=6, ParClose=7, PS_Not=8, 
		PS_And=9, PS_Or=10, PS_LessEq=11, PS_GreatEq=12, UndefinedSymbol=13, WS=14, 
		Comment=15, Semicolon=16;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "Numeral", "Decimal", "Digit", "Sym", "ParOpen", 
			"ParClose", "PS_Not", "PS_And", "PS_Or", "PS_LessEq", "PS_GreatEq", "UndefinedSymbol", 
			"WS", "Comment", "Semicolon"
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


	public gensysLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "gensys.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22\u0095\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\7\5R\n\5\f\5\16\5U\13\5\5"+
		"\5W\n\5\3\6\3\6\3\6\7\6\\\n\6\f\6\16\6_\13\6\3\6\3\6\3\7\3\7\3\b\3\b\3"+
		"\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3"+
		"\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\7\20\177\n\20\f\20\16\20\u0082"+
		"\13\20\3\21\6\21\u0085\n\21\r\21\16\21\u0086\3\21\3\21\3\22\3\22\7\22"+
		"\u008d\n\22\f\22\16\22\u0090\13\22\3\22\3\22\3\23\3\23\2\2\24\3\3\5\4"+
		"\7\5\t\6\13\7\r\2\17\2\21\b\23\t\25\n\27\13\31\f\33\r\35\16\37\17!\20"+
		"#\21%\22\3\2\7\3\2\63;\3\2\62;\n\2##&(,-/\61>\\`ac|\u0080\u0080\5\2\13"+
		"\f\17\17\"\"\4\2\f\f\17\17\2\u0099\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2"+
		"\2\t\3\2\2\2\2\13\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27"+
		"\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2"+
		"\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5.\3\2\2\2\7\64\3\2\2\2\tV\3\2\2"+
		"\2\13X\3\2\2\2\rb\3\2\2\2\17d\3\2\2\2\21f\3\2\2\2\23h\3\2\2\2\25j\3\2"+
		"\2\2\27n\3\2\2\2\31r\3\2\2\2\33u\3\2\2\2\35x\3\2\2\2\37{\3\2\2\2!\u0084"+
		"\3\2\2\2#\u008a\3\2\2\2%\u0093\3\2\2\2\'(\7*\2\2()\7i\2\2)*\7q\2\2*+\7"+
		"c\2\2+,\7n\2\2,-\7u\2\2-\4\3\2\2\2./\7*\2\2/\60\7i\2\2\60\61\7q\2\2\61"+
		"\62\7c\2\2\62\63\7n\2\2\63\6\3\2\2\2\64\65\7<\2\2\65\66\7r\2\2\66\67\7"+
		"t\2\2\678\7g\2\289\7e\2\29:\7k\2\2:;\7u\2\2;<\7k\2\2<=\7q\2\2=>\7p\2\2"+
		">?\7\"\2\2?@\7r\2\2@A\7t\2\2AB\7g\2\2BC\7e\2\2CD\7k\2\2DE\7u\2\2EF\7g"+
		"\2\2FG\7\"\2\2GH\7<\2\2HI\7f\2\2IJ\7g\2\2JK\7r\2\2KL\7v\2\2LM\7j\2\2M"+
		"\b\3\2\2\2NW\7\62\2\2OS\t\2\2\2PR\5\r\7\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2"+
		"\2ST\3\2\2\2TW\3\2\2\2US\3\2\2\2VN\3\2\2\2VO\3\2\2\2W\n\3\2\2\2XY\5\t"+
		"\5\2Y]\7\60\2\2Z\\\7\62\2\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^"+
		"`\3\2\2\2_]\3\2\2\2`a\5\t\5\2a\f\3\2\2\2bc\t\3\2\2c\16\3\2\2\2de\t\4\2"+
		"\2e\20\3\2\2\2fg\7*\2\2g\22\3\2\2\2hi\7+\2\2i\24\3\2\2\2jk\7p\2\2kl\7"+
		"q\2\2lm\7v\2\2m\26\3\2\2\2no\7c\2\2op\7p\2\2pq\7f\2\2q\30\3\2\2\2rs\7"+
		"q\2\2st\7t\2\2t\32\3\2\2\2uv\7>\2\2vw\7?\2\2w\34\3\2\2\2xy\7@\2\2yz\7"+
		"?\2\2z\36\3\2\2\2{\u0080\5\17\b\2|\177\5\r\7\2}\177\5\17\b\2~|\3\2\2\2"+
		"~}\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081"+
		" \3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0085\t\5\2\2\u0084\u0083\3\2\2\2"+
		"\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088"+
		"\3\2\2\2\u0088\u0089\b\21\2\2\u0089\"\3\2\2\2\u008a\u008e\5%\23\2\u008b"+
		"\u008d\n\6\2\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2"+
		"\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u008e\3\2\2\2\u0091"+
		"\u0092\b\22\2\2\u0092$\3\2\2\2\u0093\u0094\7=\2\2\u0094&\3\2\2\2\n\2S"+
		"V]~\u0080\u0086\u008e\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}