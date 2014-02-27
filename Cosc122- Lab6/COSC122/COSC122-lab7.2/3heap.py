#--------------------------------------------------------------------------
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
class Heap(object):
    """An abstract interface for a Heap."""
    def __init__(self):
        # Create a list to store heap items.
        self._items = [0]
       
    def insert(self, item):
        #don't implement here
        #this is just a place holder
        pass
    
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        """Returns the actual length of the heap,
        ie, how many items are in the heap"""
        return len(self._items)-1
    
    def __repr__(self):
        """Returns only the items in the heap,
        ie, leaves out _items[0] as the heap
        data starts from index 1..."""
        return repr(self._items[1:])
   

#-------------------------------------------------
#-------------------------------------------------
class Max_3_Heap(Heap):
    """Implementation of a max-three-heap.
    Each child must be smaller than or equal to its parent.
    Each parent has up to 3 children.
    First element of the heap is stored in _items[1]
    left_child_index = parent_index*3-1
    middle_child_index = parent_index*3
    right_child_index = parent_index*3+1
    
    parent = (child+1)//3"""

    def __init__(self):
        super(Max_3_Heap, self).__init__()
    

    #-------------------------------------------------
    def insert(self, item):
        """Inserts a given item into the heap.
    
        >>> h = Max_3_Heap()
        >>> h.insert(3)
        >>> h._items
        [0, 3]
        >>> h.insert(7)
        >>> h._items
        [0, 7, 3]
        >>> h.insert(5)
        >>> h._items
        [0, 7, 3, 5]
        >>> h.insert(2)
        >>> h._items
        [0, 7, 3, 5, 2]
        >>> h.insert(6)
        >>> h._items
        [0, 7, 6, 5, 2, 3]
        """
        # Append the item to the end of the heap
        self._items.append(item)
        # Sift it up into place
        self._sift_up(len(self))
        

    #-------------------------------------------------
    def _sift_up(self, index):
        """
        Moves the item at the given index up through the heap until it finds
        the correct place for it. That is, the item is moved up through the heap
        while it is larger than its parent.
        """
        #----------------------
        #----------------------
        # Write your code here
        # parent = (index+1)//3
  
            
        #----------------------
        #----------------------
            
    #-------------------------------------------------           
    def peek_max(self):
        """
        Returns the smallest value in the heap, ie, the
        top of the heap. Doesn't change the heap.
        
        >>> h = Max_3_Heap()
        >>> h.insert(5)
        >>> h.validate()
        True
        >>> h.peek_max()
        5
        >>> h.insert(3)
        >>> h.peek_max()
        5
        >>> h.insert(7)
        >>> h.peek_max()
        7
        """
        return self._items[1]
    
    
    #-------------------------------------------------
    def delete_max(self):
        """
        Removes the largest item in the heap and returns it. Returns None if
        there are no items in the heap. Can be thought of as Popping the max
        item off the heap.
        
        >>> h = Max_3_Heap()
        >>> h.insert(5)
        >>> h.delete_max()
        5
        >>> len(h)
        0
        >>> h.insert(3)
        >>> h.insert(7)
        >>> h.delete_max()
        7
        >>> h.delete_max()
        3
        >>> len(h)
        0
        >>> tmp = map(h.insert, (3, 7, 5, 2, 4))
        >>> print h
        [7, 4, 5, 2, 3]
        >>> h.delete_max()
        7
        >>> h._items[1]
        5
        >>> h._items[2]
        4
        >>> h.delete_max()
        5
        >>> print h
        [4, 2, 3]
        >>> h = Max_3_Heap()
        >>> h.insert(1)
        >>> h.insert(5)
        >>> h.insert(2)
        >>> h.insert(7)
        >>> h.validate()
        True
        >>> h.delete_max()
        7
        >>> h.validate()
        True
        """

        if len(self)>0:
            max_item = self._items[1]
            if len(self) > 1:
                # If there are more items in the heap, swap the last one with the
                # first, and sift it down
                self._items[1] = self._items.pop()
                self._sift_down(1)
            else:
                # Otherwise, remove the item
                self._items.pop(1)
            return max_item
        else:
            return None
 

    #-------------------------------------------------
    def _sift_down(self, index):
        """
        Moves an item at the given index down through the heap until it finds
        the correct place for it. That is, the item is moved down through the
        heap while it is smaller than either of its children.
        """
        
        #----------------------
        #----------------------
        # Write your code here

        # While the item at 'index' has at least one child...
        # ....
            
        #----------------------
        #----------------------

            
    #-------------------------------------------------        
    def validate(self):
        """
        Validates the heap. Returns True if the heap is a valid max-3-heap, and
        False otherwise.
        
        >>> h = Max_3_Heap()
        >>> h._items = [0, 5, 3, 1]
        >>> h.validate()
        True
        >>> h._items = [0, 100, 90, 40, 30, 80, 60, 30, 11]
        >>> h.validate()
        True
        >>> h._items = [0, 7, 6, 1, 8]
        >>> h.validate()
        False
        """
        for i in range(2, len(self)+1):
            if self._items[(i+1)//3] < self._items[i]:
                return False
        return True
        
        
        
if __name__ == '__main__':
    import doctest
    import os
    os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    doctest.testmod()
    
    
    