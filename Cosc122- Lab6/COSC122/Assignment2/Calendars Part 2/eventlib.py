
from datetime import datetime
import json, sys, time

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


class Event(object):
  def __init__(self, attributes):
    self.attributes = attributes
    self.start_timestamp = datetime.strptime(self.attributes['start_timestamp'], TIMESTAMP_FORMAT)
    self.end_timestamp = datetime.strptime(self.attributes['end_timestamp'], TIMESTAMP_FORMAT)
    self.name = self.attributes.get('name')


  def __repr__(self):
    return '<Event' + repr((id(self), self.start_timestamp.strftime(TIMESTAMP_FORMAT), self.end_timestamp.strftime(TIMESTAMP_FORMAT), self.name,)) + '>'


  def clashes_with(self, other_event):
    return self.intersects(other_event) or other_event.intersects(self)


  def intersects(self, other_event):
    return self.includes(other_event.start_timestamp) or self.includes(other_event.end_timestamp)


  def is_before(self, other_event):
    return self.start_timestamp < other_event.start_timestamp


  def includes(self, timestamp):
    return timestamp >= self.start_timestamp and timestamp < self.end_timestamp


  def __le__(self, other):
    return self.start_timestamp <= other.start_timestamp


  def __lt__(self, other):
    return self.start_timestamp < other.start_timestamp


  def __ge__(self, other):
    return self.start_timestamp >= other.start_timestamp


  def __gt__(self, other):
    return self.start_timestamp > other.start_timestamp


  def __eq__(self, other):
    return self.attributes == other.attributes


def load(io, klass = Event):
  """Read events from an input io"""
  events = []
  for line in io:
    attributes = json.loads(line)

    event = klass(attributes)

    events.append(event)
  return events


def save(io, events):
  """Save events to an output io"""
  for event in events:
    attributes_string = json.dumps(event.attributes)

    io.write(attributes_string)
    io.write('\n')


def load_file(path, klass = Event):
  """Read events from a file given by path"""
  return load(open(path), klass)


def save_file(path, events):
  """Write events to a file given by path"""
  save(open(path, "w"), events)


def check_events_are_sequential(events):
  events.sort(key=lambda x: x.start_timestamp)
  
  previous = None
  for event in events:
    if previous:
      if previous.end_timestamp > event.start_timestamp:
        print "Event", previous, "overlaps with", event
        return False
    previous = event
  
  return True
