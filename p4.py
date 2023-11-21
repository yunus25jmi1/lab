# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year

# To get Input from the user.
m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))

# Ensure that m is less than or equal to n
if m > n:
    print("Invalid input: m should be less than or equal to n.")
else:
    print(f"Even numbers between {m} and {n}:")
    
    # Loop through the range from m to n (inclusive)
    for num in range(m, n + 1):
        # Check if the number is even
        if num % 2 == 0:
            print(num)
