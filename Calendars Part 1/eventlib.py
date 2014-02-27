
from datetime import datetime
import json, sys, time

"""The time format used in the JSON encoding."""
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

class Event(object):
  """An event with a start_timestamp and end_timestamp and associated 
  attributes."""
  
  def __init__(self, attributes):
    self.attributes = attributes
    self.start_timestamp = datetime.strptime(self.attributes['start_timestamp'], TIMESTAMP_FORMAT)
    self.end_timestamp = datetime.strptime(self.attributes['end_timestamp'], TIMESTAMP_FORMAT)
    self.name = self.attributes.get('name')


  def __repr__(self):
    return '<Event' + repr((id(self), self.start_timestamp.strftime(TIMESTAMP_FORMAT), self.end_timestamp.strftime(TIMESTAMP_FORMAT), self.name,)) + '>'


  def clashes_with(self, other_event):
    """Returns true if the event overlaps with the given other_event."""
    return self.intersects(other_event) or other_event.intersects(self)


  def intersects(self, other_event):
    """Returns true if this event includes in its time span, the other events 
    start or end timestamp"""
    return self.includes(other_event.start_timestamp) or self.includes(other_event.end_timestamp)


  def is_before(self, other_event):
    """Returns true if this event starts before the given other event."""
    return self.start_timestamp < other_event.start_timestamp


  def includes(self, timestamp):
    """Returns true if the given timestamp falls in between the event's time 
    span."""
    return timestamp >= self.start_timestamp and timestamp < self.end_timestamp


  def __eq__(self, other):
    """Returns true if these events appear to be the same."""
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

