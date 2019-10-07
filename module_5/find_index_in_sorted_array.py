def find_index(nums, target):
    """
    Binary search: 24ms solution from leetcode
    NOTE:You can assume there is no duplicates
    """
    if not nums:
        return 0
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print(f"mid: {mid}, left: {left}, right: {right}")
    return left


nums = [1, 3, 5, 7]
target = 5
result = find_index(nums, target)
print(f"result: {result}, target: {target}")
