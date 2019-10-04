def atoi(text):
    """
    Converts string into int if it is convertible, otherwise returns 0
    """
    result = ""
    INT_MAX = (2**31)-1
    INT_MIN = -(2**31)
    sign = "+-"
    start = 0
    for i, char in enumerate(text):
        if not char.isspace() and char in sign:
            if char == "-" or char.isdigit():
                result += char
                start = i
                break
    # check if the first char after +- sign is number
    if not text[start+1].isdigit():
        return 0
    
    for i in range(start, len(text)):
        print("num starts:", text[start:])
        char = text[i]
        if char.isdigit():
            print(char)
            result += char
            print("inside isdigit: ", result)
        else:
            break
    print("before return")
    return int(result)


text = "-4193 with words"
result = atoi(text)
print(result)
