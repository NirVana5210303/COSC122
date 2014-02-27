
class Stack(object):
    """
    Implements a Stack using a Python list.
    
    >>> s = Stack()
    >>> s.push('a')
    >>> s.peek()
    'a'
    >>> s.pop()
    'a'
    >>> s.push('a')
    >>> s.push('b')
    >>> s.peek()
    'b'
    >>> len(s)
    2
    >>> s.pop()
    'b'
    >>> len(s)
    1
    """
    def __init__(self):
        self._items = []
        
    def push(self, item):
        """Push a new item onto the stack."""
        self._items.append(item)
    
    def pop(self):
        """Pop an item off the top of the stack and return it."""
        self._items.pop()
    
    def peek(self):
        """Return the item on the top of the stack, but don't remove it."""
        return self._items[-1]
    
    def is_empty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "Bottom -> "+repr(self._items)+" <- Top"
    
    
class Queue(object):
    """
    Implements a Queue using a Python list.
    
    >>> q = Queue()
    >>> q.enqueue('a')
    >>> q.dequeue()
    'a'
    >>> q.enqueue('a')
    >>> q.enqueue('b')
    >>> len(q)
    2
    >>> q.dequeue()
    'a'
    >>> len(q)
    1
    """
    def __init__(self):
        self._items = []
        
    def enqueue(self, item):
        """Add an item onto the end of the queue."""
        self._items.append(item)
    
    def dequeue(self):
        """Remove an item from the front of the queue and return it."""
        self._items.remove(self._items[0])
    
    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "Front -> "+repr(self._items)+" <- Rear"
    
    
    
class Deque(object):
    """
    Implements a Deque using a Python list.
    
    >>> d = Deque()
    >>> d.enqueue_front('a')
    >>> d.dequeue_front()
    'a'
    >>> d.enqueue_front('a')
    >>> d.enqueue_rear('b')
    >>> len(d)
    2
    >>> d.dequeue_rear()
    'b'
    >>> len(d)
    1
    """
    def __init__(self):
        self._items = []
        
    def enqueue_front(self, item):
        """Add an item onto the front of the queue."""
        self._items.insert(0,item)
    
    def enqueue_rear(self, item):
        """Add an item onto the rear of the queue."""
        self._items.append(item)
        
    def dequeue_front(self):
        """Remove an item from the front of the queue and return it."""
        return self._items.pop(0)

    def dequeue_rear(self):
        """Remove an item from the rear of the queue and return it."""
        return self._items.pop()
   
    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "Front -> "+repr(self._items)+" <- Rear"
    
     
   
    
if __name__ == '__main__':
    import doctest
    #import os
    #os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    
    #Uncomment the next line to run the doctests
    #doctest.testmod()
    #If everything works then the doctests will output nothing...