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
from generator import Generator
from client import Client
from solve import Solver


def init_constants():
    C = 2
    N = 2 ** 16
    CONSTANT = utils.get_random_bytes(16)

    K1 = secrets.token_bytes(16)
    K2 = secrets.token_bytes(16)
    return C, N, CONSTANT, K1, K2


def init_parties():
    return Generator(), Client(), Solver()


@utils.measure_time
def main():

    C, N, CONSTANT, K1, K2 = init_constants()

    gen = Generator()
    cl = Client()
    solver = Solver()

    puzzles = gen.perform_puzzle_generation(C, N, CONSTANT, K1, K2)

    random_puzzle = cl.pick_random_puzzle(puzzles)

    found_puzzle = solver.solve_puzzle(random_puzzle, C, N, CONSTANT)
    found_id = found_puzzle[:16]
    found_key = found_puzzle[16:32]

    iv = hashlib.sha256(str(found_id).encode()).digest()
    iv = iv[:16]
    k = utils.encrypt(found_id, K2, iv)

    assert k == found_key


if __name__ == "__main__":
    main()

