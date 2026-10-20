#  BMI_Calculater

name = input("Enter your name: ")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

print("Name:", name)
print("Your BMI is:", round(bmi, 2))

if bmi < 20.2:
    print("Category: Underweight")
elif bmi < 30:
    print("Category: Normal weight")
elif bmi < 40:
    print("Category: Overweight")
else:
    print("Category: Obese")
