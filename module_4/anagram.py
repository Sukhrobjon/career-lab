def is_anagram_v1(word1, word2):
    """Determines if two words are anagram of each other"""

    # if the strings are not equal length they can't be anagram
    if len(word1) != len(word2):
        return False

    offset = 97
    count_s = [0] * 26
    count_t = [0] * 26

    for i in range(len(word1)):
        count_s[ord(word1[i])-offset] += 1
        count_t[ord(word2[i])-offset] += 1
    print(count_s)
    print(count_t)
    # comparing the the two arrays
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            return False
    return True


def is_anagram_v2(word1, word2):
    """Determines if two words are anagram of each other"""

    # if the strings are not equal length they can't be anagram
    if len(word1) != len(word2):
        return False

    offset = 97
    count = [0] * 26

    for i in range(len(word1)):
        count[ord(word1[i])-offset] += 1
        count[ord(word2[i])-offset] -= 1
    print(f"all chars: {count}")
    for i in count:
        if i != 0:
            return False
    return True


def is_anagram_v3(s, t):
    """
    NOTE: THIS SOLUTION DOES NOT WORK FOR ALL CASES
    e.g: s = 'ac', t = 'bb', or aa vs bb
    """
    val = 0

    for i in range(len(s)):
        val ^= ord(s[i])
        print(f"val: {val}")
        val ^= ord(s[i])
        print(f"val: {val}")
    return val == 0

word1 = "aa"
word2 = "bb"
print(is_anagram_v1(word1, word2))
