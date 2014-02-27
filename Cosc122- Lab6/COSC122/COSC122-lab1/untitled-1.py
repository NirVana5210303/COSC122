import time
from Arrays import SortedArray
s = SortedArray ()
start_time = time . clock ()
s.load_file("file3")
end_time = time.clock()
time_taken = end_time - start_time
print " Took {0:.3f} seconds .".format(time_taken)