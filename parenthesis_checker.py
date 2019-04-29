from stack import Stack

def par_checker(symbol_str):
  """
  Checks if a group of parenthesis are balanced
  Returns True if so and False otherwise
  """

  s = Stack()
  balanced = True
  index = 0

  while index < len(symbol_str) and balanced:
    symbol = symbol_str[index]
    if symbol in '(':
      s.push(symbol)
    else:
      if s.is_empty():
        balanced = False
      else: 
        s.pop()

    index += 1

  if balanced and s.is_empty():
    return True
  else:
    return False
