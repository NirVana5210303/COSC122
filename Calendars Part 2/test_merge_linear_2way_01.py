#!/usr/bin/env python

import unittest, merge_linear_2way, eventlib

event1 = eventlib.Event({
  'start_timestamp': '2012-01-01 14:00:00',
  'end_timestamp': '2012-01-01 16:00:00',
  'name': 'Test1'
})

event1a = eventlib.Event({
  'start_timestamp': '2012-01-01 14:00:00',
  'end_timestamp': '2012-01-01 16:00:00',
  'name': 'Test1a'
})

event2 = eventlib.Event({
  'start_timestamp': '2012-02-01 14:00:00',
  'end_timestamp': '2012-02-01 16:00:00',
  'name': 'Test2'
})

event3 = eventlib.Event({
  'start_timestamp': '2012-03-01 14:00:00',
  'end_timestamp': '2012-03-01 16:00:00',
  'name': 'Test3'
})

event4 = eventlib.Event({
  'start_timestamp': '2012-04-01 14:00:00',
  'end_timestamp': '2012-04-01 16:00:00',
  'name': 'Test4'
})


class TestMergeLinear2Way(unittest.TestCase):
  def test_merge_events(self):
    'Ensure that events are merged correctly'
    
    c0 = [event1, event2]
    c1 = [event3, event4]
    merged = [event1, event2, event3, event4]
    self.assertEqual(merge_linear_2way.merge_events(c0, c1), merged)
    self.assertEqual(merge_linear_2way.merge_events(c1, c0), merged)


  def test_merge_events_same_start_timestamp(self):
    'Ensure that events are merged correctly even if events have the same start_timestamp'
    
    c0 = [event1, event2]
    c1 = [event1a, event3, event4]
    merged = [event1, event1a, event2, event3, event4]
    self.assertEqual(merge_linear_2way.merge_events(c0, c1), merged)

    c0 = [event1a, event2, event3]
    c1 = [event1, event2, event4]
    merged = [event1a, event1, event2, event2, event3, event4]
    self.assertEqual(merge_linear_2way.merge_events(c0, c1), merged)


  def test_efficiency(self):
    'Ensure that number of comparisons is correct.'
    
    events_a = eventlib.load_file('data/events_a.txt')
    events_b = eventlib.load_file('data/events_b.txt')
    events_c = eventlib.load_file('data/events_c.txt')
    merged = eventlib.load_file('data/merged_abc.txt')
    
    merge_linear_2way.counter.reset()
    self.assertEqual(merge_linear_2way.merge_calendars([events_a, events_b, events_c]), merged)
    self.assertEqual(merge_linear_2way.counter.count, 479)


if __name__ == '__main__':
  unittest.main(exit=False)
