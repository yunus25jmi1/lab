# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year

# Input the height of the equilateral triangle
height = int(input("Enter the height of the equilateral triangle: "))

# Loop through each row
for i in range(1, height + 1):
    # Print spaces for alignment
    for j in range(height - i):
        print(" ", end="")
    
    # Print stars for the current row
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Move to the next line for the next row
    print()
