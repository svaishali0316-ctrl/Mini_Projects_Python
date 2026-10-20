# Currency_Converter

print("Currency Convertor")
print("1. INR to EUR")
print("2. INR to USD")
print("3. INR to CAD")

rates={"EUR": 90, "USD": 120, "CAD": 105}


amount=float(input("Enter a amount in INR: "))
currency=input("Choose a currency(EUR/USD/CAD): ").upper()
converted=amount/rates[currency]

def Currency_Convertor():
    if(currency not in rates):
         print("Invalid currency. Choose EUR,USD,CAD.")
    else:
        print(f"{amount:.2f} INR = {converted:.2f} {currency}")
        

Currency_Convertor()
