import time
import random

def run_list_trials(num_trials=1):
    """ Creates empty lists of increasing size
    then searches for a randomly generated number in each list.
    Returns two lists, the first contains all the list sizes tried and 
    the second contains the average time per locate operation for each list size. """
    
    list_of_times = []
    list_of_ns = range(20000,1000001,20000)
    num_list=range(10000)
    for n in list_of_ns:
        num_list = list(range(n)) #creates a list of n items
        
        #run trials, each on simply trying to locate the number in the list
        start=time.clock() 
        for i in range(num_trials):
            #try to find random number (between 1 and n) in the list
            random.randrange(n) in num_list
        end= time.clock()       
      
        #print number of trials and time taken (with a tab in between)
        time_taken_per_locate = (end - start)/num_trials
        print "{0:7d}\t{1:10.8f}".format(n, time_taken_per_locate)
        
        #keep track of all the times
        list_of_times.append(time_taken_per_locate)
    return list_of_ns,list_of_times


def run_dictionary_trials():
    """ Creates an empty Dictionary and search for a randomly generated number 
    in the dictionary"""
    for n in range(20000,1000001,20000):
        dict_num = {} #create an empty dictionary
        for i in range (n): #fill the dictionary with n items
            dict_num[i] = None
        start = time.clock()
        #checks whether a randomly generated number is in the dictionary
        random.randrange(n) in dict_num 
        end = time.clock()
        time_taken = end - start
        print "{0:7d}\t{1:10.8f}".format(n,time_taken)

   
if __name__ == "__main__":
    print "LIST TRIAL RUN"
    run_list_trials(5)

    #print "\n\n\nDICTIONARY TRIAL RUN"
    #run_dictionary_trials()