def trailing_zeros(n):
    """Returns number of trailing zeros in n factorial."""
    if n < 5:
        return 0
    if n % 5 == 0:
        return n // 5

print(trailing_zeros(120))
