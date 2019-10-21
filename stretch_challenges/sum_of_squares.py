def sum_of_squares(k, base, number):
    """Calculates sum of squares of each digit of number.
    NOTE: Base range is 3 <= base <= 16"""
    result = encode(number, base)
    sums = 0
    for digit in result:
        sums += int(digit)**2
    print(k, sums)


# max 32 unsigned integer = 4,294,967,295
def encode(number, base):
    """
    Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)
    NOTE: For the purpose of this function we keep remainders as number
    we didnt convert them into hex value
    """
    # Handle up to base 36 [0-9a-z]
    assert 3 <= base <= 16, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    dividend = number
    divisor = base
    quotient = 1

    result = []

    while quotient != 0:
        # check if dividend(number) is less than divisor(base)
        # if true no need to devide. then divedend = remainder
        if dividend < divisor:
            remainder = dividend
            quotient = 0
        else:
            remainder = dividend % divisor
            # updating the dividend until it is less than devisor
            dividend = (dividend - remainder) // divisor

        # if remainder > 9:
        #     remainder = chr(remainder + hex_letter_offset)
        #     remainder = str(remainder)

        # result += str(remainder)
        result.append(str(remainder))

    return result


k = 1
base = 16
decimal = 987654321
(sum_of_squares(k, base, decimal))
