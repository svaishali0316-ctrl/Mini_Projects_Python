# PDF2Image_Converter

from pdf2image import convert_from_path

print("="* 30)
print("   PDF TO IMAGE CONVERTER    ")
print("="* 30)

pdf_path = input("Enter PDF file path: ")

try:
    pages = convert_from_path(pdf_path)

    for i, page in enumerate(pages):
        image_name = f"page_{i + 1}.png"
        page.save(image_name, "PNG")
        print("Image saved:", image_name)

    print("Conversion completed!")

except Exception as e:
    print("Error:", e)


    
