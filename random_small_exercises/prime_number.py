import time
import math


def is_prime_v1(n):
    """Naive version of finding if number is prime"""
    if n == 1:
        return False

    for devisor in range(2, n):
        if n % devisor == 0:
            return False
    return True


def is_prime_v2(n):
    """Version 2 of finding if number is prime
    it uses
    Runtime: O(sqrt(N))"""
    if n == 1:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for divisor in range(2, 1 + max_divisor):
        if n % divisor == 0:
            return False
    return True


def is_prime_v3(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for divisor in range(3, 1 + max_divisor, 2):
        if n % divisor == 0:
            return False
    return True

# ====== Test Function =====
start_time = time.time()
for n in range(1, 1000000):
    is_prime_v2(n)
end_time = time.time()
print("Time required: ", end_time - start_time)

# for n in range(1, 21):
#     print(n, is_prime_v3(n))
