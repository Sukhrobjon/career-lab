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


print(excel_column_to_number("Ab"))
