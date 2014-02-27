#!/usr/bin/env python

import eventlib, sys, time, comparelib

counter = comparelib.Counter()


def clashes_with(possible_event, calendar):
  """Return true if the possible_event clashes with any event in the calendar.
  
  Use a linear scan to check each event in the calendar. You may break early 
  if you hit the case where possible_event.end_timestamp is less than
  event.start_timestamp, as it is no longer possible to encounter any clashing 
  events.
  """

  for event in calendar:
    counter.increment()
    if event.clashes_with(possible_event)==True:
      return True
    if possible_event.end_timestamp < event.start_timestamp:
      return False
    
  
  # --[ WRITE CODE HERE ]-->
  # Implement the linear scan.
  # You can check for clashes using event.clashes_with(other_event) which 
  # returns true of the events overlap.
  # Don't forget to call counter.increment() for every call to 
  # Event.clashes_with.
  # <--[ WRITE CODE HERE ]--




def find_possibilities(personal_calendar, event_calendar):
  """Return a subset of events from the event calendars which don't clash with
  any events in the personal calendar.
  
  You can assume that calendars will always be sorted according to
  event.start_timestamp"""
  
  possible = []
  
  for event in event_calendar:
    if clashes_with(event, personal_calendar)!=True:
      possible.append(event)
  
  
  return possible


  # --[ WRITE CODE HERE ]-->
  # Collect all events from the event_calendar that don't clash
  # with any events in the personal_calendar.
  # <--[ WRITE CODE HERE ]--


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
