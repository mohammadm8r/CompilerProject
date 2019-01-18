import ply.lex as lex

tokens = (
    'NUMBER',
    'LETTER',
    'BRACKET_OPEN',
    'BRACKET_CLOSE',
    'PARENTHESES_OPEN',
    'PARENTHESES_CLOSE',
    'BRACE_OPEN',
    'BRACE_CLOSE'

)


t_PARENTHESES_OPEN = r'\('
t_PARENTHESES_CLOSE = r'\)'
t_BRACKET_OPEN = r'\['
t_BRACKET_CLOSE = r'\]'
t_BRACE_OPEN = r'\{'
t_BRACE_CLOSE = r'\}'


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
