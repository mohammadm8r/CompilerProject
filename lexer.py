import ply.lex as lex

tokens = (
    'NUMBER',
    'LETTER',
    'BRACKET_OPEN',
    'BRACKET_CLOSE',
    'PARENTHESES_OPEN',
    'PARENTHESES_CLOSE',
    'BRACE_OPEN',
    'BRACE_CLOSE',
    'SEMICOLON',
    'DOT',
    'COMMA',
    'TILDA',
    'AND',
    'OR',
    'LOGICAL_OR',
    'LOGICAL_AND',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'PERCENTAGE',
    'QUESTION_MARK',
    'TWO_POINTS',
    'PLUS_PLUS',
    'MINUS_MINUS',
    'EQUAL',
    'PLUS_EQUAL',
    'MINUS_EQUAL',
    'MULTIPLY_EQUAL',
    'DIVISION_EQUAL',
    'LEQ',
    'GEQ',
    'EEQ',
    'NEQ',
    'LT',
    'GT'
)

t_PARENTHESES_OPEN = r'\('
t_PARENTHESES_CLOSE = r'\)'
t_BRACKET_OPEN = r'\['
t_BRACKET_CLOSE = r'\]'
t_BRACE_OPEN = r'\{'
t_BRACE_CLOSE = r'\}'
t_SEMICOLON = r'\;'
t_DOT = r'\.'
t_COMMA = r'\,'
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_OR = r'or'
t_AND = r'and'
t_TILDA = r'~'
t_QUESTION_MARK = r'\?'
t_MINUS = r'\-'
t_PLUS = r'\+'
t_MULTIPLY = r'\*'
t_PERCENTAGE = r'%'
t_DIVIDE = r'/'
t_TWO_POINTS = r':'
t_PLUS_PLUS = r'\+\+'
t_MINUS_MINUS = r'\-\-'
t_EQUAL = r'='
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'\-='
t_MULTIPLY_EQUAL = r'\*='
t_DIVISION_EQUAL = r'/='
t_LEQ = r'<='
t_GEQ = r'>='
t_EEQ = r'=='
t_LT = r'<'
t_GT = r'>'
t_NEQ = r'!='



def t_NUMBER(t):
    r'[1-9]+[0-9]*'
    return t


def t_LETTER(t):
    r'[a-zA-Z]+'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Test it out
data = '''
3 + 4 * 10
+ -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
