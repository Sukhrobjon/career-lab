def fizzbuzz(n):
    """Given an input, print all numbers up to and including that input,
    unless they are divisible by 3, then print "fizz" instead, or if they
    are divisible by 5, print "buzz". If the number is divisible by both,
    print "fizzbuzz".
    """
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

n = 7

fizzbuzz(n)