numbers = [1, 2, 3, 3, 4, 5, 5, 6]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(f"List without duplicates: {unique_numbers}")
