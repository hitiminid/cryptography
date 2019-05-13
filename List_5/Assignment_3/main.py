import pdb
import random

import utils
import generator
import solve
import hashlib
import secrets


def main():
    C = 1
    N = 2**2
    CONSTANT = utils.get_random_bytes(16)

    K1 = secrets.token_bytes(16)
    K2 = secrets.token_bytes(16)
    # CONSTANT = CONSTANT.to_bytes(16, byteorder="big")

    # TODO: move C out of generator
    puzzles = generator.generate_puzzles(C, N, CONSTANT, K1, K2)
    # pdb.set_trace()

    random_puzzle = pick_random_puzzle(puzzles)

    found_puzzle = solve.solve_puzzle(random_puzzle, C, N, CONSTANT)
    found_id = found_puzzle[:16]
    found_key = found_puzzle[16:32]

    iv = hashlib.sha256(str(found_id).encode()).digest()
    iv = iv[:16]
    k = utils.encrypt(found_id, K2, iv)

    assert k == found_key

    # pdb.set_trace()
    # assert random_puzzle == solution


def pick_random_puzzle(puzzles):
    return puzzles[random.randint(0, len(puzzles)-1)]


if __name__ == "__main__":
    main()
