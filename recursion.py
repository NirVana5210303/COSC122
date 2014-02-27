from random import *
from turtle import *

class Node:
    def __init__(self,item):
        self.data = item
        self.next = None

        
def add_item_to_list(first_node, item):
    """
    Adds item to end of linked list.
    first_node is the first node in the list.
    """
    new_node = Node(item)
    if first_node == None:
        # the list needs a first node
        # initialise a first node with first_node = Node(item)
        # then call add_item_to_list to add another node
        raise IndexError ("None doesn't have a .next")
    else:
        current_node = first_node
        #traverse list until at last node
        while current_node.next <> None:
            current_node = current_node.next
        #set last node's next pointer to point to the new node
        current_node.next = new_node

            
 
def power(x, n):
    """Computes x**n"""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
                         
                         

def gcd(a,b):
    """Computes the greatest common divisor of a and b."""
    if b == 0:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(a-b, b)

    
def str_length(s):
    """
    Calculates the length of a string.
    Definitely not the best way of doing this!
    Think about how much space all the sub lists will take up.
    """
    if s == "":
        return 0
    return 1 + str_length(s[1:])
    

def fib_recursive(n):
    """Returns the 'n'th Fibonacci number.
    >>> fib_recursive(0)
    0
    >>> fib_recursive(1)
    1
    >>> fib_recursive(2)
    1
    >>> fib_recursive(3)
    2
    >>> fib_recursive(4)
    3
    >>> fib_recursive(9)
    34
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)
    
    

def fib_iterative(n):
    """Returns the 'n'th Fibonacci number.
    >>> fib_iterative(0)
    0
    >>> fib_iterative(1)
    1
    >>> fib_iterative(2)
    1
    >>> fib_iterative(3)
    2
    >>> fib_iterative(4)
    3
    >>> fib_iterative(9)
    34
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_n_minus2 = 0
        fib_n_minus1 = 1  
        for i in range(1,n):
            curr_fib = fib_n_minus1+fib_n_minus2
            fib_n_minus2 = fib_n_minus1
            fib_n_minus1 = curr_fib
        return curr_fib



def fibonacci_sequence(n):
    """
    Prints Fibonacci numbers up to the nth number (including the 0th number).

    >>> fibonacci_sequence(9)
    0 1 1 2 3 5 8 13 21 34
    """
    if n == 0:
        print 0,
    else:
        fibonacci_sequence(n-1)
        print fib_recursive(n),


def tree(size,level):
    """
     Draws a funky fractal tree.
     Feel free to experiment with parameters...
     """    
    if level<>0:
        forward(random()*size)
        x = pos()
        angle=random()*20
        right(angle)
        tree(size*.8,level-1)
        setpos(x)
        left(angle)
        angle=random()*-20
        right(angle)
        tree(size*.8,level-1)
        left(angle)
        setpos(x)
    

        
def linked_list_print(list_node):
    """
    Prints list, one item per line.
    
    >>> first_node = Node(1)
    >>> linked_list_print(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_print(first_node)
    1
    2
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_print(first_node)
    1
    2
    3
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_print(first_node)
    1
    2
    3
    4
    """
    if list_node == None:
        return
    else:
        print list_node.data
        linked_list_print(list_node.next)
        
        
#-------------------------------------------------------------------------------
#Functions for you to implement
#-------------------------------------------------------------------------------
        
def linked_list_length(list_node):
    """
    Returns the number of nodes in a linked list,
    0 if list is empty.
    
    >>> first_node = Node(1)
    >>> linked_list_length(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_length(first_node)
    2
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_length(first_node)
    3
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_length(first_node)
    4
    >>> add_item_to_list(first_node, 10)
    >>> linked_list_length(first_node)
    5
    """
    if list_node == None:
        return 0
    else:
        return linked_list_length(list_node.next)+1
        

    
def linked_list_reverse_print(list_node):
    """
    Prints list in reverse, one item per line.
    
    >>> first_node = Node(1)
    >>> linked_list_reverse_print(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_reverse_print(first_node)
    2
    1
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_reverse_print(first_node)
    3
    2
    1
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_reverse_print(first_node)
    4
    3
    2
    1
    """

    if list_node == None:
        return
    else:
        linked_list_reverse_print(list_node.next)
        print list_node.data
   
   
def is_in_linked_list(list_node,item):
    """
    Returns TRUE if item is in list, otherwise False.
    
    >>> first_node = Node(1)
    >>> is_in_linked_list(first_node,2)
    False
    >>> add_item_to_list(first_node, 2)
    >>> is_in_linked_list(first_node,2)
    True
    >>> add_item_to_list(first_node, 3)
    >>> add_item_to_list(first_node, 4)
    >>> add_item_to_list(first_node, 5)
    >>> is_in_linked_list(first_node,3)
    True
    >>> is_in_linked_list(first_node,10)
    False
    """
    if list_node==None:
        return False
    if list_node.data==item:
        return True
    else:
        return is_in_linked_list(list_node.next,item)

def factorial(n):
    """Computes n!
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        yj=1
        for i in range(1,n+1):
            yj*=i
        return yj

    
def quick_power(x,n):
    """
    Computes x ^ n where n is an integer
    NOTE: You need to write the doc test for the base case.
    >>> quick_power(2,3)
    8
    >>> quick_power(2,8)
    256
    >>> quick_power(2,16)
    65536
    >>> quick_power(2,0)
    1
    """
    if n==0:
        return 1
    if n%2==0:
        return (quick_power(x,n/2))**2
    if n%2==1:
        return x*quick_power(x,n-1)
    
    
def recursive_string_print(s):
    """
    Prints a string out, one character per line, using recursion
    Think about why this is very inefficient for long strings!
    """
    pass
    
    

if __name__ == '__main__':
    import doctest
    import os
    os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    doctest.testmod()
    
    n = 5000
    print 'fib({0:d}) = {1:d}'.format(n,fib_iterative(n))
    print '\n'
    
    n = 100
    print 'fib({0:d}) = {1:d}'.format(n,fib_iterative(n))
    print '\n'    
    
    n = 31
    print 'fib({0:d}) = {1:d}'.format(n,fib_recursive(n))
    print '\n'

    #Given the value for fib_iterative(100) would it be wise 
    #to try to run fib_recursive(100)????
    
    
    #my_list=Node('b')
    #add_item_to_list(my_list,'a')
    #linked_list_print(my_list)
    
    
    #Uncomment to draw a tree
    shape('turtle')
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(-90)
    forward(100)
    right(-90)
    forward(50)
    left(90)
    forward(100)