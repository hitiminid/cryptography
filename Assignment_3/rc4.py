

def RC4(K, N, T):
    S = KSA(K, N, T)
    prga = PRGA(N, S)
    save_output_to_file(prga)


def KSA(K, N, T):

    S = [i for i in range(N)]
    L = len(K) // 8
    j = 0

    for i in range(0, T):
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


def save_output_to_file(prga):
    with open(file_name, 'a') as output:
        for value in prga:
            line = f'{str(value)}\n'
            output.write(line)

file_name = 'output'

K = [1,2,3,4,5,6,7,8]
N = 256
T = 256

RC4(K, N, T)
