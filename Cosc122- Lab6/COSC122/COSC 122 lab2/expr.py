
def calculate(operator, param1, param2):
    """
    Returns the result of a calculation between param1 and param2 using the
    given operator.
    Supported operators: *, /, +, -
    
    >>> calculate('*', 2, 3)
    6
    >>> calculate('+', 2, 3)
    5
    >>> calculate('-', 2, 3)
    -1
    """
    if operator == '*':
        return param1 * param2
    elif operator == '/':
        # Promote these to floats to avoid truncation
        return float(param1) / float(param2)
    elif operator == '+':
        return param1 + param2
    elif operator == '-':
        return param1 - param2
    
    #Didn't recognise operator
    raise Exception("Invalid operator")


    

def evaluate_post_fix(expression):
    """
    Evaluates an expression in postfix notaion.
    Numerical operands must be integers.

    >>> evaluate_post_fix('2 3 +')
    5
    >>> evaluate_post_fix('2 3 4 * +')
    14
    >>> evaluate_post_fix('2 3 + 4 *')
    20
    >>> evaluate_post_fix('2 3 2 * + 5 -')
    3
    >>> evaluate_post_fix('2 3 + 2 5 - *')
    -15
    >>> evaluate_post_fix('2 3 + 5 2 / *')
    12.5
    """
    from structs import Stack
    import re
    
    OP_PREC={"(":1,
             "+":2,
             "-":2,
             "*":3,
             "/":3,
             ")":4}
    
    # Split postfix string into a list of tokens. For example:
    #  '2 3 +' => expression contains the list ['2', '3', '+']
    # Don't worry about how this works
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', expression)
 
    
    #Code to evaluate the postfix expression and return the result goes here
    
    pass



def infix_to_postfix(infix):
    """
    Converts an infix expression to a postfix expression.
    Numerical operands must be integers.

    >>> infix_to_postfix('2+3')
    '2 3 +'
    >>> infix_to_postfix('2+3*4')
    '2 3 4 * +'
    >>> infix_to_postfix('(2+3)*4')
    '2 3 + 4 *'
    >>> infix_to_postfix('2+3*2-5')
    '2 3 2 * + 5 -'
    >>> infix_to_postfix('(2+3)*(2-5)')
    '2 3 + 2 5 - *'
    >>> infix_to_postfix('(2+3)*(5/2)')
    '2 3 + 5 2 / *'
    """
    
    from structs import Stack
    import re
    
    OP_PREC={"(":1,
             "+":2,
             "-":2,
             "*":3,
             "/":3,
             ")":4}    
    
    # Split infix string into tokens. For example:
    #  '2+3*4' => ['2', '+', '3', '*', '4']
    # Don't worry too much about how...
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', infix)
    
  
    #Code to process tokens and return the postfix string goes here
    
    pass
    
    
    
def evaluate_infix(infix):
    """
    Evaluates an infix expression.
    Numerical operands must be integers.
    
    >>> evaluate_infix('2+3*4')
    14
    >>> evaluate_infix('2+(3*4)')
    14
    >>> evaluate_infix('(2+3)*4')
    20
    >>> evaluate_infix('2+3*2-5')
    3
    >>> evaluate_infix('(2+3)*(2-5)')
    -15
    >>> evaluate_infix('(2+3)*(5/2)')
    12.5
   
    """
    
    from structs import Deque
    import re
    
    OP_PREC={"(":1,
             "+":2,
             "-":2,
             "*":3,
             "/":3,
             ")":4}    
    
    # Split infix string into tokens. For example:
    #  '2+3*4' => ['2', '+', '3', '*', '4']
    # Don't worry too much about how...
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', infix)
    
  
    #Code to process tokens and evaluate the infix expression
    
    pass



if __name__ == '__main__':
    import doctest
    #import os
    #os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    
    # Uncomment next line to run the tests
    # doctest.testmod()
    # Can enter an infinite loop if your code isn't implemented correctly