import time, random
from quicksort import *
from matplotlib import pyplot

list_of_ns = range(40,800,40)
n_trials = 100
avg_times_sorted = []

for n in list_of_ns:
    total_time_sorted = 0
    for i in range(n_trials):
        x = range(n)
        start = time.clock()
        s = quicksort(x,'left-pivot')
        end = time.clock()
        time_taken = end-start
        total_time_sorted += time_taken
    avg_time_sorted = total_time_sorted/n_trials
    avg_times_sorted.append(avg_time_sorted)
    
pyplot.plot(list_of_ns,avg_times_sorted,'bo')
pyplot.title("Time vs. List size, average of {0} trials".format(n_trials))
pyplot.xlabel('n')
pyplot.ylabel('Average Time per sort')
pyplot.show()

    
