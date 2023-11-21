# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year
import csv
data = [
    ['Name', 'Age', 'Department'],
    ['Md Yunus', 18, 'CEO'],
    ['John Doe', 30, 'Sales'],
    ['Jane Smith', 35, 'Marketing'],
    ['Bob Brown', 25, 'HR']
]
with open('test.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("Data written to CSV file successfully.")
with open('test.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
