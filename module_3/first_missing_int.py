def first_missing_positive_int(integers):
    """Finds the first missing positive integer in the unsorted list
    Returns:
        num(int): missing int in the sequence
    """
    pos_ints = [i for i in integers if i > 0]
    seen_dict = {i: None for i in integers}
    return seen_dict


a = [3, 4, -1, 1]

print(first_missing_positive_int(a))

b = sorted(a)
print(b)