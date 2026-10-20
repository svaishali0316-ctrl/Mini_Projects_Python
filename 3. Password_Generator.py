# Password_Generator

import random

print("="*25)
print("     PASSWORD GENERATOR")
print("="*25)

def Password_Generator():
    length=int(input("Enter the password length: "))
    password= ""
    for i in range(length):
        password+=random.choice("Vaish@123")
    print("password: ",password)



Password_Generator()
