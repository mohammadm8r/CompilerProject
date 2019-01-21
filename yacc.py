from ply import yacc

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

    def p_numOrletter1(self, p):
        '''numOrletter : NUM'''
    def p_numOrletter2(self, p):
        '''numOrletter : LETTER'''
    def p_numOrletter3(self, p):
        '''numOrletter : LETTER NUM'''
    def p_numOrletter4(self, p):
        '''numOrletter : NUM LETTER'''
    def p_numOrletter5(self, p):
        '''numOrletter : empty'''

    def p_program(self, p):
        '''program : list'''

    def p_list1(self, p):
        '''list : list declaration'''
    def p_list2(self, p):
        '''list : declaration'''

    def p_declaration1(self, p):
        '''declaration : function'''
    def p_declaration2(self, p):
        '''declaration : varDeclaration'''

    def p_varDeclaration(self, p):
        '''varDeclaration : type variableList'''

    def p_ScopedVariableDec(self, p):
        '''ScopedVariableDec : scopedSpecifier variableList'''

    def p_variableList1(self, p):
        '''variableList : variableList COMMA varInitialization'''
    def p_variableList2(self, p):
        '''variableList : varInitialization'''

    def p_varInitialization1(self, p):
        '''varInitialization : varForm'''
    def p_varInitialization2(self, p):
        '''varInitialization : varForm TWO_POINTS PARENTHESES_OPEN eachExpression PARENTHESES_CLOSE'''

    def p_varForm1(self, p):
        '''varForm : LETTER numOrletter BRACKET_OPEN NUM BRACKET_CLOSE'''
    def p_varForm2(self, p):
        '''varForm : LETTER numOrletter'''

    def p_scopedSpecifier1(self, p):
        '''scopedSpecifier : STATIC_KW type'''
    def p_scopedSpecifier2(self, p):
        '''scopedSpecifier : type'''

    def p_type1(self, p):
        '''type : BOOLEAN_KW'''
    def p_type2(self, p):
         '''type : CHARACTER_KW'''
    def p_type3(self, p):
         '''type : INTEGER_KW'''
    def p_type4(self, p):
         '''type : CHAR_KW'''
    def p_type5(self, p):
         '''type : BOOL_KW'''
    def p_type6(self, p):
         '''type : INT_KW'''

    def p_function1(self, p):
        '''function : VOID_KW numOrletter PARENTHESES_OPEN parameter PARENTHESES_CLOSE BRACE_OPEN statement BRACE_CLOSE'''
    def p_function2(self, p):
        '''function : type LETTER numOrletter PARENTHESES_OPEN parameter PARENTHESES_CLOSE statement'''

    def p_parameter1(self, p):
        '''parameter : listOfParameters'''
    def p_parameter2(self, p):
        '''parameter : empty'''
    def p_empty(self, p):
        '''empty : '''

    def p_listOfParameters1(self, p):
        '''listOfParameters : listOfParameters SEMICOLON paramTypeList'''
    def p_listOfParameters2(self, p):
        '''listOfParameters : paramTypeList'''

    def p_paramTypeList(self, p):
        '''paramTypeList : type paramList'''

    def p_paramList1(self, p):
        '''paramList : paramList COMMA paramId'''

    def p_paramList2(self, p):
        '''paramList : paramId'''

    def p_localDeclarations1(self, p):
        '''localDeclarations : localDeclarations ScopedVariableDec'''
    def p_localDeclarations2(self, p):
        '''localDeclarations : empty'''

    def p_paramId1(self, p):
        '''paramId : LETTER numOrletter'''
    def p_paramId2(self, p):
        '''paramId : LETTER numOrletter BRACKET_OPEN BRACKET_CLOSE'''

    def p_statement1(self, p):
        '''statement : phrase'''
    def p_statement2(self, p):
        '''statement : compoundPhrase'''
    def p_statement3(self, p):
        '''statement : selectPhrase'''
    def p_statement4(self, p):
        '''statement : iterationPhrase'''
    def p_statement5(self, p):
        '''statement : returnPhrase'''
    def p_statement6(self, p):
        '''statement : continue'''

    def p_compoundPhrase(self, p):
        '''compoundPhrase : BRACE_OPEN localDeclarations statementList BRACE_CLOSE'''

    def p_statementList1(self, p):
        '''statementList : statementList statement'''
    def p_statementList2(self, p):
        '''statementList : empty'''

    def p_phrase1(self, p ) :
        '''phrase : allExpression SEMICOLON'''
    def p_phrase2(self, p):
        '''phrase : SEMICOLON'''

    def p_selectPhrase1(self, p ) :
        '''selectPhrase : IF_KW PARENTHESES_OPEN eachExpression PARENTHESES_CLOSE ifBody'''
    def p_selectPhrase2(self, p ) :
        '''selectPhrase : IF_KW PARENTHESES_OPEN eachExpression PARENTHESES_CLOSE BRACE_OPEN ifBody ifBody BRACE_CLOSE'''

    def p_ifBody1(self, p ) :
        '''ifBody : statement'''
    def p_ifBody2(self, p ) :
        '''ifBody : statement OTHER_KW statement'''
    def p_ifBody3(self, p ) :
        '''ifBody : SEMICOLON'''

    def p_iterationPhrase(self, p ) :
        '''iterationPhrase : TILL_KW PARENTHESES_OPEN eachExpression PARENTHESES_CLOSE statement'''

    def p_returnPhrase1(self, p ) :
        '''returnPhrase : COMEBACK_KW SEMICOLON'''
    def p_returnPhrase2(self, p ) :
        '''returnPhrase : GIVEBACK_KW allExpression SEMICOLON'''
    def p_returnPhrase3(self, p ) :
        '''returnPhrase : GIVEBACK_KW numOrletter SEMICOLON'''

    def p_continue(self, p ) :
        '''continue : CONTINUE_KW SEMICOLON'''

    def p_allExpression1(self, p):
          '''allExpression : alterable mathOp allExpression'''
    def p_allExpression2(self, p):
          '''allExpression : alterable PLUS_PLUS'''
    def p_allExpression3(self, p):
          '''allExpression : alterable MINUS_MINUS'''
    def p_allExpression4(self, p):
          '''allExpression : eachExpression'''
    def p_allExpression5(self, p):
          '''allExpression : alterable mathOp alterable'''

    def p_mathOp1(self, p):
        '''mathOp : EQUAL'''
    def p_mathOp2(self, p):
        '''mathOp : PLUS_EQUAL'''
    def p_mathOp3(self, p):
        '''mathOp : MINUS_EQUAL'''
    def p_mathOp4(self, p):
        '''mathOp : MULTIPLY_EQUAL'''
    def p_mathOp5(self, p):
        '''mathOp : DIVISION_EQUAL'''

    def p_eachExpression1(self, p):
        '''eachExpression : eachExpression logicOp eachExpression'''
    # def p_eachExpression2(self, p):
    #     '''eachExpression :eachExpression logicOp eachExpression'''
    def p_eachExpression3(self, p):
        '''eachExpression : eachExpression logicOp THEN_KW eachExpression'''
    def p_eachExpression4(self, p):
        '''eachExpression : logicOp eachExpression'''
    def p_eachExpression5(self, p):
        '''eachExpression : relExpression'''
    def p_eachExpression6(self, p):
        '''eachExpression : eachExpression logicOp ELSE_KW eachExpression'''

    def p_relExpression1(self, p):
        '''relExpression : mathEXP compareType mathEXP'''
    def p_relExpression2(self, p):
        '''relExpression : mathEXP'''

    def p_compareType1(self, p):
        '''compareType : equal'''
    def p_compareType2(self, p):
        '''compareType : nonEqual'''

    def p_equal1(self, p):
        '''equal : LEQ'''
    def p_equal2(self, p):
        '''equal : GEQ'''
    def p_equal3(self, p):
        '''equal : EEQ'''

    def p_nonEqual1(self, p):
       '''nonEqual : LT'''
    def p_nonEqual2(self, p):
       '''nonEqual : GT '''
    def p_nonEqual3(self, p):
       '''nonEqual : NEQ'''

    def p_mathEXP1(self, p):
        '''mathEXP : mathEXP op mathEXP'''
    def p_mathEXP2(self, p):
        '''mathEXP : unaryExpression'''

    def p_op1(self, p):
        '''op : PLUS '''
    def p_op2(self, p):
        '''op : MINUS'''
    def p_op3(self, p):
        '''op : MULTIPLY'''
    def p_op4(self, p):
        '''op : DIVIDE'''
    def p_op5(self, p):
        '''op : PERCENTAGE'''

    def p_unaryExpression1(self, p):
        '''unaryExpression : unaryop unaryExpression'''
    def p_unaryExpression2(self, p):
        '''unaryExpression : factor'''

    def p_unaryop1(self, p):
        '''unaryop : MINUS'''
    def p_unaryop2(self, p):
        '''unaryop : MULTIPLY'''
    def p_unaryop3(self, p):
        '''unaryop : QUESTION_MARK'''

    def p_factor1(self, p):
        '''factor : inalterable'''
    def p_factor2(self, p):
        '''factor : alterable'''

    def p_alterable1(self, p):
        '''alterable : LETTER numOrletter'''
    def p_alterable2(self, p):
        '''alterable : alterable BRACKET_OPEN allExpression BRACKET_CLOSE'''
    def p_alterable3(self, p):
        '''alterable : alterable DOT LETTER numOrletter'''

    def p_inalterable1(self, p):
        '''inalterable : PARENTHESES_OPEN allExpression PARENTHESES_CLOSE'''
    def p_inalterable2(self, p):
        '''inalterable : constant'''
    def p_inalterable3(self, p):
        '''inalterable : LETTER numOrletter PARENTHESES_OPEN args PARENTHESES_CLOSE'''

    def p_args1(self, p):
        '''args : arguments'''
    def p_args2(self, p):
        '''args : empty'''

    def p_arguments(self, p):
        '''arguments : arguments COMMA allExpression'''

    def p_constant1(self, p):
        '''constant : CONST_KW '''
    def p_constant2(self, p):
        '''constant : TRUE_KW '''
    def p_constant3(self, p):
        '''constant : FALSE_KW'''

    def p_logicOp1(self, p):
        '''logicOp : LOGICAL_AND '''
    def p_logicOp2(self, p):
        '''logicOp : LOGICAL_OR'''
    def p_logicOp3(self, p):
        '''logicOp : TILDA'''
    def p_logicOp4(self, p):
        '''logicOp : AND'''
    def p_logicOp5(self, p):
        '''logicOp : OR'''

    def p_error(self, p):
        print("Syntax error in input!")

    def make_parser(self, **kwargs):
        """
        build the parser
        """
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
