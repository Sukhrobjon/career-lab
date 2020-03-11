class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # at the beginnning set it to empty list
        combinations = []

        self.helper(digits, combinations.append, 0, [])

        return combinations

    def helper(self, digits, combinations, index, prefix=None):
        """
        Helper function to build the combination
        """
        digit_map = {
                    '1': '', '2': 'abc', '3': 'def',
                    '4': 'ghi', '5': 'jkl', '6': 'mno',
                    '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        if prefix is None:
            prefix = []

        if len(digits) == 1:
            return digit_map[digits]
        if index >= len(digits):
            prefix.append(prefix)
            return

        pass

    def iterative_combination(self, digits):
        """
        Credit:
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/184395/Python-20ms-faster-than-100.00-of-other-python-submissions
        """
        digit_map = {
                    '1': '', '2': 'abc', '3': 'def',
                    '4': 'ghi', '5': 'jkl', '6': 'mno',
                    '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
                    }
        all_combinations = [""]
        for digit in digits:
            
            current_comb = []
            
            for com in all_combinations:
                for letter in digit_map[digit]:
                    
                    current_comb.append(com + letter)
            
            all_combinations = current_comb
            
        return all_combinations

    def rec_combination(self, digits, all_combinations=None):
        """
    
        """
        digit_map = {
                        '1': ' ', '2': 'abc', '3': 'def',
                        '4': 'ghi', '5': 'jkl', '6': 'mno',
                        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
                    }
        # base case, all combinations is None
        if all_combinations is None:
            all_combinations = [""]
        # no digits left to add up
        if digits == "":
            return all_combinations
        
        # current digit
        digit = digits[0]

        current_combo = []
        for combo in all_combinations:
            for letter in digit_map[digit]:
                current_combo.append(combo + letter)

        return self.rec_combination(digits[1:], current_combo)


digits = '234'
obj = Solution()
combinations = obj.rec_combination(digits)
# combinations = obj.iterative_combination(digits)
print(combinations)
