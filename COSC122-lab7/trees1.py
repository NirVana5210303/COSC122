 #-------------------------------------------------
def load_file(file_name):
    alist = []
    v = 0
    f = open(file_name)
    line = f.readline()
    while line != "":
        line.strip()
        line = int(line)
        alist = alist + [line]
        line = f.readline()
    return alist


#-------------------------------------------------
#-------------------------------------------------
class Node(object):
    """Represents a node in a binary tree."""
    
    #-------------------------------------------    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


    #-------------------------------------------        
    def __repr__(self):
        return "['%s', l:{%s} r:{%s}]" % (str(self.value),
                                          str(self.left),
                                          str(self.right))



#-------------------------------------------------
#-------------------------------------------------
class BinarySearchTree(object):
    """Implements the operations for a Binary Search Tree."""
    
    #-------------------------------------------
    def __init__(self):
        self.root = None

        
    #-------------------------------------------    
    def insert(self, value):
        """
        Inserts a new item into the tree.
        
        >>> b = BinarySearchTree()
        >>> b.insert(5)
        >>> b.insert(3)
        >>> b.root.left.value
        3
        >>> b.insert(4)
        >>> b.root.left.right.value
        4
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

        
    #-------------------------------------------
    def _insert(self, subtree, value):
        """
        Recursively locates the correct position in 'subtree' to insert 'value',
        and attaches 'value' to the tree.
        """
        if value < subtree.value:
            # Insert to the left
            if subtree.left is None:
                subtree.left = Node(value)
            else:
                self._insert(subtree.left, value)
        else:
            # Insert to the right
            if subtree.right is None:
                subtree.right = Node(value)
            else:
                self._insert(subtree.right, value)
                

    #-------------------------------------------
    def in_order_items(self):
        """
        Returns a sorted list of all items in the tree using in-order traversal.
        
        >>> b = BinarySearchTree()
        >>> b.insert(5)
        >>> b.insert(3)
        >>> b.insert(4)
        >>> b.in_order_items()
        [3, 4, 5]
        """
        l = []
        self._in_order_items(self.root, l)
        return l


    #-------------------------------------------
    def _in_order_items(self, subtree, l):
        """Performs an in-order traversal of 'subtree', adding its items to 'l'."""
        
        #***************************
        #*** Your code goes here ***
        #***************************
        
        if subtree == None:
            return
        else:
            self._in_order_items(subtree.left,l)
            l.append(subtree.value)
            self._in_order_items(subtree.right,l)
            
        


    #-------------------------------------------
    def pre_order_items(self):
        """
        Returns a list of all items in the tree using pre-order traversal.
        
        >>> b = BinarySearchTree()
        >>> b.insert(5)
        >>> b.insert(3)
        >>> b.insert(4)
        >>> b.pre_order_items()
        [5, 3, 4]
        """
        l = []
        self._pre_order_items(self.root, l)
        return l


    #-------------------------------------------
    def _pre_order_items(self, subtree, l):
        """Performs a pre-order traversal of 'subtree', adding its items to 'l'."""
        
        #***************************
        #*** Your code goes here ***
        #***************************

        if subtree == None:
            return
        else:
            l.append(subtree.value)
            self._pre_order_items(subtree.left,l)
            self._pre_order_items(subtree.right,l)
 
    
    
    #-------------------------------------------    
    def post_order_items(self):
        """
        Returns a list of all items in the tree using post-order traversal.
        
        >>> b = BinarySearchTree()
        >>> b.insert(5)
        >>> b.insert(3)
        >>> b.insert(4)
        >>> b.post_order_items()
        [4, 3, 5]
        """ 
        l = []
        self._post_order_items(self.root, l)
        return l


    #-------------------------------------------
    def _post_order_items(self, subtree, l):
        """Performs a post-order traversal of 'subtree', adding its items to 'l'."""
        
          #***************************
          #*** Your code goes here ***
          #***************************

        if subtree == None:
            return
        else:
            self._post_order_items(subtree.left,l)
            self._post_order_items(subtree.right,l)
            l.append(subtree.value)
    #-------------------------------------------
    def __contains__(self, value):
        """
        Returns True if the tree contains an item, False otherwise.
        
        >>> b = BinarySearchTree()
        >>> b.insert(5)
        >>> b.insert(3)
        >>> b.insert(4)
        >>> 4 in b
        True
        >>> 999 in b
        False
        """
        return self._contains(self.root, value)

    
    #-------------------------------------------    
    def _contains(self, tree, value):
        # Base case -- reached the end of the tree
        if tree is None:
            return False
        # Found the item
        if value == tree.value:
            return True
        # The item is to the left
        elif value < tree.value:
            return self._contains(tree.left, value)
        # The item is to the right
        else:
            return self._contains(tree.right, value)
        
        
    #-------------------------------------------   
    def __len__(self):
        """
        Returns the number of items in the tree.
        
        >>> b = BinarySearchTree()
        >>> b.insert(5)
        >>> b.insert(3)
        >>> len(b)
        2
        >>> b.insert(4)
        >>> len(b)
        3
        """
        return self._len(self.root)
 
 
    
    #-------------------------------------------
    def _len(self, tree):
        if tree is None:
            return 0
        return 1 + self._len(tree.left) + self._len(tree.right)


    
    #-------------------------------------------
    def remove(self, value):
        """
        Removes the first occurrence of value from the tree.
        
        >>> b = BinarySearchTree()
        >>> b.insert(5)
        >>> b.insert(3)
        >>> b.insert(4)
        >>> 4 in b
        True
        >>> b.remove(3)
        >>> 3 in b
        False
        >>> b.insert(9)
        >>> b.insert(7)
        >>> b.insert(6)
        >>> b.insert(6.5)
        >>> b.remove(5)
        >>> b.root.value
        6
        >>> 6.5 in b
        True
        """
        self.root = self._remove(self.root, value)

        
    #-------------------------------------------
    def _remove(self, subtree, value):
        # value is not in the tree
        if subtree is None:
            return subtree
        # The item should be on the left
        if value < subtree.value:
            subtree.left = self._remove(subtree.left, value)
        # The item should be on the right
        elif value > subtree.value:
            subtree.right = self._remove(subtree.right, value)
        # The item to be deleted IS subtree!
        else:
          #***************************
          #*** Your code goes here ***
          #***************************
            if subtree.left==None and subtree.right==None:
                subtree=None
            elif subtree.left!=None and subtree.right==None:
                subtree=subtree.left
            elif subtree.left==None and subtree.right!=None:
                subtree=subtree.right
            else:
                pass
         
        return subtree
    pass




    #-------------------------------------------
    def _in_order_successor(self, parent):
        """
        Returns the value of the in-order successor and removes it from
        the tree.
        
        >>> b = BinarySearchTree()
        >>> b.insert(7)
        >>> b.insert(5)
        >>> b.insert(15)
        >>> b.insert(9)
        >>> b.insert(13)
        >>> b.insert(11)
        
        >>> b._in_order_successor(b.root).value
        9
        >>> str(b.root.right)
        "['15', l:{['13', l:{['11', l:{None} r:{None}]} r:{None}]} r:{None}]"
        
        >>> b._in_order_successor(b.root).value
        11
        >>> str(b.root.right)
        "['15', l:{['13', l:{None} r:{None}]} r:{None}]"
        
        >>> b._in_order_successor(b.root).value
        13
        >>> str(b.root.right)
        "['15', l:{None} r:{None}]"
        
        >>> b._in_order_successor(b.root).value
        15
        >>> str(b.root)
        "['7', l:{['5', l:{None} r:{None}]} r:{None}]"
        """
        
        #***************************
        #*** Your code goes here ***
        #***************************
        self._in_order_successor_recursive(subtree)
        pass


    
       
    #-------------------------------------------    
    def _in_order_successor_recursive(self, subtree):
        """
        Takes a subtree with a left branch and searches down for the in order
        successor. 
        
        Note: This method does not handle the condition where the in order 
        successor is the direct descendant of the node to be removed. That 
        condition must be checked for before calling this method!!
        
        >>> b = BinarySearchTree()
        >>> b.insert(7)
        >>> b.insert(15)
        >>> b.insert(9)
        >>> b.insert(13)
        >>> b.insert(11)
        
        >>> b._in_order_successor_recursive(b.root.right).value
        9
        >>> b._in_order_successor_recursive(b.root.right).value
        11
        >>> b._in_order_successor_recursive(b.root.right).value
        13
        
        """
        
        
        #***************************
        #*** Your code goes here ***
        #***************************
        
        # If the left child of subtree has no left child, it is the in-order 
        # successor, de-link it from subtree and return its value.
        # Remember to connect its children to subtree if it has any, 
        # so they aren't lost.        
    
        pass
        

l = load_file('list3.txt')
tree = BinarySearchTree()
for li in l:
    tree.insert(li)
pass

if __name__ == '__main__':
    import doctest
    import os
    os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    doctest.testmod()
    