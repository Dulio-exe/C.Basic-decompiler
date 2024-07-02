import os
import re

def main():
    fileName = input("Enter file name (G1M): ")
    final = ""
    name = ""
    try:
        with open(fileName, 'rb') as f:
            i = 0
            byte = f.read(1)
            while byte != b"":
                i += 1
                if 61 <= i <= 68:
                    name += identify_byte_to_string(byte)
                if i > 86:
                    final += identify_byte_to_string(byte)
                byte = f.read(1)
    except FileNotFoundError:
        print("Invalid file!")
        return

    with open(decomp(name) + ".txt", "w") as output_file:
        output_file.write(decomp(final))

def identify_byte_to_string(sym):
    return "[U+" + "".join(f"{i:02X}" for i in sym) + "]"

def decomp(code):
    replacements = {
        "[U+20]": " ",
        "[U+21]": "!",
        "[U+22]": "\"",
        "[U+23]": "#",
        "[U+24]": "$",
        "[U+25]": "%",
        "[U+26]": "&",
        "[U+27]": "'",
        "[U+28]": "(",
        "[U+29]": ")",
        "[U+2A]": "*",
        "[U+2B]": "+",
        "[U+2C]": ",",
        "[U+2D]": "-",
        "[U+2E]": ".",
        "[U+2F]": "/",
        "[U+30]": "0",
        "[U+31]": "1",
        "[U+32]": "2",
        "[U+33]": "3",
        "[U+34]": "4",
        "[U+35]": "5",
        "[U+36]": "6",
        "[U+37]": "7",
        "[U+38]": "8",
        "[U+39]": "9",
        "[U+3A]": ":",
        "[U+3B]": ";",
        "[U+3C]": "<",
        "[U+3D]": "=",
        "[U+3E]": ">",
        "[U+3F]": "?",
        "[U+40]": "@",
        "[U+41]": "A",
        "[U+42]": "B",
        "[U+43]": "C",
        "[U+44]": "D",
        "[U+45]": "E",
        "[U+46]": "F",
        "[U+47]": "G",
        "[U+48]": "H",
        "[U+49]": "I",
        "[U+4A]": "J",
        "[U+4B]": "K",
        "[U+4C]": "L",
        "[U+4D]": "M",
        "[U+4E]": "N",
        "[U+4F]": "O",
        "[U+50]": "P",
        "[U+51]": "Q",
        "[U+52]": "R",
        "[U+53]": "S",
        "[U+54]": "T",
        "[U+55]": "U",
        "[U+56]": "V",
        "[U+57]": "W",
        "[U+58]": "X",
        "[U+59]": "Y",
        "[U+5A]": "Z",
        "[U+61]": "a",
        "[U+62]": "b",
        "[U+63]": "c",
        "[U+64]": "d",
        "[U+65]": "e",
        "[U+66]": "f",
        "[U+67]": "g",
        "[U+68]": "h",
        "[U+69]": "i",
        "[U+6A]": "j",
        "[U+6B]": "k",
        "[U+6C]": "l",
        "[U+6D]": "m",
        "[U+6E]": "n",
        "[U+6F]": "o",
        "[U+70]": "p",
        "[U+71]": "q",
        "[U+72]": "r",
        "[U+73]": "s",
        "[U+74]": "t",
        "[U+75]": "u",
        "[U+76]": "v",
        "[U+77]": "w",
        "[U+78]": "x",
        "[U+79]": "y",
        "[U+7B]": "{",
        "[U+7C]": "|",
        "[U+7D]": "}",
        "[U+7E]": "~",
        "[U+F7][U+D2]": "AxesOff",
        "[U+F7][U+7A]": "GridOff",
        "[U+A6]": "Int ",
        "[U+DA]": "Deg",
        "[U+DB]": "Rad",
        "[U+D1]": "Cls",
        "[U+F7][U+A5]": "Text ",
        "[U+F7][U+08]": "While ",
        "[U+F7][U+09]": "WhileEnd",
        "[U+81]": "sin ",
        "[U+82]": "cos ",
        "[U+89]": "+",
        "[U+99]": "-",
        "[U+A9]": "×",
        "[U+B9]": "÷",
        "[U+D0]": "π",
        "[U+EB]": "ViewWindow ",
        "[U+0D]": "\n",
        "[U+0E]": "→",
        "[U+13]": "⇒",
        "[U+27]": "'",
        "[U+C1]": "Ran#",
        "[U+7F][U+87]": "RanInt#(",
        "[U+7F][U+B1]": " Or ",
        "[U+00]": "",
        "[U+7F]": "→",
        "[U+5B]": "(",
        "[U+5D]": ")",
        "[U+19]": "ClrGraph",
        "[U+8F]": "Getkey",
        "[U+94]": "RclPict",
        "[U+AB]": "PxlOn",
        "[U+01]": "Then",
        "[U+03]": "IfEnd",
        "[U+04]": "For",
        "[U+05]": "To",
        "[U+06]": "Step",
        "[U+07]": "Next",
        "[U+0A]": "Do",
        "[U+0B]": "LpWhile",
        "[U+B3]": "Not",
        "[U+11]": "≠",
        "[U+12]": "≥",
        "[U+9E]": "Menu",
        "[U+E2]": "Lbl ",
        "[U+EC]": "Goto",
        "[U+E6]": "#",
        "[U+A5]": "E",
        "[U+A7]": "F-Line",
        "[U+AC]": "PxlOff",
        "[U+F7]": "If",
        "[U+F9]": "Str",
        "[U+B0]": "And",
        "[U+02]": "Else"
    }

    for k, v in replacements.items():
        code = code.replace(k, v)
    
    return code

if __name__ == "__main__":
    main()
