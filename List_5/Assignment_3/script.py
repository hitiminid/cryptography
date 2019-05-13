import pdb

def init():
    K1 = random()
    K2 = random()
    C = random()
    return K1, K2, C

def encrypt(key: str, *args):
    message = ''.join([arg for arg in args])
    ciphertext = perform_encryption(key, message)
    # pdb.set_trace()


# encrypt(1, 'a', 'b', 'c')

def generate_puzzles(number_of_puzzles, K1, K2):
    # K1, K2

    for i in range(number_of_puzzles):
        ID = encrypt(K1, i)
        key = encrypt(K2, ID)

        # random_key = rand range c*n
        puzzle = encrypt(random_key, ID, key, constant)


def generate_ids():
    pass



def get_random_int(no_of_bytes):
    with open("/dev/random", "rb") as f:
        value = f.read(no_of_bytes)
        return int.from_bytes(value, byteorder='big')
