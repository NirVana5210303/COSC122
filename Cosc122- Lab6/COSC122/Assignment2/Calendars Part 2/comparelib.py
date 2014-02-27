
class Counter(object):
  def __init__(self):
    self.count = 0
  
  def increment(self, count = 1):
    self.count += count
  
  def reset(self):
    self.count = 0
  
  def __repr__(self):
    return repr(self.count)

def count_comparisons(key, counter):
  class K(object):
    def __init__(self, obj):
      self.obj = obj
    def __lt__(self, other):
      counter.increment(); return key(self.obj) < key(other.obj)
    def __gt__(self, other):
      counter.increment(); return key(self.obj) > key(other.obj)
    def __eq__(self, other):
      counter.increment(); return key(self.obj) == key(other.obj)
    def __le__(self, other):
      counter.increment(); return key(self.obj) <= key(other.obj)
    def __ge__(self, other):
      counter.increment(); return key(self.obj) >= key(other.obj)
    def __ne__(self, other):
      counter.increment(); return key(self.obj) != key(other.obj)
  
  return K

def by_start_timestamp(counter):
  return count_comparisons(lambda x : x[0].start_timestamp, counter)
