def search_for_range(array, target):
    pass


def binary_search(array, target):
    left = 0
    right = len(array)

    while left < right:
        # mid = (right + left) // 2
        mid = left + (right - left) // 2
        # print(f"mid {mid}")
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1


def first_binary_search(array, target):
    """
    Search for the first occurrence of the target and returns the
    index, or -1 if target not found.
    Args:
        array (list): list of integers
        target (int): a target to be found
    Returns:
        index (int): the first occurrence of the target, -1 if not found
    """
    
    first_occur = binary_search(array, target)
    print(f"first occurrence: {first_occur}")
    if first_occur == -1:
        return -1

    left = 0
    right = first_occur

    while left < right:
        mid = left + (right - left) // 2
        # print(f"while:")
        print(f"left: {left}, right: {right}, mid: {mid}")
        if target == array[mid]:
            if mid < first_occur:
                first_occur = mid
                print(f"mid < first")
                right = mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid

    return first_occur



array = [8, 8, 10]
all_dups = [1, 1, 1, 1, 1, 1]
print(array)
result = first_binary_search(all_dups, 1)
print(result)
