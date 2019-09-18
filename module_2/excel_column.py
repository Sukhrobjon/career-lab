"""
A -> 1
B -> 2
C -> 3
Z -> 26
AA -> 27
AB -> 28
Prompt
Given a column title as appears in an Excel sheet, return its corresponding
column number.
"""
import string


def excel_column_to_number(column):
    """Converts a string(column title) to number representation"""

    offset = 65     # capital 'A' ascii value
    value = 0
    BASE = 26
    for _, char in enumerate(column):
        if char not in string.ascii_letters:
            raise ValueError("String should be ascii letter!")
        char_val = ord(char.upper()) - offset
        value = BASE * value + 1 + char_val
    return value


# print(excel_column_to_number("Ab"))

# BDF = 1462
# val = 0
# B = 2 * (26 ** 2) = 1352
# D = 4 * (26 ** 1) = 104
# F = 6 * (26 ** 0) = 6


column = "BDF"
power = len(column) - 1
result = 0
base = 26
for i in range(len(column)):
    char_val = ord(column[i]) - 64
    result += char_val * (base ** power)
    power -= 1

print(f"result: {result}")