class TwoSum():

    def two_sum_v1(self, numbers, target):
        """
        Return a pair in a list of numbers add up to the target
        Brute force solution: compares all posibble pairs to find the pair
        Runtime: Worst and Average is O(n^2), because, the pair might be at
        the last two elements of the numbers list.
        Returns: all_pairs(list of list)
        """
        all_pairs = list()
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                # if we find the pair adds up to target
                if numbers[i] + numbers[j] == target:
                    all_pairs.append([numbers[i], numbers[j]])

        return all_pairs
    
    # TODO: there is a bug, left and right should always be incremented or
    # decremented by 1
    def two_sum_v2(self, numbers, target):
        """
        Given an array of numbers and target value, return all pairs
        whose sum is target. assuming numbers are unique
        Runtime: O(nlog(n)), because we need to sort the array and
        we can use two pointers from the left and right. 
        Returns: all_pairs(list of list)
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

    def two_sum_v3(self, numbers, target):
        """
        Given an array of numbers and target value, return all pairs
        whose sum is target. assuming numbers are unique
        Runtime: O(n), because we are using Hashtable to store the seen
        numbers and search if the complement of target value and current
        number in the numbers array.
        Returns: all_pairs(list of list)
        """
        all_pairs = list()
        seen = dict()

        for i, number in enumerate(numbers):
            complement = target - number
            if complement not in seen:
                seen[number] = i
            else:   # we found the pair
                all_pairs.append([complement, number])
        
        return all_pairs

    def two_sum_with_duplicate(self, numbers, target):
        """
        Given an array of numbers and target value, return all pairs
        whose sum is target. Duplicates might exist
        Runtime: O(n), because we are sting using the hashtable to store the
        seen values, so we can search for them later as complement of target and
        current number
        Returns:
            all_pairs(list of lists)
        """
        # first we need to build the hash table, because there might be a duplicates
        numbers_dict = {}

        for i, number in enumerate(numbers):
            # if we saw the number before we just add the new index
            # so we know how many times it is occured
            if number in numbers_dict:
                numbers_dict[number].append(i)
            else:
                numbers_dict[number] = [i]
        
        return numbers_dict

numbers = [5, 3, 6, 3, 8, 2, 2, 8, 4, 7]
target = 10
obj = TwoSum()
result = obj.two_sum_with_duplicate(numbers, target)
print(result)
