class Stack:
  """
  An object for creating a stack and it's associated methods for basic stack manipulation operaion
  """

  def __init__(self):
    self.items = [];

  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) - 1]
  
  def size(self):
    return len(self.items)

