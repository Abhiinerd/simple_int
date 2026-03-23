principal = float(input("Enter principal amount: "))
rate = float(input("Enter Rate Amount (in %): "))
time = float(input("Enter Time (in years): "))
num_time_int = int(input("Enter number of times interest compounded per year: "))

rate = rate / 100

# Total Amount
amount = principal * (1 + rate / num_time_int) ** (num_time_int * time)

# Compound Interest
compound_interest = amount - principal

print("Compound Interest = ₹", compound_interest)
print("Total Amount Payable = ₹", amount)