from deque import Deque

def palindrome_checker(str):
  """
  Checks if a word is palindrome. Returns True if it is.
  Returns False if not.
  Uses the deque abstract data type
  """

  d = Deque()

  for char in str:
    d.add_rear(char)

  stillPalindrome = True

  while d.size() > 1 and stillPalindrome:
    first = d.remove_front()
    last = d.remove_rear()

    if first != last:
      stillPalindrome = False

  return stillPalindrome
