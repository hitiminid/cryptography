import secrets
import math

secretsGenerator = secrets.SystemRandom()
def sequence(num_of_elements):
    sequence = []
    # start = (((2**i)-1) * 2 ** num_of_elements) + 1
    for i in range(num_of_elements):
        start = (((2**i)-1) * 2 ** num_of_elements) + 1
        end = (2**i) * 2 ** num_of_elements
        sequence.append(secretsGenerator.randint(start, end))
    return sequence

# print(sequence(10)

def modulo(sequence):
    start = sum(sequence)
    modulo = secretsGenerator.randint(start + 1, 2**(2*(len(sequence) + 1))-1)
    return modulo

def gen_r(modulo):
    r = secretsGenerator.randint(2, modulo-2)
    while math.gcd(r, modulo) != 1:
        r = secretsGenerator.randint(2, modulo-2)
    return r

def private(n):
    seq = sequence(n)
    mod = modulo(seq)
    r = gen_r(mod)

    return seq, mod, r

def public_key(private):
    pub_key = [(element * private[2]) % private[1] for element in private[0]]
    return private, pub_key

def encrypt(message, pub_key):
    b = ''.join('{0:08b}'.format(ord(char), 'b') for char in message)
    ciper = sum([x if y == '1' else 0 for x, y in zip(pub_key, b)])
    return ciper

def egcd(a, b):
	if a == 0:
		return b, 0, 1
	else:
		g, x, y = egcd(b % a, a)
		return g, y - (b // a) * x, x

def modinv(b, n):
	g, x, _ = egcd(b, n)
	if g == 1:
		return x % n


def decrypt(c, private_key):
    r = private_key[2]
    modulo = private_key[1]
    inverse = modinv(r, modulo)

    c_prim = (c*inverse) % private_key[1]
    message = ''

    rev_sequence = private_key[0][::-1]
    
    for i in rev_sequence:
        if c_prim >= i:
            message = '1' + message
            c_prim -=i
        else: 
            message = '0' + message

    m = ''
    print(len(message))
    for i in range(0, len(message), 8):
        c = message[i: i+8]
        m += chr(int(c, 2))
    return m
    # return chr(int(message, 2)), c_prim

key = public_key(private(24))
enc = encrypt('abc', key[1])
dec = decrypt(enc, key[0])

print(enc, dec)