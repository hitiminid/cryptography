import random
import pdb
import hashlib
from Crypto.Cipher import AES
import secrets


CONSTANT = 1
C = 1
N = 16


def get_random_int(no_of_bytes):
    with open("/dev/random", "rb") as f:
        return f.read(no_of_bytes).hex()


def encrypt(message, key, iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(message)


def generate_puzzles(N: int):
    K1 = secrets.token_bytes(16)
    K2 = secrets.token_bytes(16)

    puzzles = []

    for i in range(N):
        puzzle = generate_puzzle(i, K1, K2)
        puzzles.append(puzzle)
        if i % 1000000 == 0:
            print('chuj')

    # puzzles = [generate_puzzle(i, K1, K2) for i in range(N)]
    return puzzles


def generate_puzzle(i, K1, K2):
    iv = hashlib.sha256(str(i).encode()).digest()
    iv = iv[:16]
    i = i.to_bytes(16, byteorder='big')
    # pdb.set_trace()

    puzzle_id = encrypt(i, K1, iv)

    iv = hashlib.sha256(str(puzzle_id).encode()).digest()
    iv = iv[:16]

    puzzle_key = encrypt(puzzle_id, K2, iv)

    random_key = get_random_integer(C * N)
    random_key = random_key.to_bytes(16, byteorder='big')

    puzzle_body = puzzle_id + puzzle_key + \
        CONSTANT.to_bytes(16, byteorder="big")

    iv = hashlib.sha256(puzzle_body).digest()
    iv = iv[:16]
    puzzle = encrypt(puzzle_body, random_key, iv)
    return puzzle


def get_random_integer(rng):
    return secrets.SystemRandom().randrange(1, rng)


def main():
    puzzles = generate_puzzles(2**24)
    print(puzzles)
    # while True:
    # print(get_random_integer(N))
    # pass
    # mode = AES.MODE_CBC
    # key = get_random_int(8)
    # iv = get_random_int(8)
    # message = "The answer is no"
    # pass
    # ciphertext = encrypt(message, mode, key, iv)
    # obj2 = AES.new(key, AES.MODE_CBC, iv)
    # print(obj2.decrypt(ciphertext))


if __name__ == "__main__":
    main()


# def init():
#     K1 = random()
#     K2 = random()
#     C = random()
#     return K1, K2, C

# def encrypt(key: str, *args):
#     message = ''.join([arg for arg in args])
#     ciphertext = perform_encryption(key, message)
#     # pdb.set_trace()

# # encrypt(1, 'a', 'b', 'c')

# def generate_puzzles(number_of_puzzles, K1, K2):
#     # K1, K2

#     for i in range(number_of_puzzles):
#         ID = encrypt(K1, i)
#         key = encrypt(K2, ID)

#         # random_key = rand range c*n
#         puzzle = encrypt(random_key, ID, key, constant)


# def generate_ids():
#     pass
