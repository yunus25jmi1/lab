# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year

# Define a dictionary to map digits to words
digit_words = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}

# Input numeric digits from the user
num_str = input("Enter a number: ")

# Convert each digit to its word representation
words = []
for digit in num_str:
    if digit in digit_words:
        words.append(digit_words[digit])
    else:
        words.append('Invalid input')

# Display the numeric digits in words
print(' '.join(words))
