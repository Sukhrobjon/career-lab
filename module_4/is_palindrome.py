import re


def is_palindrome_iterative(text):
    """
    A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing.
    """

    # normalize the string and remove all punctuation and whitespaces
    text = re.sub('[^A-Za-z0-9]+', '', text.lower())

    last_index = len(text) - 1
    for i in range(len(text)//2):
        if text[i] != text[last_index-i]:
            return 0
    return 1


text = "A man, a plan, a canal, Panama."
print(is_palindrome_iterative(text))
