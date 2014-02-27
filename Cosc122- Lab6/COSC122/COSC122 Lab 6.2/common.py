from quicksort import *

def common_items(list_x,list_y):
    """Returns a list containing all the items in x that are also in y.
    The resulting list should be in order.
    Clashes need only be listed once.
    Returns an empty list if there are none.
    >>> common_items([0,1,2,3],[0,0,2,4])
    [0, 2]
    >>> common_items([0,1,2,3],[1,2,3,4])
    [1, 2, 3]
    >>> common_items([0,1,2,3],[3,2,1,0])
    [0, 1, 2, 3]
    >>> common_items([0,1,2,3],[5,6,7,8])
    []
    >>> common_items([],[5,6,7,8])
    []
    >>> common_items([1,2,3,4],[])
    []
    >>> common_items([],[])
    []
    
    """

    #Your code goes here
    #You should have just finished a nice sort function you can use
    #to sort the lists in to order



if __name__ == "__main__": 
    doctest.testmod()
