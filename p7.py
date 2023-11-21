# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year

# Input the number of terms for the Fibonacci series
n = int(input("Enter the number of Fibonacci terms to generate: "))

# Initialize the first two terms
first_term = 0
second_term = 1

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series up to 1 term:")
    print(first_term)
else:
    # Print the first two terms
    print("Fibonacci series:")
    print(first_term)
    print(second_term)

    # Generate and print the remaining terms
    for i in range(2, n):
        next_term = first_term + second_term
        print(next_term)
        # Update the first and second terms for the next iteration
        first_term, second_term = second_term, next_term
