# Temperature_Converter

print("="*30)
print("        TEMPERATURE CONVERTER")
print("="*30)

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice=int(input("Enter your choice: "))
temp=float(input("Enter your temperature: "))

if choice==1:
    Result=(temp*9/5)+32
    print("Temperature= ",Result,"Fahrenheit")
elif choice==2:
    Result=(temp-32)*5/9
    print("Temperature= ",Result,"Celsius")
else:
    print("Invalid Choice")
    
