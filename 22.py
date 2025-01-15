numbers = [1, 2, 3, 4, 5]

start = 0
end = len(numbers) - 1

while start < end:
    numbers[start], numbers[end] = numbers[end], numbers[start]
    start += 1
    end -= 1

print(f"The reversed list is: {numbers}")
