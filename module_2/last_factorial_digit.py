def last_factorial_digit(n):
    """Returns the last digit of the factorial of number,
    Given that n is non-negative number.
    NOTE: Solve it without calculating the factorial of the number
    """
    # if n >= 5, then we know there is 2 and 5 in the multiplication
    # which mutplication of 2 and 5 always ends with 0.
    if n >= 5:
        return 0
    else:
        return factorial(n) % 10


def factorial(n):
    """Helper function to calculate only factorial of 1-4(inclusive)"""
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = 4
m = 6

print(last_factorial_digit(n))
