original_dict = {'a': 1, 'b': 2, 'c': 3}

inverted_dict = {value: key for key, value in original_dict.items()}

print(f"Inverted dictionary: {inverted_dict}")
