def anagram(word1, word2):
    s1 = 0
    s2 = 0
    for i in range(len(word1)):
        s1 += ord(word1[i])
        s2 += ord(word2[i])
    
    return s1 == s2


word1 = "listes"
word2 = "silent"

print(anagram(word1, word2))