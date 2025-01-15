import json

file_name = input("Enter the JSON file name: ")

try:
    with open(file_name, 'r') as file:
        data = json.load(file)
    
    key_to_modify = input("Enter the key to modify: ")
    if key_to_modify in data:
        new_value = input(f"Enter the new value for {key_to_modify}: ")
        data[key_to_modify] = new_value
    else:
        print(f"Key '{key_to_modify}' not found in the JSON data.")
    
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Data has been updated in {file_name}.")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except json.JSONDecodeError:
    print(f"Error: The file '{file_name}' is not a valid JSON file.")
