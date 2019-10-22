"""
Description:
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a
non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned.
Do not use any built square root functions.
"""


def square_root(n):
    """
    Compute and return the square root of n, where n is guaranteed to be a
    non-negative integer.
    """
    # this runs always n // 2 guaranteed, beacuse square root never
    # be greater than half of that number n
    for divisor in range(1, n+1):
        qoutient = n // divisor
        if divisor >= qoutient:
            return qoutient

for i in range(1, 26):
    result = square_root(i)
    print(f"Square root of {i} is {result}")
