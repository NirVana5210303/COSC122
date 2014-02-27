#!/usr/bin/env python

import eventlib, comparelib, sys, time, json

counter = comparelib.Counter()

def find_minimum(top, calendars):
  """Given a list of indices and corresponding calendars, find the index for the
  event with the nearest start_timestamp."""
  
  # --[ WRITE CODE HERE ]-->
  # Linearly iterate over the top events in the calendars. Each calendar has a
  # corresponding event given by calendars[i][top[i]].
  # Return the smallest index i for the nearest event such that:
  # calendars[i][top[i]] <= calendars[j][top[j]] for all j
  # Call counter.increment() for any comparison between events.
  index = 0
  minum = calendars[0][top[0]]
  for i in range(1,len(top)):
    counter.increment()
    if minum > calendars[i][top[i]]:
      minum = calendars[i][top[i]]
      index = i
  return index
  # <--[ WRITE CODE HERE ]--


def merge_calendars(calendars):
  """Given a list of calendars, merge them by taking the earliest event from all
  the calendars once at a time until they are all empty."""
  merged = []

  # --[ WRITE CODE HERE ]-->
  # Assign an index for each calendar. Select the earliest event from all
  # calendars using find_minimum which takes this list of indices and a list of
  # calendars. Append this event to the list of merged events.
  # If the calendar becomes empty remove it from the list of calendars and the 
  # list of indices.
  # <--[ WRITE CODE HERE ]--
  
  top = []
  while len(top) < len(calendars):
    top.append(0)
  
  while len(calendars) > 0:
    index = find_minimum(top, calendars)
    merged.append(calendars[index][top[index]])
    top[index] += 1
    if top[index] == len(calendars[index]):
      calendars.pop(index)
      top.pop(index)
      if len(calendars) == 1:
        for i in calendars[0][top[0]:]:   # coz the len(calendars)== 1 so only one item need to check
          merged.append(i)
        calendars.pop(0)
  return merged


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print >> sys.stderr, "You must provide at least two calendars as arguments!"
  else:
    calendars = []

    for path in sys.argv[1:]:
      events = eventlib.load_file(path)
      if len(events) > 0:
        calendars.append(events)
  
    start = time.clock()
  
    merged = merge_calendars(calendars)
  
    end = time.clock()
  
    print >> sys.stderr, end - start
    print >> sys.stderr, counter
    eventlib.save(sys.stdout, merged)
