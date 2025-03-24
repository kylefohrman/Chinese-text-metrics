# AnkiDeckExtractor.py
# 2024 www.fohrman.org

from pathlib import Path
from time import sleep
import re
from lib.chinese_metrics import chineseMetrics

print("--------------------------------------")
print("| ANKI CHARACTER COUNTER FOR CHINESE |")
print("--------------------------------------")
print("2024 www.fohrman.org")
print()
print()
print("This program will take a Chinese Anki deck exported to .txt and extract metrics on the unique characters. If the file you are uploading is not an Anki deck, please use chinese_text_metrics.py instead.")
print()
print("To extract an anki deck from desktop:")
print("- Open Anki desktop client")
print("- Select your deck's settings -> Export -> Notes in Plain Text (.txt) -> Uncheck all boxes")
print()
print("Please select below:")

pathYes = ['y', 'Y', "Yes", "yes"]
pathNo = ['n', 'N', "No", "no"]
lines = []
words = []
wordsReg = []

while True:
    pathType = input("Is your .txt file in this program's root folder? (y/n) ")
    try:
        if pathType in pathYes:
            filename = input("Please enter the filename (with extension): ")
            filepath = Path(__file__).with_name(filename)
            break
        elif pathType in pathNo:
            filepath = Path(input("Please enter the full file path: "))
            filename = filepath.name
            break
        else:
            print("Invalid selection.")
    except ValueError as e:
        input(f"Invalid selection with error: \"{e}\"")
        raise ValueError

print("Opening file...")
try:
    with open(filepath, encoding="utf8") as f:
        lines = f.readlines()
except Exception as e:
    print("Error when loading file at path {}, {}".format(str(filepath), e))
    input("Press Enter to exit...")
    exit(1)
print("File opened successfully.", end = "")
for i in range(0, 30):
    print(".", end = "")
print(len(lines), "lines in file.")
print()

print("The following should be the first card from your deck:")
print()
splitLine = lines[3].split("\t")
segmentCount = 0
for segment in splitLine:
    print(f"| {segment} ", end="")
print("|")
simplifiedMarker = input("Which number item ")
if simplifiedMarker == "":
    simplifiedMarker = "[Simplified]"
simplifiedMarker += "\n"
prev = False
for line in lines:
    if prev == True:
        prev = False
        words.append(line)
        wordsReg.append(re.sub(r'[a-zA-Z0-9]', '', line))
    if line == simplifiedMarker:
        prev = True
print("Words extracted.", end="")
for i in range(0, 30):
    print(".", end = "")
print(len(words), "total words.")
print()

filename = filename.split(".")[0]

filepath = Path(__file__).parent / "output" / (str(filename) + "AnkiWords.txt")
try:
    with open(filepath, "w", encoding="utf8") as f:
        f.writelines(wordsReg)
    print("Output full word list to",filepath)
except Exception as e:
    print("Error trying to write to word list: ", e)

chineseMetrics(words, filename)


input("Press Enter to exit...")
