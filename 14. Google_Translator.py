# Google_Translator

from deep_translator import GoogleTranslator

print("="*30)
print("             TRANSLATOR           ")
print("="*30)

text=input("Enter the text: ")

translated=GoogleTranslator(source="en",target="ta").translate(text)

print("Tamil Translation: ")
