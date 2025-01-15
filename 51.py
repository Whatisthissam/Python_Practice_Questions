file_name = input("Enter the file name to read: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
