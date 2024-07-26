def is_palindrome(s):
  """Checks if a string is a palindrome.
  
  Args:
    s: The string to check.
  
  Returns:
    True if the string is a palindrome, False otherwise.
  """
  return s == s[::-1]

string = input("Enter a string: ")

if is_palindrome(string):
  print(f"{string} is a palindrome.")
else:
  print(f"{string} is not a palindrome.")
  print("so its wrong")
  