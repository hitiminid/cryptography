import random
import argparse
import math


def RC4(N, T, K, D):
    S = KSA(K, N, T)
    prga = PRGA(N, S)
    RC4_drop(prga, D)


def KSA(K, N, T):
    S = [i for i in range(N)]
    L = len(K) // 8
    j = 0

    for i in range(0, T+1):
        j = (j + S[i % N] + K[i % L]) % N
        S[j % N], S[i % N] = S[i % N], S[j % N]
    return S


def PRGA(N, S):
    i = 0
    j = 0

    while True:
        i = (i + 1) % N
        j = (j + S[i]) % N
        S[i], S[j] = S[j], S[i]
        Z = S[(S[i] + S[j]) % N]
        yield Z


def RC4_drop(prga, D):
    with open('output', 'a') as output:
        counter = 0
        for value in prga:
            if counter % (D + 1) == 0:
                line = f'{str(value)}\n'
                output.write(line)
            # print(str(value))

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', dest='mode', help='Mode 1) N 2) 2Nlog(N)', type=int, default = 1)
    parser.add_argument('--N', dest='N', type=int, default=16)
    parser.add_argument('--key', dest='key_length', default=40)
    parser.add_argument('--D', dest='D', type=int, default=0)
    return parser.parse_args()


def setup():
    arguments = parse_arguments()

    N = arguments.N
    T = N if arguments.mode == 0 else 2 * N * math.log(N)
    K = [random.randint(0, N) for _ in range(arguments.key_length)] # key
    D = arguments.D

    return N, int(T), K, D


N, T, K, D = setup()
import pdb; pdb.set_trace()

RC4(N, T, K, D)
