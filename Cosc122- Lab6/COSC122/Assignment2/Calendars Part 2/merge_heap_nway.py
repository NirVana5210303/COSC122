#!/usr/bin/env python

import eventlib, comparelib, sys, time, json

counter = comparelib.Counter()

def siftdown(heap, pos):
  """The child indices of heap index pos are already heaps, transform the heap 
  so that we have at index pos too. The heap items are tuples or lists where 0th
  item will be used for ordering.
  """

  # --[ WRITE CODE HERE ]-->
  while (pos * 2) + 1 <= len(heap) - 1:
    newitem = heap[pos]
    childpos = 2 * pos + 1    # leftmost child position
    right_pos = childpos + 1  # rightmost child position
    
  # Repeatedly move the item heap[pos] down the tree by swapping with the
  # smallest child to restore the heap invariant.
  # <--[ WRITE CODE HERE ]--
    if right_pos <= len(heap) - 1:
      counter.increment()
      if heap[right_pos][0] < heap[childpos][0]:
        childpos = right_pos
    counter.increment()
    if newitem[0] > heap[childpos][0]:
      heap[pos], heap[childpos] = heap[childpos], newitem
      pos = childpos
    else:
      break
      
def heapify(x):
  """Transform list into a heap, in-place, in O(|x|) time. The heap items are
  tuples or lists where 0th item will be used for ordering."""
  # --[ WRITE CODE HERE ]-->
  # Turn the list x into a min-heap using the in-place heapify algorithm.
  num_sum = len(x)
  for i in reversed(range(num_sum // 2)):
    siftdown(x, i)
  # <--[ WRITE CODE HERE ]--


def merge_calendars(calendars):
  """Use a heap to merge the calendars by selecting the smallest event
  repeatedly"""
  
  merged = []
  
  # --[ WRITE CODE HERE ]-->
  # Initialise the heap with lists containing the event in the 0th position.

  heap = []
  
  # Prime the top of the merge:
  for calendar in calendars:
    heap.append([calendar[0], 0, calendar])
  heapify(heap)
  while len(heap) != 0:
    event = heap[0][0]
    index = heap[0][1]
    cal = heap[0][2]
    
    merged.append(event)
    next_index = index + 1
    if next_index > len(cal) - 1:
      last_item = heap.pop()
      if len(heap) > 0:  # for check whather the heap is empty or not if the heap is empty
        heap[0] = last_item
        siftdown(heap, 0)
    else:
      next_event = cal[next_index]
      heap[0][1] = next_index
      heap[0][0] = next_event
      siftdown(heap, 0)
    
    
    
  # Firstly you need to heapify the items in heap.
  
  # While the heap isn't empty, take the top item and append it to merged.
  # Increment the offset by 1 and update the heap item. Then, reposition the
  # item in the heap by calling siftdown.
  # <--[ WRITE CODE HERE ]--
  
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
