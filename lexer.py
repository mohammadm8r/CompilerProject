import ply.lex as lex

tokens = (
    'NUMBER',
    'LETTER'
    'MINUS',

)


def t_NUMBER(t):
    r'[1-9]+[0-9]*'
    return t


def t_LETTER(t):
    r'([a-zA-Z]+)+'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Test it out
data = '''
ARR + 4 * 10
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