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
    
global counter
counter = 0
def selection_sort(file_name):
    """Returns a list containing the numbers from the file in order."""
    alist = load_file(file_name)
    global counter
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax  = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
                counter+=1        
        alist[fillslot], alist[positionOfMax]  = alist[positionOfMax], alist[fillslot]
        counter+=1
    return counter


def insertion_sort(file_name):
    global counter
    counter = 0
    """Returns a list containing the numbers from the file in order."""
    alist = load_file(file_name)
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1
            counter = counter + 1
        alist[position] = currentvalue
        counter = counter + 1
    return counter


def shell_sort(file_name):
    global num
    """Returns a list containing the numbers from the file in order."""
    alist = load_file(file_name)
    sub_list_count = len(alist) // 2
    gaplist = []
    while sub_list_count > 0 :
        for start_position in range(sub_list_count):
            gap_insertion_sort(alist,start_position,sub_list_count)
        #print("After increments of size", sub_list_count, "the list is", alist)
        gaplist += [sub_list_count]
        sub_list_count = sub_list_count //2
    return num

def gap_insertion_sort(alist, start, gap):
    global num
    """Used by shell sort to sort the sublist of items 
       seperated by the given gap."""
    for i in range (start+gap, len(alist), gap):
        current_value = alist[i]
        position = i
        while position >= gap and alist[position-gap] > current_value:
            num = num + 1
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = current_value
        num = num + 1
        if position < gap:
            num = num - 1


num = 0
#print selection_sort('file3.txt')
print insertion_sort('file3.txt')
#print shell_sort('file4.txt')



#selection_sort('file0.txt')
#insertion_sort('file0.txt')
#shell_sort('file7.txt')