def excel_column_to_number(column):
    """
    """
    offset = 64
    # iterate throurgh the title
    # for each character
    # add the value by multiplying the base
    value = 0
    base = 26
    for index, char in enumerate(column):
        char_val = ord(char) - offset
        value += (base ** index) * char_val
        # 1 += (26 ** 1) * 2
    return value


print(excel_column_to_number("AB"))