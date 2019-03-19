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


def crack_unknown_increment(data, modulo, multiplier):
    increment = (data[1] - data[0] * multiplier) % modulo
    return modulo, multiplier, increment


def crack_unknown_multiplier(data, modulo):
    multiplier = (data[2] - data[1]) * modinv(data[1] - data[0], modulo) % modulo
    return crack_unknown_increment(data, modulo, multiplier)


def crack_unknown_increment_and_multiplier(modulo, data):
    first_difference = (data[2] - data[1]) % modulo
    second_difference = (data[1] - data[0]) % modulo

    multiplier = (first_difference * modinv(second_difference, modulo)) % modulo
    _, _, increment = crack_unknown_increment(data, modulo, multiplier)
    return multiplier, increment


def crack_unknown_all(data):
    diffs = [s1 - s0 for s0, s1 in zip(data, data[1:])]
    zeroes = [t2 * t0 - t1 * t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]

    modulo = abs(functools.reduce(gcd, zeroes))
    return crack_unknown_multiplier(data, modulo)


# def egcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         g, x, y = egcd(b % a, a)
#         return g, y - (b // a) * x, x


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


def perform_test(lcg, multiplier, increment, modulo, data):
    first_a = ((data[-1] * multiplier) + increment) % modulo 
    a = next(lcg)   

    breakpoint()

    assert a == first_a


def main(): 
    seed = 123
    a = 1103515245
    c = 12345
    m = 2**31

    lcg = LCG(seed, a, c, m)
    data = generate_data(lcg, 32)

    breakpoint()
    modulo, multiplier, increment = crack_unknown_all(data)
    perform_test(lcg, multiplier, increment, modulo, data)

main()

