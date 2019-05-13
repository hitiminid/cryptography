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
