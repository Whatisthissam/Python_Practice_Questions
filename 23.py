numbers = [1, 2, 3, 4, 3, 5, 3]

target = int(input("Enter a number to count: "))

count = 0
for num in numbers:
    if num == target:
        count += 1

print(f"The number {target} appears {count} times in the list.")
