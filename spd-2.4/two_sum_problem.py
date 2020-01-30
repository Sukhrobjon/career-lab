class Solution():

    def two_sum_v1(self, numbers, target):
        """
        Finds a pair in a list of numbers add up to the target
        Brute force solution: compares all posibble pairs to find the pair
        Runtime: Worst and Average is O(n^2), because, the pair might be at
        the last two elements of the numbers list.
        """
        all_pairs = list()
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                # if we find the pair adds up to target
                if numbers[i] + numbers[j] == target:
                    all_pairs.append([numbers[i], numbers[j]])

        return all_pairs
    
    def two_sum_v2(self, numbers, target):
        """
        Given an array of numbers and target value, find all pairs
        whose sum is target. assuming numbers are unique
        Runtime: O(nlog(n)), because we need to sort the array and
        we can use two pointers from the left and right. 
        """
        s_numbers = sorted(numbers)  # O(nlogn)
        left, right = 0, len(s_numbers) - 1
        all_pairs = list()

        # it left should be strictly less than right pointer
        # in terms of its position, because we can't add the same
        # number to itself
        while left < right:  # O(logn)
            if s_numbers[left] + s_numbers[right] == target:
                all_pairs.append([s_numbers[left], s_numbers[right]])
            left += 1
            right -= 1

        return all_pairs


numbers = [2, 1, 2, 2]
target = 4
obj = Solution()
result = obj.two_sum_v2(numbers, target)
print(result)
