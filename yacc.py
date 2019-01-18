from ply import yacc

# Get the token map from the lexer.  This is required.
from lexer import Lexer


# def logger(p, log):
#     print(log, [str(x).replace('\\n', '') for x in p], sep='\t')
#     # print([str(qr) for qr in Yacc.quadRuples])
#     # print()
#     # print(log)
#     # pass


class Yacc:
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULTIPLY', 'DIVIDE'),
    )

    tokens = Lexer.tokens

    def p_program(self, p):
        '''program : list'''

    def p_list1(self, p):
        '''list : list declaration'''
    def p_list2(self, p):
        '''list : declaration'''

    def p_declaration1(self, p):
        '''declaration : function'''
    def p_declaration2(self, p):
        '''varDeclaration'''

    def p_varDeclaration(self, p):
        '''varDeclaration : type variableList'''

    def p_ScopedVariableDec(self, p):
        '''ScopedVariableDec : scopedSpecifier variableList'''

    def p_variableList1(self, p):
        '''variableList : variableList COMMA varInitialization'''
    def p_variableList2(self, p):
        '''varInitialization'''

    def p_varInitialization1(self, p):
        '''varInitialization : varForm'''
    def p_varInitialization2(self, p):
        '''varForm TWO_POINTS PARENTHESES_OPEN eachExpression PARENTHESES_CLOSE'''

    def p_varForm1(self, p):
        '''varForm : LETTER numOrletter BRACKET_OPEN num BRACKET_CLOSE'''
    def p_varForm2(self, p):
        '''varForm : LETTER numOrletter'''

    def p_scopedSpecifier(self, p):
        '''scopedSpecifier : STATIC_KW type | type'''

    def p_type(self, p):
        '''type : BOOLEAN_KW | CHARACTER_KW | INTEGER_KW | CHAR_KW | BOOL_KW | INT_KW'''

    def p_function(self, p):
        '''function : VOID_KW
        |   numOrLetter OPENING_PARENTHESES parameter CLOSING_PARENTHESES OPENING_BRACE statement CLOSING_BRACE
        |   type LETTER numOrLetter OPENING_PARENTHESES parameter CLOSING_PARENTHESES statement'''

    def p_parameter(self, p):
        '''parameter : listOfParameters | ε'''

    def p_listOfParameters(self, p):
        '''listOfParameters : listOfParameters SEMICOLON paramTypeList | paramTypeList'''

    def p_paramTypeList(self, p):
        '''paramTypeList : type paramList'''

    def p_paramList(self, p):
        '''paramList : paramList COMMA paramId | paramId'''

    def p_localDeclarations(self, p):
        '''localDeclarations : localDeclarations ScopedVariableDec | ε'''

    def p_paramId(self, p):
        '''paramId : LETTER numOrLetter | LETTER numOrLetter OPENING_BRACKET CLOSING_BRACKET'''

    def p_statement(self, p):
        '''statement : phrase | compoundPhrase | selectPhrase | iterationPhrase | returnPhrase | continue'''

    # def p_phrase(self, p ) :
    #     '''phrase : allExpression SEMICOLON | SEMICOLON'''

    # def p_selectPhrase(self, p ) :
    #     '''selectPhrase : IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES ifBody
    #     |   IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES OPENING_BRACE ifBody ifBody CLOSING_BRACE
    #     '''

    # def p_ifBody(self, p ) :
    #     '''ifBody : statement | statement OTHER_KW statement | SEMICOLON'''

    # def p_iterationPhrase(self, p ) :
    #     '''iterationPhrase : till OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES statement'''

    # def p_returnPhrase(self, p ) :
    #     '''returnPhrase : COMEBACK_KW SEMICOLON
    #     |   GIVEBACK_KW allExpression SEMICOLON
    #     |   GIVEBACK_KW numOrLetter SEMICOLON'''

    # def p_continue(self, p ) :
    #     '''continue : CONTINUE SEMICOLON'''

    # def p_continue(self, p ) :
    #     '''continue : CONTINUE SEMICOLON'''

    def p_allExpression(self, p):
        #   '''allExpression : alteralbe mathOp allExpression
        #  | alterable PLUS_PLUS | alterable MINUS_MINUS
        #   | eachExpression | alterable mathOp alterable'''

    def p_mathOp(self, p):

        # '''mathOp : EQUAL | PLUS_EQUAL | MINUS_EQUAL
        #    | TIMES_EQUAL | DIVIDE_EQUAL'''

    def p_eachExpression(self, p):

        # '''eachExpression : eachExpresiioin logicOp eachExpression
        #    | eachExpression logicOp eachExpression
        #    | eachExpression logicOp THEN_KEYWORD
        #    | logicOp eachExpression | relExpression
        #    | eachExpression logicOp ELSE_KEYWORD eachExpression'''

    def p_relExpression(self, p):

        # '''relExpression : mathEXP compareType mathEXP | mathEXP'''

    def p_compareType(self, p):
            '''compareType : equal | notEqual'''

    def p_equal(self, p):
        #     '''equal : LESS_EQUAL | GREATER_EQUAL | EQUAL_EQUAL'''

    def p_nonEqual(self, p):
    #    '''nonEqual : LESS_THAN | GREATER_THAN | NOT_EQUAL'''

    def p_mathEXP(self, p):
        '''mathEXP : mathEXP op mathEXP | unaryExpression'''

    # def p_op(self, p ) :
    #     '''op : PLUS | MINUS | TIMES | DIVIDE | PERCENTAGE'''

    def p_unaryExpression(self, p):
        '''unaryExpression : unaryop unaryExpression | factor'''

    # def p_unaryop(self, p ) :
    #     '''unaryop : MINUS | TIMES | QUESTION_MARK'''

    #rule 45 to top
    def p_factor(self, p):
        '''inalterable | alterable'''

    #def p_alterable(self, p):
        '''letter numOrletter | alterable BRACKET_OPEN allExpression BRACKET_CLOSE | alterable DOT letter'''

    #def p_inalterable(self, p):
        '''PARENTHESES_OPEN allExpression PARENTHESES_CLOSE | constant 
        | letter numOrletter PARENTHESES_OPEN args PARENTHESES_CLOSE'''

    def p_args(self, p):
        '''arguments | ε'''

    # def p_arguments(self, p):
        ''''arguments COMMA allExpression | allExpression'''

    # def p_constant(self, p):
        '''CONST_KW | TRUE_KW | FALSE_KW'''

    # def p_logicOp(self, p):
        '''LOGICAL_AND | LOGICAL_OR | TILDA | AND | OR'''





    def p_error(self, p):
        print("Syntax error in input!")

    def build(self, **kwargs):
        """
        build the parser
        """
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
