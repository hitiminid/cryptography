from time import time
from Crypto.Cipher import AES
import secrets


def get_random_bytes(no_of_bytes):
    with open("/dev/random", "rb") as f:
        return f.read(no_of_bytes)


def get_random_integer(rng):
    return secrets.SystemRandom().randrange(1, rng)


def encrypt(message, key, iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(message)


def measure_time(func):
    def inner(*args, **kwargs):
        start_time = time()
        result = func(*args)
        end_time = time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time} seconds")
        return result

    return inner


def generate_chunks(n: int, number_of_chunks: int):
    start = 1
    end = (n // number_of_chunks) + 1

    chunks = [(start, end)]

    for i in range(1, number_of_chunks):
        start = i * n // number_of_chunks + 1
        end = (i + 1) * n // number_of_chunks + 1
        chunks.append((start, end))
    return chunks
