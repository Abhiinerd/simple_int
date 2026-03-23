principal = float(input("Enter principal amount: "))
rate = float(input("Enter Rate Amount (in %): "))
time = float(input("Enter Time (in years): "))

rate = rate / 100  # convert to decimal

Simple_int = principal * rate * time
Amount_payable = principal + Simple_int

print("Simple Interest = ₹", Simple_int)
print("Amount Payable = ₹", Amount_payable)