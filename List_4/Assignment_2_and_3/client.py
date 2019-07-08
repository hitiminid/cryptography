import random
from Crypto.Cipher import AES
import pdb

import generator
import utils


class Client:

    def pick_random_puzzle(self, puzzles):
        return puzzles[random.randint(0, len(puzzles) - 1)]

    @utils.measure_time
    def solve_puzzle(self, puzzle, C, N, CONSTANT):

        # key length, 16 bytes
        number_of_keys = C * N
        c = None

        for i in range(number_of_keys):

            # generate key
            key = i.to_bytes(16, byteorder="big")

            # decrypt message
            aes = AES.new(key, AES.MODE_CBC, CONSTANT)
            plaintext = aes.decrypt(puzzle)

            if plaintext[-16:] == CONSTANT:
                return plaintext
