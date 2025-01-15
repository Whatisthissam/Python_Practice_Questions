file_name = input("Enter the file name to count lines: ")

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(f"The file has {len(lines)} lines.")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
