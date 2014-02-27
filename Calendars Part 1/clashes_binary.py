##########################
###  Name: Liguo Jiao  ###
###                    ###
### Student ID:91734390###
##########################

#!/usr/bin/env python

import eventlib, sys, time, comparelib

counter = comparelib.Counter()

def bisect_left(a, x):
  """Return the index where to insert item x in list a, assuming a is sorted.

  The return value i(index) is such that all e(element) in a[:i] have e < str(x), and all e in
  a[i:] have e >= str(x).
  """ 
  first = 0
  last = len(a) - 1

  while first < last:
    middle = (first + last) // 2
    if x > a[middle].start_timestamp:
      counter.increment()
      first = middle + 1
    else:
      counter.increment()
      last = middle
  return last

  # --[ WRITE CODE HERE ]-->
  # Implement a standard binary search algorithm that finds an offset 
  # according to the docstring.
  # Call counter.increment() for each comparison for start_timestamp or 
  # end_timestamp.
  # <--[ WRITE CODE HERE ]--
  
  

# Does possible_event clash with any event in calendar?
# We can assume calendar is sorted, so we can do a binary search:
        
def clashes_with(possible_event, calendar):
  
  """Return true if the possible_event intersects any event in the calendar.
  
  This function should use a binary search to find the initial offset and then
  scan along until the possible_event.end_timestamp is beyond the range of
  the calendar event, similar to the linear scan.
  """
  
  offset = bisect_left(calendar, possible_event.start_timestamp)
  
  # Individual items in a particular calendar are guaranteed not to clash, but 
  # the end_timestamp may overlap with the given event, so we need to look
  # one back for clashes:
  #
  # calendar[offset].start_timestamp is >= possible_event.start_timestamp, but 
  # this doesn't mean that calendar[offset-1].end_timestamp is < 
  # possible_event.start_timestamp, e.g. the end of the previous event may
  # overlap the start of the possible event, in which case a clash may occur:
  #
  #
  #                     /----Possible Event-----\
  #     /--calendar[offset-1]---\   /--calendar[offset]--\
  #
  # ('/' means start_timestamp and '\' means end_timestamp, --- is duration)

  if offset > 0: 
    offset -= 1
  
  if len(calendar) == 0 or calendar == None:
    return False

  else:   
    for Look_Right in calendar[offset:]:
      if Look_Right.clashes_with(possible_event) == True:
	return True
      if possible_event.end_timestamp < Look_Right.start_timestamp:
	counter.increment()
	counter.increment()
	counter.increment()
	counter.increment()
	return False
     
  
  
  # -- WRITE CODE HERE-->
  # Enumerate all events starting from the given offset, and return true if it  
  # clashes.
  # Call counter.increment() for every call to Event.clashes_with
  # <--[ WRITE CODE HERE ]--
  
  # The possible_event didn't clash with any event in calendar:



def find_possibilities(personal_calendar, event_calendar):
  """Return a subset of events from the event calendars which don't clash with
  any events in the personal calendar.
  
  You can assume that calendars will always be sorted according to
  event.start_timestamp"""
  
  possible = []

  # --[ WRITE CODE HERE ]-->
  # Collect all events from the event_calendar that don't clash
  # with any events in the personal_calendar.
  # <--[ WRITE CODE HERE ]--
  
  if len(personal_calendar) == 0 or personal_calendar == None:
    return list(event_calendar)
  
  elif len(event_calendar) == 0 or event_calendar == None:
    possible1 = []
    return possible1
  
  else:
    for event in event_calendar:
      if not clashes_with(event, personal_calendar) == True:
	counter.increment()
	counter.increment()
	counter.increment()
	possible.append(event)
    return possible


# The command line interface. Do not modify!
if __name__ == "__main__":
  if len(sys.argv) < 2:
    print >> sys.stderr, "You must provide at least two calendars as arguments!"
  else:
    calendars = []

    # Load all calendars as specified by the command line:
    for path in sys.argv[1:]:
      calendars.append(eventlib.load_file(path))

    # The first calendar is the personal calendar:
    personal_calendar = calendars[0]

    # The remaining calendars are the event calendars:
    event_calendars = calendars[1:]

    # Find all possible events which don't clash with events in the personal
    # calendar:
    start = time.clock()
    possible = []
    for event_calendar in event_calendars:
      possible += find_possibilities(personal_calendar, event_calendar)
    end = time.clock()

    # Print out the time, number of comparisons to stderr:
    print >> sys.stderr, end - start
    print >> sys.stderr, counter.count

    # Print out the list of possibilities to stdout:
    eventlib.save(sys.stdout, possible)
