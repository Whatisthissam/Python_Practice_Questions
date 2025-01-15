n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = [0, 1]

for i in range(2, n):
    fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

print(f"The first {n} Fibonacci numbers are: {fib_sequence}")
