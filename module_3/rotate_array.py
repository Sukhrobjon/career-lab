def rotate_array_v1(arr, k):
    """
    Naive version: Given an array, rotate the array to the right by k steps,
    where k is non-negative.
    Run time: O(n)
    Space Complexity: O(k) I need to ask
    """
    # 1st slice get all elements from k number of elements from last element
    # 2nd slice get everthying but not last k number of elements
    return (arr[-k:] + arr[:-k])


def rotate_array_v2(arr, k):
    """
    """
    # run time of loop is O(k*n) as it runs insert operation k times
    # where insert takes O(n)
    for _ in range(k):
        target = arr.pop()  # get the last element in the list
        # run time is O(n)
        arr.insert(0, target)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
# arr = [-1, -100, 3, 99]
k = 3
print(rotate_array_v1(arr, k))
