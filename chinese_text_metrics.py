# ChineseTextMetrics.py
# 2024 www.fohrman.org

from pathlib import Path
from time import sleep
import re
from lib.chinese_metrics import chineseMetrics

print("------------------------------")
print("| CHINESE TEXT ANALYSIS TOOL |")
print("------------------------------")
print("2024 www.fohrman.org")
print()
print()
print("This program will extract Chinese language data from a given text file.")
print()
print("Please select below:")

pathYes = ['y', 'Y', "Yes", "yes"]
pathNo = ['n', 'N', "No", "no"]
lines = []

while True:
    pathType = input("Is your .txt file in this program's root folder? (y/n) ")
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

filename = filename.split(".")[0]

chineseMetrics(lines, filename)

input("Press Enter to exit...")