import random
import pdb
import hashlib
from Crypto.Cipher import AES
import secrets

import utils


def generate_puzzles(rng, c: int, n: int, con: int, K1, K2):
    global C, N, CONSTANT
    C = c
    N = n
    CONSTANT = con
    puzzles = []

    start, end = rng[0], rng[1]

    for i in range(start, end):
        puzzle = generate_puzzle(i, K1, K2)
        puzzles.append(puzzle)
        if i % 1000000 == 0:
            print("Million")

    return puzzles


# def generate_puzzles(c: int, n: int, con: int, K1, K2):
#     global C, N, CONSTANT
#     C = c
#     N = n
#     CONSTANT = con
#     puzzles = []

#     for i in range(N):
#         puzzle = generate_puzzle(i, K1, K2)
#         puzzles.append(puzzle)
#         if i % 1000000 == 0:
#             print('Million')

#     return puzzles


def generate_puzzle(i, K1, K2):
    iv = hashlib.sha256(str(i).encode()).digest()
    iv = iv[:16]
    i = i.to_bytes(16, byteorder="big")

    puzzle_id = utils.encrypt(i, K1, iv)

    iv = hashlib.sha256(str(puzzle_id).encode()).digest()
    iv = iv[:16]

    puzzle_key = utils.encrypt(puzzle_id, K2, iv)

    random_key = utils.get_random_integer(C * N)
    random_key = random_key.to_bytes(16, byteorder="big")

    puzzle_body = puzzle_id + puzzle_key + CONSTANT
    puzzle = utils.encrypt(puzzle_body, random_key, CONSTANT)
    return puzzle
