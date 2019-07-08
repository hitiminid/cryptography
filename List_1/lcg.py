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


def solve_unknown_increment(data, modulo, multiplier):
    increment = (data[1] - data[0] * multiplier) % modulo
    return modulo, multiplier, increment


def solve_unknown_multiplier(data, modulo):
    multiplier = (data[2] - data[1]) * modinv(data[1] - data[0], modulo) % modulo
    return solve_unknown_increment(data, modulo, multiplier)


def solve_unknown_all(data):
    differences = [former - latter for former, latter in zip(data, data[1:])]
    zeroes = [t2 * t0 - t1 * t1 for t0, t1, t2 in zip(differences, differences[1:], differences[2:])]

    modulo = abs(functools.reduce(gcd, zeroes))
    return solve_unknown_multiplier(data, modulo)


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

    # breakpoint()
    modulo, multiplier, increment = solve_unknown_all(data)
    perform_test(lcg, multiplier, increment, modulo, data)

if __name__ == '__main__':
    main()

