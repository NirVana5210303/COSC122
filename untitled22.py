import time
from Arrays import LinearArray
s = LinearArray ()
start_time = time . clock ()
s.load_file("file0")
end_time = time.clock()
time_taken = end_time - start_time
print " Took {0:.3f} seconds .".format(time_taken)