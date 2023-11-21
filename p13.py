# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year
def factorial(n):
  """Calculates the factorial of a given number.
  Args:
    n: The number whose factorial is to be calculated.
  Returns:
    The factorial of n.
  """
  if n < 0:
    raise ValueError("Factorial of negative numbers is not defined.")
  elif n == 0:
    return 1
  else:
    factorial = 1
    for i in range(1, n + 1):
      factorial *= i
    return factorial
