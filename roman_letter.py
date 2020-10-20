def convert_number_to_roman_letter(number):
    ref_roman_letters = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 50: "L"}
    if number in ref_roman_letters.keys():
        return ref_roman_letters[number]
    else:
        ret = ""

        if number >= 20:
            quotien = number // 10
            number = number % 10
            ret = quotien * "X"

        if number >= 10:
            number -= 10
            ret = "X"

        if number >= 5:
            number -= 5
            ret += "V"

        return ret + (number % 5) * "I"


import re

def regexp():
    match = re.match(r"([0-9])([0-9])", '21', re.I)
    if match:
        print(match.groups())

if __name__ == "__main__":
    regexp()