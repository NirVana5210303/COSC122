import time
#-------------------------------------------------------------------------------
class Frequency(object):
    """
    Stores a letter:frequency pair.

    >>> f = Frequency('c', 2)
    >>> f.item
    'c'
    >>> f.frequency
    2
    >>> f
    'c': 2
    """
    def __init__(self, item, frequency):
        self.item = item
        self.frequency = frequency
        self.next = None
        
    def increment(self):
        self.frequency += 1
    
    def __repr__(self):
        return "\'{0}\': {1:d}".format(self.item, self.frequency)

#-------------------------------------------------------------------------------
class FreqList(object):

    """
    NOTE: This is a parent class for Unsorted, NicerSorted and Sorted FreqLists
    So, don't write any code here:)
    Stores a collection of Frequency objects as a linked list.
    """
    def __init__(self):
        self.head = None
    
    def get_item_frequency(self,item):
        """Returns Frequency object for item, if found else returns None."""
        current = self.head
        found = False
        while not(current==None):
            if current.item == item:
                return current.frequency
            current = current.next
        return 0    
    
    def get_xy_for_plot(self):
        x = []
        y = []
        curr_item = self.head
        while not(curr_item == None):
            x.append(curr_item.item)
            y.append(curr_item.frequency)
            curr_item = curr_item.next
        return x,y    
    
    def __repr__(self):
        """
        Retruns the items together with their letter frequencies
        """
        item_strs = []
        current = self.head
        while current is not None:
            item_strs.append(repr(current))
            current = current.next
        return '\n'.join(item_strs)
    

    
#-------------------------------------------------------------------------------    
class UnsortedFreqList(FreqList):
        
    def add(self, new_item):
        """
        Adds the given `letter` with a frequency of 1 as a Frequency object
        to the list. If the given `letter` is already in the list, the frequency 
        is incremented by 1. 
        
        NOTE: If not in the list then the item is added at start

        >>> f = UnsortedFreqList()
        >>> f.add('a')
        >>> f
        'a': 1
        >>> f.add('b')
        >>> f
        'b': 1
        'a': 1
        >>> f.add('a')
        >>> f
        'b': 1
        'a': 2
        """
        
        #insert your code here and remove the pass
        pass
    

#-------------------------------------------------------------------------------    
class NicerUnsortedFreqList(FreqList):
        
    def add(self, new_item):
        """
        Adds the given `letter` with a frequency of 1 as a Frequency object
        to the list. If the given `letter` is already in the list, the frequency 
        is incremented by 1.  
        
        NOTE: If not in list, the item is added to the end.

        >>> f = NicerUnsortedFreqList()
        >>> f.add('a')
        >>> f
        'a': 1
        >>> f.add('b')
        >>> f
        'a': 1
        'b': 1
        >>> f.add('a')
        >>> f
        'a': 2
        'b': 1
        """
        #insert your code here and remove the pass
        pass

    
    
#-------------------------------------------------------------------------------    
class SortedFreqList(FreqList):
    
    def add(self, new_item):
        """
        Adds the given `letter` with a frequency of 1 as a Frequency object
        to the list. If the given `letter` is already in the list, the frequency 
        is incremented by 1.

        >>> f = SortedFreqList()
        >>> f.add('a')
        >>> f
        'a': 1
        >>> f.add('b')
        >>> f
        'a': 1
        'b': 1
        >>> f.add('b')
        >>> f
        'b': 2
        'a': 1
        """
        #insert your code here and remove the pass     
        pass
    

#-------------------------------------------------------------------------------
# End of Class #===============================================================================
#===============================================================================


def make_single_char_unsorted_freq_list(doc):
    """
    Calculate the letter frequencies using unsorted list
    """
    f = UnsortedFreqList()
    start = time.clock()
    for char in doc:
        f.add(char)
    end = time.clock()
    return f, (end-start)
    

def make_single_char_nicer_unsorted_freq_list(doc):
    """
    Calculate the letter frequencies using unsorted list
    """
    f = NicerUnsortedFreqList()
    start = time.clock()
    for char in doc:
        f.add(char)
    end = time.clock()
    return f, (end-start)

    
def make_pairs_unsorted_freq_list(doc):
    """
    Calculate the letter pair frequencies using unsorted list
    """
    f = UnsortedFreqList()
    first_in_pair = doc[0]
    start = time.clock()
    for i in range(1,len(doc)):
        char = doc[i]
        pair = first_in_pair + char
        f.add(pair)
        first_in_pair = char
    end = time.clock()
    return f, (end-start)


def make_pairs_nicer_unsorted_freq_list(doc):
    """
    Calculate the letter pair frequencies using unsorted list
    """
    f = NicerUnsortedFreqList()
    first_in_pair = doc[0]
    start = time.clock()
    for i in range(1,len(doc)):
        char = doc[i]
        pair = first_in_pair + char
        f.add(pair)
        first_in_pair = char
    end = time.clock()
    return f, (end-start)

    
def make_single_char_sorted_freq_list(doc):
    """
    Calculate the letter frequencies using sorted list
    """
    f = SortedFreqList()
    start = time.clock()
    for char in doc:
        f.add(char)
    end = time.clock()
    return f, (end-start)

       
def make_pairs_sorted_freq_list(doc):
    """
    Calculate the letter pair frequencies using sorted list
    """
    f = SortedFreqList()
    first_in_pair = doc[0]
    start = time.clock()
    for i in range(1,len(doc)):
        char = doc[i]
        pair = first_in_pair + char
        f.add(pair)
        first_in_pair = char
    end = time.clock()
    return f, (end-start)



def plot_freq_list(freq_list):
    """ Plots a bar chart showing item frequency.
    Will take any of the various freq_list classes, eg, unsorted, sorted etc"""
    from matplotlib import pyplot
    (x,y) = freq_list.get_xy_for_plot()
    item_list_nums=list(range(len(x)))
    width=0.8
    pyplot.bar(item_list_nums,y,width)
    pyplot.title("Frequency Distribution")
    pyplot.xlabel('Letter')
    tick_positions = [i+width/2 for i in item_list_nums]
    pyplot.xticks(tick_positions,x)
    pyplot.ylabel('Frequencies')
    pyplot.draw()
    pyplot.show()



#-------------------------------------------------------------------------------
def run_tests(filename):
    """Runs sorted/unsorted * 1/2 char tests"""
    f = open(filename)
    doc = format_document(f.read())
    f.close()
    
    print "\n\n"
    print "--------------------------------------"
    print "Tests for "+filename
    print "Doc size = "+str(len(doc))+" chars"
    print "======================================"
    
    
    # Comment/Uncomment relevant frequency list runs
    # Use ctrl+/ to comment a selection of lines in Wing
    # Use ctrl+? to uncomment a selection of lines in Wing
    
    #(freq_list, total_time) = make_single_char_unsorted_freq_list(doc)
    #print filename+' - Chars, Unsorted, t = '+str(total_time)
    #print freq_list
    #print "\n"

    #(freq_list , total_time) = make_single_char_nicer_unsorted_freq_list(doc)
    #print filename+' - Chars, NicerUnsorted, t = '+str(total_time)
    #print freq_list
    #print "\n"

    #(freq_list , total_time) = make_single_char_sorted_freq_list(doc)
    #print filename+' - Chars, Sorted, t = '+str(total_time)
    #print freq_list
    #print "\n"
    

    
    #(freq_list, total_time) = make_pairs_unsorted_freq_list(doc)
    #print filename+' - Pairs, Unsorted, t = '+str(total_time)
    #print freq_list
    #print "\n"

    #(freq_list, total_time) = make_pairs_nicer_unsorted_freq_list(doc)
    #print filename+' - Pairs, NicerUnsorted, t = '+str(total_time)
    #print freq_list
    #print "\n"

    
    #freq_list , total_time = make_pairs_sorted_freq_list(doc)
    #print filename+' - Pairs, Sorted, t = '+str(total_time)
    #print freq_list
    #print "\n"
 


###############################################################################
#################### DO NOT MODIFY ANYTHING in this area ######################
###############################################################################

def format_document(d):
    """
    Re-formats `d` by collapsing all whitespace characters into a space and 
    stripping all characters that aren't letters or punctuation. Converts all 
    uppercase characters in the file to lower case.
    
    """
    import re
    from unicodedata import category
    d = unicode(d, 'utf-8')
    # Collapse whitespace
    d = re.compile(r'\s+', re.UNICODE).sub(' ', d)
    
    # http://www.unicode.org/reports/tr44/#General_Category_Values
    allowed_categories = ('Lu', 'Ll', 'Lo', 'Po', 'Zs') # letters, punc, spaces
    # allowed_categories = ('Lu', 'Ll', 'Lo', 'Zs') # just letters and spaces

    d = u''.join([c.lower() for c in d if category(c) in allowed_categories])
    # Disable the encode to properly process a unicode corpus
    return d.encode('utf-8')
###############################################################################
###############################################################################

if __name__ == '__main__':
    import doctest
    import os
    os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    

    # Uncomment this line to run the doctests
    doctest.testmod()
    # Can enter an infinite loop if something isn't implemented correctly
    # So test on small data file first    
    
    
    # Uncomment the files you want to test
    # ------------------------------------
    #run_tests("le_rire.txt")         # smallest corpus
    #run_tests("ulysses.txt")         # medium corpus
    #run_tests("war_and_peace.txt")   # Hugeomongous corpus
