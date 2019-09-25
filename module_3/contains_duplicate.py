def contains_duplicate(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result ^= arr[i]
        if result == 0:
            pass