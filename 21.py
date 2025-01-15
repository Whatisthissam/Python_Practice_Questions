numbers = [5, 3, 8, 1, 9]

min_val = numbers[0]
max_val = numbers[0]

for num in numbers:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print(f"The minimum value is: {min_val}")
print(f"The maximum value is: {max_val}")
