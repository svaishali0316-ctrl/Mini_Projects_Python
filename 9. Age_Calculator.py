# Age_Calculator

from datetime import date

def Age_Calculator(birthdate):
    today=date.today()
    age=today.year-birthdate.year
    
    if(today.month, today.day)<(birthdate.month, birthdate.day):
     age=age-1
    return age

print(Age_Calculator(date(2002,5,8)),"years")
