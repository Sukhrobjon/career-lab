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


array = list(range(1, 7))
print(array)
result = binary_search(array, 6)
print(result)
