class Queue:
  """
  An object for creating a queue and it's associated methods for basic stack manipulation operaion
  """

  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)
