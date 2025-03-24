# chinese_metrics.py
# Kyle Fohrman 2024 www.fohrman.org

from collections import Counter
from pathlib import Path
import re
import unicodedata
import hanzidentifier

def strip_accents(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def chineseMetrics(lines, filename):
    print("Beginning analysis (this may take a while)...")
    smush = ""
    for char in lines:
        smush += char

    smush = strip_accents(smush)

    punc = "！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
    punc += "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    chars = re.findall(r'[a-zA-Z]*', smush, re.M)
    chars = list(filter(None, chars))
    digits = re.findall(r'[0-9]*', smush, re.M)
    digits = list(filter(None, digits))
    newline = re.findall(r'(\n|\r\n|\r)', smush, re.M)
    whitespace = re.findall(r'\s', smush, re.M)
    puncList = re.findall(r'[%s]' %punc, smush, re.M)

    smush = re.sub(r'[a-zA-Z0-9\s%s]' %punc, '', smush)

    charSeparator = input("Remove traditional characters? y/n: ")
    if charSeparator.lower() == "y":
        i = 0
        while i < len(smush):
            if hanzidentifier.identify(smush[i]) is hanzidentifier.TRADITIONAL:
                smush = smush[:i] + smush[i+1:]
            else:
                i += 1

    junkFile = False
    junk = []
    for char in chars:
        junk.append(char + '\n')
    for digit in digits:
        junk.append(digit + '\n')
    if len(junk) > 0:
        junkFile = True
        for mark in Counter(puncList).most_common():
             junk.append(str(mark) + "\n")
        for white in Counter(whitespace).most_common():
            junk.append(str(white) + "\n")
    
    count = Counter(smush).most_common()
    
    output = []
    for line in count:
        output.append(line[0] + ": " + str(line[1]) + "\n")

    outputName = filename + "Metrics.txt"
    filepath = Path(__file__).parents[1] / "output" / outputName
    try:
        with open(filepath, "w", encoding="utf8") as f:
            f.writelines(output)
        print("Output character frequency list to", filepath)
    except Exception as e:
            print("Exception while writing output file:", e)
    print("Chinese metrics:")
    print("    - " + str(len(output)) + " unique Chinese characters")
    print()
    print("Other metrics:")
    print("    - " + str(len(''.join(chars))) + " English characters detected (" + str(len(chars)) + " words)")
    print("    - " + str(len(''.join(digits))) + " digits detected (" + str(len(digits)) + " numbers)")
    print("    - " + str(len(puncList)) + " punctuation characters")
    print("    - " + str(len(newline)) + " newline characters")
    print("    - " + str(len(whitespace) - len(newline)) + " other whitespace characters")

    if junkFile:
        junkName = filename + "Junk.txt"
        filepath = Path(__file__).parents[1] / "output" / junkName
        try:
            with open(filepath, "w", encoding="utf8") as f:
                f.writelines(junk)
            print("Junk characters output to", filepath)
        except Exception as e:
            print("Exception while writing to junk character file: ", e)
    else:
        print("No English or numeric characters detected, so junk file was not created.")
