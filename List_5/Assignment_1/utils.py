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