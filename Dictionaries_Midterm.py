####Part 1

# codes = {'A':'%’, 'a':‘9’, 'B':‘@’, 'b':'--', 'C':'&', 'c':'1', 'D':'µ', 'd':'3'}
codes = {
    "A": "%",
    "a": "9",
    "B": "@",
    "b": "--",
    "C": "&",
    "c": "1",
    "D": "µ",
    "d": "3",
    "E": "4",
    "e": "|",
    "F": "^",
    "f": "6",
    "G": "Ô",
    "g": "{",
    "H": "ø",
    "h": "~",
    "I": ">",
    "i": "Ç",
    "J": "-",
    "j": "0",
    "K": ";",
    "k": "¡",
    "L": "{",
    "l": "=",
    "M": ")",
    "m": "*",
    "N": "<",
    "n": "?",
    "O": "5",
    "o": "-",
    "P": "&",
    "p": "[",
    "Q": "+",
    "q": "_",
    "R": "ß",
    "r": "‡",
    "S": "¹",
    "s": "ê",
    "T": "ì",
    "t": "ò",
    "U": "¿",
    "u": "ã",
    "V": "ï",
    "v": "≠",
    "W": "Ý",
    "w": "²",
    "X": "¦",
    "x": "¯",
    "Y": "ù",
    "y": "ž",
    "Z": ",",
    "z": "µ",
    " ": " ",
    ".": ".",
    ":": ":",
}


infile = open("info_security.txt", "r")
outfile = open("info_security_encrypted.txt", "w")

infile_str = infile.read()
outfile_str = " "

print(infile_str)

for element in infile_str:
    new_char = codes[element]
    outfile_str += new_char

print(outfile_str)

outfile.write(outfile_str)

##Part2

words_to_count = ["Father", "God", "Christ", "Spirit", "life", "man"]
john_infile = open("book of John text.txt", "r")
john_str = john_infile.read()

john_words = john_str.split()

john_words_freqs = {}

for x in words_to_count:
    freq = john_words.count(x)
    john_words_freqs[x] = freq

print(john_words_freqs)