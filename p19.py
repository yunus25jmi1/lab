# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year
source_file_path = "cat.jpg"  
destination_file_path = "dog.jpg" 
try:
    with open(source_file_path, 'rb') as source_file:
        image_content = source_file.read()
        with open(destination_file_path, 'wb') as destination_file:
            destination_file.write(image_content)
    print(f"Image file copied successfully from {source_file_path} to {destination_file_path}")
except FileNotFoundError:
    print(f"File not found: {source_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
