# Project 1: Calculator

print("="*30)
print("        CALCULATOR")
print("="*30)

a=int(input("Enter the number: "))
oper=input("Enter the operator(+,-,*,/): ")
b=int(input("Enter the number: "))

if oper =="+":
     print("Total= ",a+b)
elif oper =="-":
    print("Total= ",a-b)
elif oper =="*":
    print("Total= ",a*b)
elif oper =="/":
    print("Total= ",a/b)
else:
    print("Invalid Operator")
          
