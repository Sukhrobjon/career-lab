"""
question from repl.it
https: // repl.it/student/submissions/7695405
"""


def is_prime(n):
    for curr_num in range(2, n):
        # if input is evenly divisible by the current number
        if n % curr_num == 0:
            return False
    return True

n = 10
print(is_prime(7))
