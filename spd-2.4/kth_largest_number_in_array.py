class Solution():
    def k_largest_v1(self, numbers, k):
        """
        Sort the array and return the kth largest element in the array
        Naive solution
        """
        numbers.sort(reverse=True)
        return numbers[:k]

    def k_largest_v2(self, numbers, k):
        
numbers = [7, 9, 10, 2, 35, 90, 23, 0, 3, 5, 20]
print(Solution().k_largest_v1(numbers, 3))