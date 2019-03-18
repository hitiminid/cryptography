import pdb
import functools
from math import gcd

class LCG:

    def __init__(self, seed, a, c, m):
        self._result = seed
        self._a = a
        self._c = c
        self._m = m

    def __iter__(self):
        return self

    def __next__(self):
        self._result = (self._result * self._a + self._c) % self._m
        return self._result


def crack_unknown_increment(data, modulus, multiplier):
    increment = (data[1] - data[0] * multiplier) % modulus
    return increment


def crack_unknown_multiplier(data, modulus):
    multiplier = (data[2] - data[1]) * modinv(data[1] - data[0], modulus) % modulus
    return crack_unknown_increment(data, modulus, multiplier)


def crack_unknown_increment_and_multiplier(modulus, data):
    first_difference = (data[2] - data[1]) % modulus
    second_difference = (data[1] - data[0]) % modulus

    multiplier = (first_difference * modinv(second_difference, modulus)) % modulus
    increment = crack_unknown_increment(data, modulus, multiplier)
    return multiplier, increment


def crack_unknown_all(data):
    diffs = [s1 - s0 for s0, s1 in zip(data, data[1:])]
    zeroes = [t2 * t0 - t1 * t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]

    modulus = abs(functools.reduce(gcd, zeroes))
    return crack_unknown_multiplier(data, modulus)


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def modinv(a, m) :
    a = a % m;

    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1


def generate_data(lcg, n):
    data = []
    for i in range(0, n):
        data.append(next(lcg))
    return data


def main(): 
    seed = 123
    a = 1103515245
    c = 12345
    m = 2**31

    lcg = LCG(seed, a, c, m)
    data = generate_data(lcg, 32)
    pdb.set_trace()

    crack_unknown_all(data)


main()

