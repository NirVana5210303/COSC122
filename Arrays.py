class LabArray(object):
    """
    Abstract base class for array implementations.
    Subclasses only need to store positive integers.
    """
    def insert(self, value): 
        """Inserts the given value into the array."""
        pass
    
    def remove(self, value): 
        """Removes the given value from the array."""
        pass
    
    def find(self, value): 
        """
        Searches the array for a given value.
        Returns True if the value is found in the array, and False otherwise.
        """
        pass

    def load_file(self, fileName):
        """
        Loads the array from a file. Files contain lines in the format:
            [instruction] [value]
        Valid instructions are:
            i : Insert [value]
            f : Find [value]
            d : Delete [value]
        [value] must be a valid positive integer.
        """
        f = open(fileName)
        for line in f:
            i, v = line.split(' ')
            v = int(v)
            if i == 'i':
                self.insert(v)
                print 'insert\t{0:d}\t{1:d} comparisons'.format(v, self.comparisons)
            elif i == 'f':
                print 'find\t{0}'.format(v),
                if self.find(v):
                    print '\t{0:d} comparisons (found)'.format(self.comparisons)
                else:
                    print '\t{0:d} comparisons (not found)'.format(self.comparisons)
            elif i == 'd':
                self.remove(v)
                print 'remove\t{0:d}\t{1:d} comparisons'.format(v, self.comparisons)
        f.close()


        

class LinearArray(LabArray):
    """Implements an array using an un-ordered Python list."""
    def __init__(self):
        self.data = list() # Create the list to store the data
        self.comparisons = 0 # Reset comparison counter
    
    def insert(self, value):
        self.comparisons = 0
        # Add the item to the end of the data list
        self.data.append(value)
        
    def remove(self, value):
        # Look for the index in the list that contains 
        # the element to delete
        index = self.find_index(value)

        # If we've found the item...
        if index != -1:
            # Delete it from the list
            del self.data[index]

    def find(self, value):
        return self.find_index(value) != -1

    def find_index(self, value):
        """
        Finds the index of the given value in the data list.
        Returns either the index of the item in the list, or -1 if
        the item doesn't exist.
        """
        self.comparisons = 0      
        
        # Counter for how many comparisons are done
        for item in range(len(self.data)):
            self.comparisons +=1
            if self.data[item]==value:
                return item
        
            # Loop through each item in the data list
            # Add one to comparisons for each comparison
            # involving a list element#
        # If the item is equal to our search value
        # return the index this item is at
        return -1
        # If we loop through everything and haven't found
        # the item, return -1


class SortedArray(LabArray):
    """
    Implements an array using a Python list, but stores the items in
    sorted order (rather than the order they are inserted).
    """
    def __init__(self):
        self.data = list()
        self.comparisons = 0

    def insert(self, value):
        self.comparisons = 0
        
        # Find the correct index to insert value using a binary search
        lower_bound = 0
        upper_bound = len(self.data)
        index = 0
        # When these cross, they're at the index the item should be at
        while lower_bound < upper_bound:
            self.comparisons +=1
            index = (lower_bound + upper_bound) / 2
            if self.data[index] < value:
                lower_bound = index + 1 # Look in the upper half
            else:
                upper_bound = index     # Look in the lower half
        self.data.insert(lower_bound, value)

    def remove(self, value):
        # Find the index to remove
        idx = self.find_index(value)
        # If we've found the item...
        if idx != -1:
            # Delete it from the list
            # (this will shuffle all of the higher items down for us)
            del self.data[idx]
            
    def find(self, value):
        return self.find_index(value) != -1
    
    def find_index(self, value):
        """
        Finds the index of the given value in the data list.
        Returns either the index of the item in the list, or -1 if
        the item doesn't exist.
        """
        self.comparisons = 0
        lower_bound = 0
        upper_bound = len(self.data)
        index = 0
        while lower_bound < upper_bound:
            self.comparisons +=1
            index = (lower_bound + upper_bound) / 2
            if self.data[index] == value: 
                # Found it!
                
                return index
            if self.data[index] < value:
                # Look in the upper half
                self.comparisons +=1
                lower_bound = index + 1 
            else:
                self.comparisons +=1
                # Look in the lower half
                # If we haven't found it by now, it doesn't exist
                upper_bound = index     
        #didn't find it
        return -1


                

class BitVectorArray(LabArray):
    """Implements an array using a variation on a bit vector (bitmap)."""

    def __init__(self, max_value):
        """
        Creates a new BitVectorArray.
        maxValue is the largest integer value that can be stored in this set.
        """
        self.data = [0 for n in xrange(max_value+1)]
        self.comparisons = 0

    def remove(self, value):
        if self.data[value]:
            self.data[value] -= 1

    def insert(self, value):
        self.data[value] += 1

    def find(self, value):
        return self.data[value] > 0
    
    
