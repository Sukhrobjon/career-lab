nums = []

def fizzbuzz(start, end, nums=None):
    """
    Recursive Fizzbuzz
    """
    if visit is None:
        nums = []
    # when this ends
    if start == end + 1:
        return nums
    
    if start % 3 == 0 and start % 5 == 0:
        nums.append('fizzbuzz')
        return fizzbuzz(start+1, end)
    elif start % 3 == 0:
        nums.append('fizz')
        return fizzbuzz(start+1, end)
    if start % 5 == 0:
        nums.append('buzz')
        return fizzbuzz(start+1, end)
    else:
        nums.append(start)
        return fizzbuzz(start+1, end)

# nums = []
# result = fizzbuzz(1, 20)
print(nums)
