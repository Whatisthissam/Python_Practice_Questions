principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (in %): ")) / 100
time = float(input("Enter time period (in years): "))
n = float(input("Enter number of times interest is compounded per year: "))

amount = principal * (1 + rate / n) ** (n * time)
compound_interest = amount - principal

# Print the result
print(f"The compound interest is: {compound_interest}")
