number = input("Enter a number: ")

sum_digits = 0

for digit in number:
    sum_digits += int(digit)

print(f"The sum of the digits is: {sum_digits}")
