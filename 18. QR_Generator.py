# QR_Generato

import qrcode

print("=" * 30)
print("    QR CODE GENERATOR     ")
print("=" * 30)

data=input("Enter text or website URL: ")

qr=qrcode.make(data)

qr.save("hell0_qr.png")

print("QR Code generated successfully!")
print("Saved as hello_qr.png")
