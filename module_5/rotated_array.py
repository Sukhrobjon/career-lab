def find_pivot_index(nums):
    """
    Find the min num in the rotated sorted array.
    """
    min_num = nums[0]
    pivot_index = 0
    left = 0
    right = len(nums) - 1
    # i = 0

    while left <= right:
        mid = (left + right) // 2
        print(nums[mid])
        if min_num < nums[mid]:
            left = mid + 1
        elif min_num > nums[mid]:
            min_num = nums[mid]
            pivot_index = mid
            right = mid - 1

    return pivot_index, min_num

def search
nums = [2, 2, 4, 5, 7, 1]
result = find_pivot_index(nums)
print(result)
