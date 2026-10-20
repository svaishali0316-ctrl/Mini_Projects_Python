# SI__Calculator

print("="*30)
print("          SIMPLE INTEREST CALCULATOR         ")
print("="*30)

p=float(input("Enter the principle amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time in years: "))

SI=p*r*t

print("Simple Interest= ",SI)
print("Total Amount= ",p+SI)
