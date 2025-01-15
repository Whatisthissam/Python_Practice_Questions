def convert_to_int(input_str):
    try:
        return int(input_str)
    except ValueError:
        print("Error: The input is not a valid integer.")

user_input = input("Enter a number: ")
convert_to_int(user_input)
