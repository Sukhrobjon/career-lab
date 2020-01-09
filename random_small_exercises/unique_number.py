from collections import Counter
def unique_number(arr):
    """
    Returns unique number if one exist in the list 
    """
    my_dic = Counter(arr)
    
    for key, value in my_dic.items():
        if my_dic[key] == 1:
            return key
    return "There is no unique number in the list"

    
arr = [7, 2, 2, 7, 4, 9, 9, 7, 4, 1]
print("unique number is: {}".format(unique_number(arr)))


# def findPair(arr, k):
#     for item in arr:
#         outer_diff = k - item
#         for i in range(len(arr)-1):
#             diff = outer_diff - i
#             if (diff) in arr:
#                 return True
#             else:
#                 return False

# arr2 = [5,3,1,3,4] 

# print(findPair(arr2, 6))
