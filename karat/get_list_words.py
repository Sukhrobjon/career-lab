"""
* You should write your code inside a function

* Your function should take the input(s) as argument(s)

* Your function should return the answer as a data-structure

* You can validate/test your code by calling your function and printing the data-structure it returns

* Your function should return the same output if it is called multiple times in a row


https://public.karat.io/content/q093/wordlist.txt

The text file at the URL above lists common words in English, together with a count of their occurrence in a certain text. It is tab-delimited and newline-separated. The file is sorted with most common words at the top. 

\r\n


Given two strings s1 and s2, we will call (s1, s2) a "step" if you can form s2 by adding exactly one letter to s1 and possibly rearranging the letters of s1.

For example:
(OF, FOR) is a step
(OF, IF) is not a step
(OF, OCT) is not a step
(ERA, EAR) is not a step
(SHE, SHEEP) is not a step
(TEE, TEST) is not a step

Given the 1000-word wordlist we just generated, produce an index
 w -> {  w1 | (w, w1) is a step } 
that associates to each word all the words in the wordlist that are a step
away from it.

index = step_index(wordlist)

# Expected output (pseudocode):

index['ERA'] = ['REAL', 'RARE', 'AREA', 'READ', 'RATE',
                'BEAR', 'NEAR', 'RACE',
                'HEAR', 'YEAR', 'DEAR', 'FEAR', 'CARE']


index['JOY'] = []

"""
# all_words = []
# read file
# while i read it
# if the word has length 2 <= word <= ab
# all words append this current word [word, occur]
# def step_index(wordlist):

#     for word in wordlist:
#        pass

import urllib.request


def one_step(s1, wordlist):
    s1_sorted = sorted(s1)
    index_dict = []

    for word in wordlist:
        if len(word[0]) == len(s1) + 1:
            print("words: ", word[0])
            s2_sorted = sorted(word[0])
    #         step away
            if s1_sorted == s2_sorted[:len(s1_sorted)]:
                print("word", word)
                index_dict.append(word[0])

    return index_dict


def get_list(n, k):
    """
    Write a function that, given parameters N and K, downloads the file and returns
    the N most common words of length [2..K] together with their occurrence counts.
    len(file) = m
    worst = O(m)
    best = o(n)
    
    """
    all_words = []

    url = "https://public.karat.io/content/q093/wordlist.txt"
    raw_text = urllib.request.urlopen(url).read().decode('utf8')
    count = 0
    for line in raw_text.split("\r\n"):
        word = line.split("\t")
        if count == n:
            break
        if 2 <= len(word[0]) <= k:
            all_words.append(word)
            count += 1

    return all_words


result = (get_list(1000, 5))
# print(result)


index = one_step('ERA', result)
print(index)
