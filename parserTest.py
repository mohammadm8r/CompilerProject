from lexer import Lexer
from yacc import Yacc

data = '''
3+4
'''
l = Lexer()
y = Yacc()
r = y.build().parse(data, l.make_lexer(), False)
print(r)
