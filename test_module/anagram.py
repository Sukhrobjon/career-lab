def anagram(word1, word2):
    """Determines if two words are anagram of each other"""

    # if the strings are not equal length they can't be anagram
    if len(word1) != len(word2):
        return False

    s1 = 0
    s2 = 0

    # add up the ascii values of each chars
    for i in range(len(word1)):
        s1 += ord(word1[i])
        s2 += ord(word2[i])
    # compare if sums are equal
    return s1 == s2


word1 = "*$a*):"
word2 = "$*a*:)"

print(anagram(word1, word2))
