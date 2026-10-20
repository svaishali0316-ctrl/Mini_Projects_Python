# ImagetoPDF_Converter

from PIL import Image

print("=" * 30)
print(" IMG TO PDF CONVERTER     ")
print("=" * 30)

image_path = "photo.jpg"
pdf_path = "photo.pdf"

image=Image.open(image_path)

def ImgToPdf():
    if image.mode in ("RGBA", "P"):
        image=image.convert("RGB")
    else:
         print("PDF created:", pdf_path)


def ImgToPdf():
