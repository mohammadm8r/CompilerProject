import ply.lex as lex


class Lexer:
    symbol_table = []
    tokens = (
        'NUMBER',
        'ID',
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
        'GT',
        'STATIC_KW',
        'BOOLEAN_KW',
        'CHARACTER_KW',
        'INTEGER_KW',
        'CHAR_KW',
        'BOOL_KW',
        'INT_KW',
        'VOID_KW',
        'IF_KW',
        'OTHER_KW',
        'TILL_KW',
        'COMEBACK_KW',
        'GIVEBACK_KW',
        'CONTINUE_KW',
        'THEN_KW',
        'ELSE_KW',
        'CONST_KW',
        'TRUE_KW',
        'FALSE_KW'
    )

    reserved = {
        'static': 'STATIC_KW',
        'boolean': 'BOOLEAN_KW',
        'character': 'CHARACTER_KW',
        'integer': 'INTEGER_KW',
        'char': 'CHAR_KW',
        'bool': 'BOOL_KW',
        'int': 'INT_KW',
        'void': 'VOID_KW',
        'if': 'IF_KW',
        'other': 'OTHER_KW',
        'till': 'TILL_KW',
        'comeback': 'COMEBACK_KW',
        'comeBack': 'COMEBACK_KW',
        'giveback': 'GIVEBACK_KW',
        'giveBack': 'GIVEBACK_KW',
        'continue': 'CONTINUE_KW',
        'then': 'THEN_KW',
        'else': 'ELSE_KW',
        'const': 'CONST_KW',
        'true': 'TRUE_KW',
        'false': 'FALSE_KW',
        'and': 'AND',
        'or': 'OR'
    }

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

    def t_ID(self, t):
        r'[0-9]*[a-zA-Z]+[0-9a-zA-Z]*'
        t.type = self.reserved.get(t.value, 'ID')
        if t.type == 'ID':
            if t.value not in self.symbol_table:
                self.symbol_table.append(t.value)
        return t

    def t_NUMBER(self, t):
        r'[1-9]+[0-9]*'
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t'

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def make_lexer(self):
        lexer = lex.lex(module=self)

        # Test it out
        data = '''
            void secondFunc(bool B ; int A ) {
            int firstArray [5] ;
            bool A1 ;
            bool A2 ;
            A1= firstNum <= secondNum
            A2 = B ;
            if ( A1 and Then A2 )
            continue ;
            Other
            {
            int B1 ;
            if (B1<5)
            till(B1 != 5)
            B1++;
            If (B1== A)
            A2 = false;
            }
            comeBack;
            }
        '''

        # Give the lexer some input
        lexer.input(data)

        # Tokenize
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input
            print(tok)


m = Lexer()
m.make_lexer()