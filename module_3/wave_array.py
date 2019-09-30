def wave_array(arr):
    """
    Given an array of integers, sort the array into a wave like array and
    return it, In other words, arrange the elements into a sequence such
    that a[0] >= a[1] <= a[2] >= a[3] <= a[4]
    """

    for i in range(0, len(arr), 2):
        # if current even element is smaller than previous, swap
        if i > 0 and arr[i] < arr[i-1]:  # skip the 0th element
            arr[i], arr[i-1] = arr[i-1], arr[i]

        # if current even element is smaller than next
        if i < (len(arr) - 1) and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

arr = [1, 2, 3, 4, 5, 6]

print(wave_array(arr))
