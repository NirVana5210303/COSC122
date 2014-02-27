#!/usr/bin/env python

import eventlib, comparelib, sys, time, json

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


def merge_calendars(calendars):
  """Merge the calendars two at a time from left to right."""
  
  # --[ WRITE CODE HERE ]-->
  # Merge all the calendars from first to last in order. A simple way to do this
  # is to take the first calendar as the initial list, then merge all remaining
  # calendars.
  
  if len(calendars) == 0:
    return []
  
  if len(calendars) < 2:
    return calendars[0]
  result = calendars[0]
  for i in range(1, len(calendars)):
    result = merge_events(result, calendars[i])
    
    
  #middle = len(calendars) // 2
  #left = merge_calendars(calendars[:middle])
  #right = merge_calendars(calendars[middle:])
  return result

# <--[ WRITE CODE HERE ]--


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print >> sys.stderr, "You must provide at least two calendars as arguments!"
  else:
    calendars = []

    for path in sys.argv[1:]:
      calendars.append(eventlib.load_file(path))
  
    start = time.clock()
  
    merged = merge_calendars(calendars)
  
    end = time.clock()
  
    print >> sys.stderr, end - start
    print >> sys.stderr, counter
    eventlib.save(sys.stdout, merged)
