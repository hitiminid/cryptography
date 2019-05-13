import pdb
import math 
import secrets
import functools
# import dataclass

import utils


secretGenerator = secrets.SystemRandom()		

def generate_private_key(n): 
	sequence = generate_sequence(n)
	modulo = generate_modulo(sequence)
	r = generate_r(modulo)
	return (sequence, modulo, r)

def generate_sequence(n):
	sequence = []

	for i in range(n):
		lower_bound = (((2**i)-1) * 2 ** n) + 1
		upper_bound = (2**i) * 2 ** n
		element = secretGenerator.randint(lower_bound, upper_bound)
		sequence.append(element)
	return sequence


def generate_modulo(sequence):
	# sequence_sum = functools.reduce(lambda acc, y : acc + y, sequence)
	sequence_sum = sum(sequence)

	lower_bound = sequence_sum + 1 
	upper_bound = 2 ** (2 * (len(sequence) + 1)) - 1
	modulo = secretGenerator.randint(lower_bound, upper_bound)

	return modulo

def generate_r(modulo):
	r = secretGenerator.randint(2, modulo-2)

	while math.gcd(r, modulo) != 1:
		r = secretGenerator.randint(2, modulo-2)		

	return r 


def generate_public_key(private_key):
	sequence = private_key[0]
	modulo = private_key[1]
	r = private_key[2]
	
	public_key = [(element * r) % modulo for element in sequence]	
	return public_key


def encrypt(message, public_key):
	bits = ''.join('{0:08b}'.format(ord(char), 'b') for char in message)
	elements = [number if bit == "1" else 0 for number, bit in zip(public_key, bits)]
	return sum(elements)


def decrypt(ciphertext, private_key):
	
	sequence, modulo, r = private_key[0], private_key[1], private_key[2]

	inverse = utils.modinv(r, modulo)
	cs = (ciphertext * inverse) % modulo

	message = ''

	reversed_sequence = sequence[::-1]


	for i in reversed_sequence:
		if cs >= i: 
			message = '1' + message
			cs -= i
		else: 
			message = '0' + message
	print(message)

	msg = ''


	for char in range(0, len(message), 8):
		c = message[char:char+8]
		m = chr(int(c,2))
		msg += m

	return msg

def main(): 
	while True:
		private_key = generate_private_key(24)
		public_key = generate_public_key(private_key)

		msg = 'abc'
		enc = encrypt(msg, public_key)
		dec = decrypt(enc, private_key)
		print(f'enc = {enc}, dec = {dec}')
		assert msg == dec


if __name__ == "__main__":
	main()