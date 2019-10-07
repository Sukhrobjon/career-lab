def length_of_last_word(text):
    """
    Given a string s consists of upper/lower-case alphabets and empty space
    characters ' ', return the length of last word in the string.

    NOTE: Please make sure you try to solve this problem without using library
    functions. Make sure you only traverse the string once. If there is one word
    it is the last word.
    Args:
        text (str): long string consisted of word(s)
    Return:
        length (int): length of the last word in the string
    """
    # counter for the last word in the string
    length = 0
    last_word = ""
    # start iterating the string at the end of it
    for i in range(len(text)-1, -1, -1):
        char = text[i]
        if char.isalpha():
            last_word += char
            length += 1
        # stop the loop if we there is space, because it means we
        # count the length of the last word already
        elif char.isspace():      
            break
    # print(last_word[::-1])
    return length


text = "Helloworld"
print(length_of_last_word(text))
