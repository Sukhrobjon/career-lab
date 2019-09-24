def first_missing_positive_int(integers):
    """Finds the first missing positive integer in the unsorted list
    Returns:
        num(int): missing int in the sequence
    """
    seen_nums = []
    for integer in integers:
        if integer < 0:
            continue
        if integer + 1 > len(seen_nums):
            extended_size = integer - len(seen_nums) + 1
            seen_nums.extend([False] * extended_size)
        seen_nums[integer] = True
    # return seen_nums

    # finding the actual number
    miss_int = 0
    for i in range(1, len(seen_nums)):
        if seen_nums[i] is False:
            miss_int = i
            return miss_int
    # if we never found the missing integer and seen_nums is empty
    # then we know first missing positive int is 1
    if miss_int == 0 and len(seen_nums) == 0:
        return 1
    else:
        return len(seen_nums)


a = [-8, -7, -6]

print(first_missing_positive_int(a))
