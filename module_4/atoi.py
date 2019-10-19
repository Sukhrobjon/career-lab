class Solution(object):
    def atoi(self, text):
        """Converts string into int if it is convertible, otherwise returns 0"""
        
        INT_MAX = (2**31)-1
        INT_MIN = -(2**31)

        # strip the whitesapce
        text = text.strip()
        
        # check if it start with non alphabetic char
        if text[0].isalpha():
            # print(text)
            return 0
        # grabbing the - or + sign to make the process easier
        result = text[0]

        for i in range(1, len(text)):
            char = text[i]
            if not char.isdigit():
                break
            # otherwise
            result += char

        if INT_MIN <= int(result) <= INT_MAX:
            return int(result)
        else:
            return INT_MIN


text = ["42", "   -42", "-4193 with words", "words and 987", "-91283472332"]
word = ".1"
obj = Solution()

# for word in text:   
result = obj.atoi(word)
    # print(result)
