# Unit_Converter

print("="*30)
print("     UNIT CONVERTER")
print("="*30)

print("1. Kilometers to Meters")
print("2. Meters to Kilometers")
print("3. Kilograms to Grams")
print("4. Grams to Kilograms")

Choice=int(input("Enter your option: "))
Value=float(input("Enter your value: "))

if Choice==1:
    print("Result= ",Value*1000,"meters")
elif Choice==2:
    print("Result= ",Value/1000,"kilometers")
elif Choice==3:
    print("Result= ",Value*1000,"grams")
elif Choice==4:
    print("Result= ",Value/1000,"kilograms")
else:
    print("Invalid Option")
    
    

