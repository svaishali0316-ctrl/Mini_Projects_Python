#  CI_Calculator

print("="*30)
print("       COMPOUND INTEREST CALCULATOR        ")
print("="*30)

p=float(input("Enter the principal of amount= "))
r=float(input("Enter the rate of interest= "))
t=float(input("enter the amount in years= "))

amount=p*(1+r/100)*t
CI=amount-p

print("Compound Interest= ",CI)
print("Total Amount= ",amount)

