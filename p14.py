# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year
def print_list_in_reverse(list1):
  """Prints the elements of a list in reverse order.
  Args:
    list1: The list whose elements are to be printed in reverse order.
  """
  for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
list1 = [1, 2, 3, 4, 5]
print_list_in_reverse(list1)
