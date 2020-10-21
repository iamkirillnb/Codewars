from math import sqrt
from itertools import count, islice

def is_prime(num):
    return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))