def wave_array(arr):
    """
    Given an array of integers, sort the array into a wave like array and
    return it, In other words, arrange the elements into a sequence such
    that a[1] >= a[2] <= a[3] >= a[4] <= a[5]
    """

    for i in range(len(arr)-1, 2):
        print(arr[i])
        arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

arr = [1, 2, 3, 4, 5]

print(wave_array(arr))