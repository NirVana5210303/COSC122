#!/usr/bin/env python

import unittest, clashes_binary, eventlib

event1 = eventlib.Event({
  'start_timestamp': '2012-01-01 14:00:00',
  'end_timestamp': '2012-01-01 16:00:00',
  'name': 'Test1'
})

event2 = eventlib.Event({
  'start_timestamp': '2011-01-01 12:00:00',
  'end_timestamp': '2012-02-01 12:00:00',
  'name': 'Test2'
})

event3 = eventlib.Event({
  'start_timestamp': '2013-01-01 14:00:00',
  'end_timestamp': '2013-01-01 16:00:00',
  'name': 'Test3'
})

class TestEventsBinary(unittest.TestCase):
  def test_clashes_with(self):
    'Ensure that if events intersect that clashes are reported'
    
    self.assertFalse(clashes_binary.clashes_with(event1, []))
    self.assertFalse(clashes_binary.clashes_with(event1, [event3]))

    self.assertTrue(clashes_binary.clashes_with(event1, [event2, event3]))
    self.assertTrue(clashes_binary.clashes_with(event1, [event1]))
    self.assertTrue(clashes_binary.clashes_with(event1, [event1, event1, event1]))


  def test_bisection(self):
    'Ensure that the bisection algorithm is working correctly'
    
    event_calendar = eventlib.load_file('data/events_b.txt')
    
    for i in xrange(len(event_calendar)):
      offset = clashes_binary.bisect_left(event_calendar, event_calendar[i].start_timestamp)
      self.assertEqual(offset, i)

  def test_find_possibilities(self):
    'Ensure that events are listed if they do not clash with the personal calendar'
    
    personal_calendar = [event1]
    event_calendar = [event1, event2, event3]
    event_calendar.sort(key=lambda x : x.start_timestamp)
    
    self.assertEqual(clashes_binary.find_possibilities([], event_calendar), event_calendar)
    self.assertEqual(clashes_binary.find_possibilities(event_calendar, []), [])
    self.assertEqual(clashes_binary.find_possibilities(personal_calendar, event_calendar), [event3])


  def test_efficiency(self):
    'Ensure that linear search number of comparisons is correct.'
    
    personal_calendar = eventlib.load_file('data/calendar.txt')
    event_calendar = eventlib.load_file('data/events_a.txt')
    results = eventlib.load_file('data/results_a.txt')
      
    clashes_binary.counter.reset()
    self.assertEqual(clashes_binary.find_possibilities(personal_calendar, event_calendar), results)
    self.assertEqual(clashes_binary.counter.count, 820)


if __name__ == '__main__':
  unittest.main(exit=False)
