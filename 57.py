file_name = input("Enter the file name to modify: ")
find_word = input("Enter the word to find: ")
replace_word = input("Enter the word to replace with: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
    
    new_content = content.replace(find_word, replace_word)
    
    with open(file_name, 'w') as file:
        file.write(new_content)
    
    print(f"'{find_word}' has been replaced with '{replace_word}' in {file_name}.")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
