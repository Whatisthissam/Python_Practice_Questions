string = input("Enter a string: ")
substring = input("Enter a substring: ")

if substring in string:
    print(f"The substring '{substring}' is present in the string.")
else:
    print(f"The substring '{substring}' is not present in the string.")
