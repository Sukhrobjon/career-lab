def single_number(integers):
    """
    Naive version: Given a non-empty array of integers, every element appears
    twice except for one. Find that single one.
    Runtime: O(n), Space: O(n)
    """
    seen = set()
    for integer in integers:
        if integer in seen:
            seen.remove(integer)
        else:
            seen.add(integer)

    return seen.pop()


def find_unique_elem(arr):
    """
    Given a non-empty array of integers, every element appears
    twice except for one. Find that single one.
    Runtime: O(n), Space: O(1)
    """
    result = 0
    for item in arr:
        # all numbers repeated twice will be equal to 0 after XOR operation
        # at the end, only left is the unique integer
        result ^= item
    return result


arr = [2, 2, 1]


print(find_unique_elem(arr))
