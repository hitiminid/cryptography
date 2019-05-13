import generator
from Crypto.Cipher import AES
import utils
import pdb


def solve_puzzle(puzzle, C, N, CONSTANT):
    # key length, 16 bytes
    number_of_keys = C * N
    c = None

    for i in range(number_of_keys):

        # generate key
        key = i.to_bytes(16, byteorder='big')

        # decrypt message
        aes = AES.new(key, AES.MODE_CBC, CONSTANT)
        plaintext = aes.decrypt(puzzle)

        if plaintext[-16:] == CONSTANT:
            return plaintext

    # pdb.set_trace()
