from googletrans import Translator
from googletrans import LANGUAGES

trans = Translator()

for lang in LANGUAGES:
    print(f'{lang}={LANGUAGES[lang]}')

print("-----------------------------------------------------------------------------------------------------------------------------------------")

print("Above are the codes of different languages you can translate your text into")

string = str(input("Enter the statement to be translated: "))

src = str(input("Enter the original language code: "))

dest = str(input("Enter the language code you want the statement to be translated into: "))

t = trans.translate(string, dest, src)

print(f'Source: {t.src}')
print(f'Destination: {t.dest}')
print(f'{t.origin} -> {t.text}')
print()
