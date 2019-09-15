def power_of_three(n):
    """Determine if number n is power is three
    Returns True if n is power of three, False otherwise
    """
    # devide the number by 3 until
    # it is not devisible and equal to 1
    quotient = 0

    while quotient != 1:
        if n % 3 == 0 and n >= 3:
            quotient = n // 3
            n = quotient
        else:
            print("quotient:", quotient)
            return False

    return True


print(power_of_three(0))