from time import time
import pdb
import random
import hashlib
import secrets
import multiprocessing
import itertools

import utils
import generator
import solve

# TODO: change to generate variable length chunks


def main():
    C = 1
    N = 2 ** 5
    CONSTANT = utils.get_random_bytes(16)

    K1 = secrets.token_bytes(16)
    K2 = secrets.token_bytes(16)

    start = time()
    NUMBER_OF_CORES = multiprocessing.cpu_count()

    if N % NUMBER_OF_CORES == 0:
        pool = multiprocessing.Pool(processes=NUMBER_OF_CORES)
        chunks = create_chunks(N)

        pool_data = [
            (chunks[0], C, N, CONSTANT, K1, K2),
            (chunks[1], C, N, CONSTANT, K1, K2),
            (chunks[2], C, N, CONSTANT, K1, K2),
            (chunks[3], C, N, CONSTANT, K1, K2),
        ]

        puzzles = pool.starmap(generator.generate_puzzles, pool_data)
        puzzles = list(itertools.chain(*puzzles))

    end = time()

    print(f"Generating took {end-start}")

    random_puzzle = pick_random_puzzle(puzzles)

    found_puzzle = solve.solve_puzzle(random_puzzle, C, N, CONSTANT)
    found_id = found_puzzle[:16]
    found_key = found_puzzle[16:32]

    iv = hashlib.sha256(str(found_id).encode()).digest()
    iv = iv[:16]
    k = utils.encrypt(found_id, K2, iv)

    assert k == found_key


def create_chunks(n):
    chunks = [
        (1, (n // 4) + 1),
        (n // 4 + 1, (2 * n // 4) + 1),
        (2 * n // 4 + 1, (3 * n // 4) + 1),
        (3 * n // 4 + 1, n + 1),
    ]
    return chunks


def pick_random_puzzle(puzzles):
    return puzzles[random.randint(0, len(puzzles) - 1)]


if __name__ == "__main__":
    main()
