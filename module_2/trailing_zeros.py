def trailing_zeros(n):
    """Returns number of trailing zeros in n factorial."""
    # factorial of nums less 5 doesn't end with 0
    if n < 5:
        return 0
    # example: n = 11
    # n % 5 = 1 => n - 1 = 10 => 10 // 5 = 2
    reminder = n % 5
    result = (n - reminder) // 5
    return result


print(trailing_zeros(20))
