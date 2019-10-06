def find_pivot_index(nums):
    """
    Suppose a sorted array A is rotated at some pivot unknown to you
    beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element. NOTE: The array will not contain duplicates.
    """
    min_num = nums[0]
    pivot_index = 0
    left = 0
    right = len(nums) - 1
    if left == right:
        return pivot_index, nums[pivot_index]

    while left <= right:
        mid = (left + right) // 2
        print(nums[mid])
    
        if min_num > nums[mid]:
            min_num = nums[mid]
            pivot_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return pivot_index, min_num


def find_pivot_index_in_duplicates(nums):
    """
    Suppose a sorted array A is rotated at some pivot unknown to you
    beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element. NOTE: The array will contain duplicates.
    """
    min_num = nums[0]
    pivot_index = 0
    left = 0
    right = len(nums) - 1
    if left == right:
        return pivot_index, nums[pivot_index]

    while left <= right:
        mid = (left + right) // 2

        print(nums[mid], mid)

        if min_num > nums[mid]:
            min_num = nums[mid]
            pivot_index = mid
            right = mid - 1
        # elif min_num == nums[mid]:
        #     # continue

        else:
            left = mid + 1

    return pivot_index, min_num


# nums = [4, 5, 6, 7, 0, 1, 2]
nums = [10, 10, 10, 10, 1]
single = [5, 5, 5, 5, 3]
result = find_pivot_index_in_duplicates(nums)
print(result)
