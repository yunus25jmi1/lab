# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year
file_path = "test.txt"
try:
    with open(file_path, 'a') as file:
        data_to_append = "This is the new data that will be appended to the file.\n"
        file.write(data_to_append)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("Contents of the file after appending:")
        print(content)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
