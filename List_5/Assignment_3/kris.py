from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import secrets
import hashlib
import multiprocessing


def encrypt(key, iv, message):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(message)


def make_puzzles(start, end, c, k1, k2, const, n):
    iv_k1 = hashlib.sha256(k1).digest()[:16]
    iv_k2 = hashlib.sha256(k2).digest()[:16]
    puzzles = []
    for i in range(start, end+1):
        id = encrypt(k1, iv_k1, i.to_bytes(16, byteorder='big'))
        key = encrypt(k2, iv_k2, id)
        random_key = secrets.randbelow(c*n).to_bytes(16, byteorder='big')
        r_iv = hashlib.sha256(random_key).digest()[:16]
        puzzle = encrypt(random_key, r_iv, id + key +
                         const.to_bytes(16, byteorder='big'))
        puzzles.append(puzzle)
    return puzzles


def X(n, c):
    k1 = secrets.token_bytes(16)
    iv_k1 = hashlib.sha256(k1).digest()[:16]
    k2 = secrets.token_bytes(16)
    iv_k2 = hashlib.sha256(k2).digest()[:16]
    const = secrets.randbits(128)
    # puzzles = []
    if n % 4 == 0:
        pool = multiprocessing.Pool(processes=4)
        puzzles = pool.starmap(make_puzzles, [(1, n//4, c, k1, k2, const, n), (n//4 + 1, 2 * n // 4, c, k1, k2, const, n),
                                              (2 * n // 4 + 1, 3 * n // 4, c, k1, k2, const, n), (3 * n // 4 + 1, n, c, k1, k2, const, n)])

        def flatten(l): return [item for sublist in l for item in sublist]
        puzzles = flatten(puzzles)
        # print(len(puzzles))


def rand(bytes):
    with open("/dev/random", "rb") as random:
         value = random.read(bytes)
         return value


X(2**24, 2)
