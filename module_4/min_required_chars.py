"""
Minimum Characters required to make a String Palindromic
You are given a string. The only operation allowed is to insert characters in
the beginning of the string. Return the number of characters that are needed
to be inserted to make the string a palindrome string


Examples:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2
"""


def min_required_char(text: str) -> int:
    """
    NAIVE VERSION!
    Find minimum number of characters required to make a String Palindromic
    NOTE:The only operation allowed is to insert characters in the beginning
    of the string. Return the number of characters that are needed to be
    inserted to make the string a palindrome string.
    Rutime: O(n^2)
    Args:
        text(str): given string
    Returns:
        num of chars(int): min required chars to make a string palindromic
    """

    if not text:
        return 0

    left = 0
    right = len(text) - 1
    sliding_window = 2

    while left <= right:

        if text[left] != text[right]:
            right = len(text) - sliding_window
            print(f"right: {right}")
            left = 0
            print(f"left: {left}")
            sliding_window += 1
        else:
            right -= 1
            left += 1

    return sliding_window - 2


text = '1221111'
result = min_required_char(text)
print(f"Min required chars in {text} is: {result}")
