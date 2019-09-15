"""
question from repl.it
https: // repl.it/student/submissions/7695405
"""


def is_prime(n):
    """Determine if input number is prime number
    Args:
        n(int): input number
    Return:
        true or false(bool):
    """
    # 1 is not prime
    if n == 1:
        return False

    for curr_num in range(2, n):
        # if input is evenly divisible by the current number
        if n % curr_num == 0:
            # print("current num:", curr_num)
            return False
    return True


def count_primes(n):
    """Counts number of prime numbers less than a non-negative number, n"""
    count = 0
    for curr_num in range(2, n):
        # check if current number is prime
        if is_prime(curr_num):
            print(curr_num)
            count += 1
    return count

n = 2
m = 10
print("is prime:", is_prime(m))
print("num of primes:", count_primes(m))
