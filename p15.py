# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year

def print_string_in_forward_and_reverse_order_using_for_loop(string1):
  """Prints the elements of a string in forward and reverse order using for loop.
  Args:
    string1: The string whose elements are to be printed in forward and reverse order.
  """
  print("Forward order:")
  for i in range(len(string1)):
    print(string1[i])
  print("Reverse order:")
  for i in range(len(string1) - 1, -1, -1):
    print(string1[i])
string1 = "Hello, world!"
print_string_in_forward_and_reverse_order_using_for_loop(string1)
