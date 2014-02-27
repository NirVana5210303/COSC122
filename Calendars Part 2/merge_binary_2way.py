#!/usr/bin/env python

import eventlib, comparelib, sys, time, json, collections

counter = comparelib.Counter()

def merge_events(left, right):
  """Given two lists of events, merge them together using the start_timestamp
  for ordering.
  
  If the start timestamp of both is the same prefer the left calendar first."""
  # --[ WRITE CODE HERE ]-->
  merged = []
  l = 0; r = 0
  # Merge the two lists by stitching them together.
  # You will need to walk through the lists left and right using l and r as
  # the index. Check which event is nearer e.g. left[l] <= right[r] implies
  # that left[l] should come before right[r]. When you select an event, you
  # need to increment the respective index.
  #
  # Call counter.increment() for every comparision between events.
  # This implementation is the same as in merge_linear_2way.
  while l < len(left) and r < len(right):
    counter.increment()
    if left[l] <= right[r]:
      merged.append(left[l])
      l += 1
    else:
      merged.append(right[r])
      r += 1 
      
  merged += left[l:]
  merged += right[r:]      
  
  return merged
  # <--[ WRITE CODE HERE ]--


def binary_merge(calendars):
  """Given a list of calendars, merge each pair. If there is one left over,
	merge it with the previously merged pair in sequence."""
  # --[ WRITE CODE HERE ]-->
  # Merge each pair of calendars (a, b) and append the array into result.
  # If there are an odd number of calendars, take the last calendar and merge
  # it with merged result of the previous two so that result has an even number
	# of calendars.
  # e.g. where a, b, c, d, e are calendars and m is the function merge_events:
  #   binary_merge([a, b, c, d]) -> [m(a, b), m(c, d)]
  #   binary_merge([a, b, c, d, e]) -> [m(a, b), m(m(c, d), e)]
  result = []
  n_pairs = len(calendars) // 2
  
  for i in range(0, n_pairs):
      result.append(merge_events(calendars[2*i],calendars[2*i+1]))
      
  if len(calendars) %2 == 1:
    result[-1]= merge_events(result[-1], calendars[-1])
    
  return result
  

  # <--[ WRITE CODE HERE ]--


def merge_calendars(calendars):
  # --[ WRITE CODE HERE ]-->
  # Repeatedly binary merge calendars until only one calendar remains;
  # return that calendar.
  # <--[ WRITE CODE HERE ]--
  
  while len(calendars) > 1:
    n_cal=calendars
    return binary_merge(n_cal)[0]


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print >> sys.stderr, "You must provide at least two calendars as arguments!"
  else:
    calendars = collections.deque()

    for path in sys.argv[1:]:
      calendars.append(eventlib.load_file(path))

    start = time.clock()

    merged = merge_calendars(calendars)

    end = time.clock()

    print >> sys.stderr, end - start
    print >> sys.stderr, counter
    eventlib.save(sys.stdout, merged)
