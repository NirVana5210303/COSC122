#-------------------------------------------------------------------------------
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    # Note: we use nice Python style for accessing object data
    # ie, we don't use get_data(), get_next(), etc
    # To get the data in a Node simply use data_item = my_node.data
    # To get the next Node use next_node = my_node.next
    # See the Stack push method for an example



#-------------------------------------------------------------------------------
class Stack (object):
    """ Implements a Stack using a Linked List"
    >>> s = Stack()
    >>> s.push('a')
    >>> s.printList()
    List is: a -> None
    >>> s.length()
    1
    >>> s.pop()
    'a'
    >>> s.printList()
    List is: None
    >>> s.push('b')
    >>> s.printList()
    List is: b -> None
    >>> s.push('c')
    >>> s.printList()
    List is: c -> b -> None
    >>> s.length()
    2
    >>> s.peek()
    'c'
    >>> s.printList()
    List is: c -> b -> None
    >>> s.pop()
    'c'
    >>> s.printList()
    List is: b -> None
    """

    def __init__(self):
        self.head = None
        
    def push(self, item):
        """push a new item on to the stack"""
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        """pop an item off the top of the stack, and return it"""
        a=self.head
        self.head=self.head.next
        return a.data
        
    def peek(self):
        """pop an item on the top of the top of the stack, but don't remove it"""
        return self.head.data
    
    def isEmpty(self):
        return self.head == None
    
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def printList(self):
        """prints all the items in the list starting from the begining of the list
        seperated by -> and ending with None"""
        print "List is:",
        """ add your code here"""
        if self.head==None:
            print "None"
        else:
            p=self.head
            while p!=None:
                print p.data,'->',
                p=p.next
            print "None"
            
                


        
#-------------------------------------------------------------------------------
class Queue (object):
    """ Implements a Queue using a Linked List"
    >>> q = Queue()
    >>> q.enqueue('a')
    >>> q.printList()
    List is: a -> None
    >>> q.length()
    1
    >>> q.enqueue('b')
    >>> q.printList()
    List is: a -> b -> None
    >>> q.enqueue('c')
    >>> q.printList()
    List is: a -> b -> c -> None
    >>> q.length()
    3
    >>> q.dequeue()
    'a'
    >>> q.printList()
    List is: b -> c -> None
    """
    
    def __init__(self):
        self.head = None
        
    def enqueue(self, item):
        """Add an item onto the tail of the queue."""
        node1 = Node(item)
        q=self.head
        if self.head==None:
            self.head=node1
        else:
            while q.next!=None:
                q=q.next
            q.next=node1
    
    def dequeue(self):
        """Remove an item from the head of the queue and return it."""
        d=self.head
        self.head=self.head.next
        return d.data
    
    def isEmpty(self):
        return self.head == None
    
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def printList(self):
        """prints all the items in the list starting from the begining of the list,
        seperated by -> and ending with None"""
        print "List is:",
        """ add your code here"""
        if self.head==None:
            print "None"
        else:
            p=self.head
            while p!=None:
                print p.data,'->',
                p=p.next
            print "None"


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    import doctest
    import os
    os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    
    # Uncomment the doctest line below to run the doctests
    # Can enter an infinite loop if your code isn't implemented correctly
    doctest.testmod()