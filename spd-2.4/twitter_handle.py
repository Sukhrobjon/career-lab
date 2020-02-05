class SimilarAccounts():
    
    def suggest(self, new_user: str, handles: list, k: int = 2):
        """
        Returns the two most similar account handles associated with
        new_user handle
        
        Args:
            new_user(str): New user's handle
            handles(list): Existing users handles
            k(int): number of similar accout handles

        Returns:
            handle(tuple): two most similar score accounts
        """
        scores = []
        pass

    def get_score_with_anagram(self, handle1, handle2):
        """
        Get the similarity score between two user handles
        +1 for each letter in the alphabet that occurs in both handles but
        scoring –1 for each letter that occurs in only one handle
        """
        anagram1 = self.make_anagram(handle1)
        anagram2 = self.make_anagram(handle2)
        
        score = 0
        for i in range(len(anagram1)):
            if anagram1[i] >= 1 and anagram2[i] > 0:
                score += 1
            elif anagram1[i] >= 1 and anagram2[i] == 0:
                score -= 1
            elif anagram2[i] >= 1 and anagram1[i] > 0:
                score += 1
            elif anagram2[i] >= 1 and anagram1[i] == 0:
                score -= 1
        
        return score

    def get_score_with_set(self, handle1, handle2):

        handle1 = set(handle1)
        handle2 = set(handle2)

        sym_diff = handle1.symmetric_difference(handle2)
        intersection = handle1.intersection(handle2)

        print(sym_diff, intersection)

        score = intersection - sym_diff
        
        return len(score)

    def make_anagram(self, word):
        """
        Create a anagram representation of the word.
        NOTE: It processes words contain only lowercase letters
        """

        # hashing 26 English letters
        anagram = [0] * 26
        offset = ord('a')

        for letter in word:
            index = ord(letter.lower()) - offset
            anagram[index] += 1

        return anagram


handles = ['DogeCoin', 'YangGang', 'HodlForLife',
           'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
new_user = 'iLoveDogs'

obj = SimilarAccounts()
result1 = obj.make_anagram(new_user)
result2 = obj.make_anagram('DogeCoin')
anagram_score = obj.get_score_with_anagram(new_user, 'DogeCoin')
set_score = obj.get_score_with_set(new_user, 'DogeCoin')
print("New us:", result1)
print("Handle:", result2)
print("anagram score:", anagram_score)
print("set score:", set_score)
