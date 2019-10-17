def search_for_range(array, target):
    pass


def binary_search(array, target):
    left = 0
    right = len(array)

    while left < right:
        # mid = (right + left) // 2
        mid = left + (right - left) // 2
        print(f"mid {mid}")
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
    left = 0
    right = len(array)
    first_occur = -1
    while left < right:
        mid = left + (right - left) // 2

        if target == array[mid]:
            if mid < first_occur and first_occur == -1:
                first_occur = mid


array = [5, 7, 7, 8, 8, 10]
print(array)
result = binary_search(array, 8)
print(result)
