def merge_sorted_list(arr1, arr2):
    # m = len(arr1), n = len(arr1)
    # since we know arr1 is always greater or equal to (m+n)
    # we compare arr2[i] with arr1[j] element and check if it
    # should be placed there
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):

        if arr2[j] == arr1[i] or arr2[j] <= arr1[i+1]:
            arr1.insert(i+1, arr2[j])
            arr1.pop()
            i += 2
            j += 1
        elif arr2[j] > arr1[i]:
            if arr1[i+1] == 0:
                arr1[i+1] = arr2[j]
                i += 1
                j += 1
            else:
                i += 1
        elif arr2[j] < arr1[i]:
            arr1.insert(i, arr2[j])
            arr1.pop()
            i += 1
            j += 1
        print(arr1)
    return arr1

def merge_sorted_list_v2(nums1, m, nums2, n):
    # fill up that empty space with string
    stop = 0
    for i in range(len(nums1)-1, 0, -1):
        if stop == len(nums2):
            break
        else:
            nums1[i] = ""
            stop += 1
    print(nums1)
    if m == 0:
        nums1 = nums2
    
    i, j = 0, 0

    empty_space = len(nums2)
    while j < len(nums2):
        if nums2[j] <= nums1[i] or i == empty_space:
            nums1.insert(i, nums2[j])
            nums1.pop()
            j += 1
            empty_space += 1
        else:
            i += 1

    return nums1
a = [1, 2, 3, 0, 0, 0]
b = [2, 5, 6]

nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
m = 6
nums2 = [1, 2, 2]
n = 3
result = merge_sorted_list_v2(nums1, 6, nums2, 3)

print("result: ", result)
