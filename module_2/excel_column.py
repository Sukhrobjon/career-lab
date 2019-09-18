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
    """Converts a string(column title) to number representation
    BDF = 1462
    val = 0
    B = 2 * (26 ** 2) = 1352
    D = 4 * (26 ** 1) = 104
    F = 6 * (26 ** 0) = 6
    """

    offset = ord("A") - 1    # capital 'A' ascii value
    result = 0
    power = len(column) - 1
    BASE = 26

    for _, char in enumerate(column):
        # handling non ascii values
        if char not in string.ascii_letters:
            raise ValueError("String should be ascii letter!")
        # getting the numerical value of curren char
        cur_char = ord(char.upper()) - offset
        result += cur_char * (BASE ** power)
        # decrementing the power as we move to the left
        power -= 1
    return result


column = "BDF"
print(excel_column_to_number(column))
