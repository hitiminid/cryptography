import sys
import tempfile
import subprocess
import pdb
import pathlib

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


file_name = 'config'

# 1385409854850246784644682622624349784560468558795524903
# 1524938362073628791222322453937223798227099080053904149

p = 1385409854850246784644682622624349784560468558795524903
q = 1524938362073628791222322453937223798227099080053904149
n = p * q
e = 65537
d = modinv(e, (p-1) * (q-1))

e1 = d % (p-1)
e2 = d % (q-1)

coeff = modinv(q, p)


def generate_private_key():
    content = f"""asn1=SEQUENCE:rsa_key

[rsa_key]
version=INTEGER:0
modulus=INTEGER:{n}
pubExp=INTEGER:{e}
privExp=INTEGER:{d}
p=INTEGER:{p}
q=INTEGER:{q}
e1=INTEGER:{e1}
e2=INTEGER:{e2}
coeff=INTEGER:{coeff}"""

    print(content + '\n' * 5)

    with tempfile.NamedTemporaryFile() as f:
        f.write(content.encode())
        f.flush()
        commands = [
            'bash', '-c', f'openssl asn1parse -genconf {f.name} -out newkey.der']
        output = subprocess.check_output(commands)

        commands = ['bash', '-c',
                    'openssl rsa -in newkey.der -inform der -text -check']
        output = subprocess.check_output(commands)
        print(output.decode())

    decoded_output = output.decode().split('\n')
    priv_key_starting_index = decoded_output.index(
        '-----BEGIN RSA PRIVATE KEY-----')
    private_key = decoded_output[priv_key_starting_index:]
    private_key = '\n'.join(private_key)

    pathlib.Path('my_priv_key').write_text(private_key)


def legit_forge_signature():
    command = 'openssl dgst -md5 -sign my_priv_key -out better_grade.sign better_grade.txt'
    rsa_data = subprocess.check_output(['bash', '-c', command])


def verify():
    command = 'openssl dgst  -md5 -verify cacertificate_pubkey.pem -signature better_grade.sign better_grade.txt'
    response = subprocess.check_output(['bash', '-c', command])
    print(response)


generate_private_key()
legit_forge_signature()
verify()
