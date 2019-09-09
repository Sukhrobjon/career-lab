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


def excel_column_to_number(column):
    """Converts a string(column title) to number representation"""
    offset = 65     # capital 'A' ascii value
    # iterate throurgh the title
    # for each character
    # add the value by multiplying the base
    value = 0
    BASE = 26
    for _, char in enumerate(column):
        char_val = ord(char.upper()) - offset
        print(char)
        value = BASE * value + 1 + char_val
    return value


print(excel_column_to_number("AAb"))
