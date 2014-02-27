
class Counter(object):
  """A simple counter object that can be incremented."""
  def __init__(self):
    self.count = 0
  
  def increment(self, count = 1):
    """Increment the count."""
    self.count += count
  
  def reset(self):
    """Reset the count back to 0."""
    self.count = 0
  
  def __repr__(self):
    return repr(self.count)
