from heapq import nlargest

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
        # stores the handle and score as (handle, score)
        scores = []
        
        for handle in handles:
            score = self.get_score_with_set(new_user, handle)
            scores.append((handle, score))
        # get the k largest handles
        k_handles = nlargest(k, scores, lambda score: score[1])
        
        return [h[0] for h in k_handles]

    def get_score_with_anagram(self, handle1, handle2):
        """
        Get the similarity score between two user handles
        +1 for each letter in the alphabet that occurs in both handles but
        scoring –1 for each letter that occurs in only one handle
        """
        anagram1 = self.make_anagram(handle1)
        anagram2 = self.make_anagram(handle2)
        print(f"{handle1} anagram: {anagram1}")
        print(f"{handle2} anagram: {anagram2}")
        
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

        handle1 = set(handle1.lower())
        handle2 = set(handle2.lower())
        # print(f'handle1 set: {handle1}, \nhandle2 set: {handle2}')

        # number of -1s, all unmatch letters
        sym_diff = handle1.symmetric_difference(handle2)
        # number of +1s all matching letters
        intersection = handle1.intersection(handle2)


        # print(f"symmetric difference: {sym_diff}, \nintersection: {intersection}")

        score = len(intersection) - len(sym_diff)
        
        return (score)

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

# NOTE: this solution assumes the handles are only english letters

handles = ['DogeCoin', 'YangGang', 'HodlForLife',
           'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
new_user = 'iLoveDogs'

obj = SimilarAccounts()
result1 = obj.make_anagram(new_user)
result2 = obj.make_anagram('DogeCoin')
anagram_score = obj.get_score_with_anagram(new_user, 'GodIsLove')
set_score = obj.get_score_with_set(new_user, 'GodIsLove')
print(f"anagram score:", anagram_score)
print(f"set score:", set_score)
k_handles = obj.suggest(new_user, handles, 4)

print(k_handles)
