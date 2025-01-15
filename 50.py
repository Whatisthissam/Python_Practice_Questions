def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Ask the user for two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate the LCM
result = lcm(a, b)

# Print the result
print(f"The LCM of {a} and {b} is: {result}")
