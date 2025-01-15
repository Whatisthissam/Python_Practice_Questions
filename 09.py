principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (in %): "))
time = float(input("Enter time period (in years): "))

interest = (principal * rate * time) / 100

print(f"The simple interest is: {interest}")
