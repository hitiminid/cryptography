import random
import pdb
import hashlib
from Crypto.Cipher import AES
import secrets
import itertools
import multiprocessing

import utils


class Generator:

    NUMBER_OF_CORES = multiprocessing.cpu_count()

    @utils.measure_time
    def perform_puzzle_generation(self, c: int, n: int, con: int, K1, K2):
        global C, N, CONSTANT
        C = c
        N = n
        CONSTANT = con
        puzzles = []

        if N % self.NUMBER_OF_CORES == 0:
            pool = multiprocessing.Pool(processes=self.NUMBER_OF_CORES)
            chunks = utils.generate_chunks(N, self.NUMBER_OF_CORES)

            pool_data = [(chunk, C, N, CONSTANT, K1, K2) for chunk in chunks]

            puzzles = pool.starmap(self.generate_puzzles, pool_data)
            puzzles = list(itertools.chain(*puzzles))

        return puzzles

    def generate_puzzles(self, rng, c: int, n: int, con: int, K1, K2):

        puzzles = []
        start, end = rng[0], rng[1]

        for i in range(start, end):
            puzzle = self.generate_puzzle(i, K1, K2)
            puzzles.append(puzzle)
            if i % 1000000 == 0:
                print("Million")
        return puzzles

    def generate_puzzle(self, i, K1, K2):
        iv = hashlib.sha256(str(i).encode()).digest()
        iv = iv[:16]
        i = i.to_bytes(16, byteorder="big")

        puzzle_id = utils.encrypt(i, K1, iv)

        iv = hashlib.sha256(str(puzzle_id).encode()).digest()
        iv = iv[:16]

        puzzle_key = utils.encrypt(puzzle_id, K2, iv)

        # random_key = C * N // 2
        random_key = utils.get_random_integer(C * N)
        random_key = random_key.to_bytes(16, byteorder="big")

        puzzle_body = puzzle_id + puzzle_key + CONSTANT
        puzzle = utils.encrypt(puzzle_body, random_key, CONSTANT)
        return puzzle
