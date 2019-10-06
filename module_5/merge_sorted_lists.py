def merge_sorted_list(arr1, arr2):
    # m = len(arr1), n = len(arr1)
    # since we know arr1 is always greater or equal to (m+n)
    # we compare arr2[i] with arr1[j] element and check if it
    # should be placed there
    
    i, j = 0, 0
    while i < len(arr1) - 1:
        if j > len(arr2) - 1:
            break
        else:
            if arr2[j] == arr1[i] or arr2[j] < arr1[i+1]:
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


a = [1, 2, 3, 0, 0, 0]
b = [1, 2, 3, 3, 4, 6]

result = merge_sorted_list(a, b)

print("result: ", result)
