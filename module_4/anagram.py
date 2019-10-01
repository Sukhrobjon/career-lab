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
    return 0 if count_s == count_t else 1


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


word1 = "abcdefghijklmnopqrstuaaaaa"
word2 = "zbcdefghijklmnopqrstuvwxyy"
print(is_anagram_v2(word1, word2))
