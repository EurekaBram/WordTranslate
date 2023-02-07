# first we will translate all letters to number following underlying schema
# finally we will transform the numbers to their final form
# medeklinkers ->1 -> w
# tweeklank ->2
# drieklank -> 3
# dof -> 4 -> d
# lang -> 5 -> zz
# kort -> 6 -> z
import csv
import sys

Three = ["aai", "ooi", "oei", ]
Three_Special = ["eeuw", "ieuw"]
Two = ["eu", "ui", "ie", "oe", "au", "ou", "ei", "ij"]
Vowels = ["a", "e", "i", "o", "u", "y"]
TranslateChars = ["1", "2", "3", "4", "5", "6"]
EncodingArray = ["w", "2", "3", "d", "zz", "z"]


def replace_char(word, vowel, replacement):
    newWord = word
    if vowel in word:
        newWord = word.replace(vowel, replacement)
    return newWord


def replace_not_occur_chars(string, char_arr):
    new_string = ""
    for c in string:
        if c in char_arr:
            new_string += c
        else:
            new_string += "1"
    return new_string


def replace_double_cons(string):
    result = ""
    i = 0
    while i < len(string)-1:
        if string[i] not in Vowels+TranslateChars and string[i] == string[i + 1]:
            result += "1"
            i += 1
        else:
            result += string[i]
        i += 1
    if i < len(string):
        result += string[i]
    return result


def replace_chars_in_string(string, index, number_of_chars, replacement):
    return string[:index] + replacement + string[index + number_of_chars:]


def fiveCharSpecialCase(word):
    return len(word) == 5 and word.endswith("en")


def matPrefix(string):
    newString = string
    if string.startswith("ver") and len(string) > 3:
        newString = replace_chars_in_string(string, 0, 3, "141")
    if string.startswith("be") and len(string) > 2 and string[2] != "e" and not fiveCharSpecialCase(string):
        newString = replace_chars_in_string(string, 0, 2, "14")
    if string.startswith("ge") and len(string) > 2 and string[2] != "e" and not fiveCharSpecialCase(string):
        newString = replace_chars_in_string(string, 0, 2, "14")
    return newString


def matSuffix(string):
    newString = string
    if string.endswith("en") and (len(string)-3) != "e":
        newString = replace_chars_in_string(string, len(string)-2, 2, "41")
    return newString


def translate_to_numbers(word):
    # Replace vowels with numbers
    # Three
    for tone_3 in Three:
        word = replace_char(word, tone_3, "3")
    for tone_3 in Three_Special:
        word = replace_char(word, tone_3, "31")
    # Mat vowels (dof)
    word = replace_char(word, "ig", "41")
    word = replace_char(word, "ing", "411")
    word = replace_char(word, "lijk", "141")

    # Two
    for tone_2 in Two:
        word = replace_char(word, tone_2, "2")
    # Mat vowels continued
    word = matPrefix(word)
    word = matSuffix(word)
    # Short and long vowels
    for vowel in Vowels:
        word = replace_char(word, vowel, "6")
    # Replace consonants with number
    # Sch and ch
    word = replace_char(word, "sch", "1")
    word = replace_char(word, "ch", "1")
    # doubles
    word = replace_double_cons(word)
    # singles
    word = replace_not_occur_chars(word, Vowels + TranslateChars)
    # result
    return word


def translate_to_encoding(word):
    result = ""
    for c in word:
        result += EncodingArray[int(c)-1]
    return result


if __name__ == '__main__':
    fileName = ""
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    else:
        fileName = input("Please enter the file name: ").lower()
    # Read the words in the excel file
    file = open(fileName)
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row[0].lower().strip())
    print(rows)
    # Translate words
    translatedWords = []
    for w in rows:
        # Translate the word into a temporary encoding
        encoded = translate_to_numbers(w)
        # Translate the encoded version into the proper encoding
        translated = translate_to_encoding(encoded)
        translatedWords.append(translated)
    print(translatedWords)
    file.close()
    with open('translation.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Woord", "Vertaling"])
        for i in range(len(rows)):
            writer.writerow([rows[i], translatedWords[i]])
