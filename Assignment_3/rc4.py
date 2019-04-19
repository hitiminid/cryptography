import random
import argparse
import math
import json
import subprocess
import os


def RC4(N, T, K, D, size):
    S = KSA(K, N, T)
    prga = PRGA(N, S)
    mdrop_gen = mdrop(prga, D)
    file_name = f'test_N={N}_T={T}_K={len(K)}_D={D}.bin'

    with open(file_name, 'wb') as f:
        frame = bytearray()

        for x, _ in zip(mdrop_gen, range(size)):
            frame.append(x)

        f.write(frame)


def KSA(K, N, T):
    S = [i for i in range(N)]
    L = len(K)
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


def mdrop(prga, D):
    while True:
        for _ in range(D):
            next(prga)
        yield next(prga)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', dest='mode', help='Mode 1) N 2) 2Nlog(N)', type=str, default='n')
    parser.add_argument('--N', dest='N', type=int, default=16)
    parser.add_argument('--key', dest='key_length', type=int, default=40)
    parser.add_argument('--D', dest='D', type=int, default=0)
    parser.add_argument('--size', type=int, default=10000000)
    return parser.parse_args()


def setup(K):
    arguments = parse_arguments()

    N = arguments.N
    T = N if arguments.mode == 'n' else 2 * N * math.log(N)
    K = K[:arguments.key_length]
    # K = [random.randint(0, N-1) for _ in range(arguments.key_length)] # key
    D = arguments.D
    size = arguments.size
    return N, int(T), K, D, size


def get_data():
    tests = {}
    with open("config.json") as f:
        tests = json.load(f)['data']  # N, len, D
    return tests


def run_tests(tests):
    script_path = './rc4.o'
    for test in tests:
        N, key_length, D = test['N'], test['key_length'], test['D']
        T = N

        # "./rc4.o %s %s %s %s" % (str(N), str(T), str(D), str(key_length))
        subprocess.call("./rc4.o %s %s %s %s" % (str(N), str(T), str(D), str(key_length)), shell=True)
        print(f'[INFO]: Test N={N}, len(K)={key_length}, D={D}, T={T} finished!')

        T = int(2 * N * math.log(N))
        subprocess.call("./rc4.o %s %s %s %s" %
                        (str(N), str(T), str(D), str(key_length)), shell=True)
        print(f'[INFO]: Test N={N}, len(K)={key_length}, D={D}, T={T} finished!')


def run_diehard():
    subprocess.call('./dieharder_auto', shell=True)


if __name__ == "__main__":
    tests = get_data()
    run_tests(tests)
    print('[INFO] Data generated. Dieharder starts')
    run_diehard()
    print('[INFO] Dieharder ended')


# K = [155, 240, 121, 136, 50, 170, 165, 101, 215, 193, 0, 182, 75, 193, 23, 159, 34, 12, 177, 172, 218, 211, 243, 197, 165, 11, 219, 14, 197, 27, 86, 120, 67, 65, 224, 24, 16, 109, 140, 15, 93, 10, 246, 15, 186, 29, 232, 217, 19, 116, 193, 53, 112, 60, 18, 82, 229, 75, 43, 113, 71, 6, 219, 129, 16, 69, 243, 66, 108, 55, 137, 91, 143, 248, 166, 5, 244, 222, 29, 204, 196, 226, 150, 6, 164, 159, 203, 30, 159, 30, 9, 56, 251, 230, 223, 74, 38, 38, 218, 189, 219, 244, 149, 39, 98, 111, 108, 33, 64, 253, 97, 5, 225, 65, 129, 49, 14, 38, 128, 20, 180, 227, 170, 123, 140, 138, 45, 218]
