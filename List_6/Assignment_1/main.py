import functools
import pdb
import subprocess


def save_to_file(file_name, content):
    pass


def extract_public_key():
    command = 'openssl x509 -pubkey -noout -in cacertificate.pem'
    public_key = subprocess.check_output(['bash', '-c', command])
    save_to_file('cacertificate_pk.pem', public_key)
    return public_key


def extract_rsa_data():
    command = 'openssl rsa -pubin -in cacertificate_pubkey.pem -text -noout'
    rsa_data = subprocess.check_output(['bash', '-c', command])
    save_to_file('rsa_data', rsa_data)
    return rsa_data.decode().split('\n')


def extract_modulus(rsa_data):
    modulus = rsa_data[2:6]
    joined_modulus = functools.reduce(
        lambda acc, x: acc + x.strip(), modulus, '')
    hex_modulus = joined_modulus.replace(':', '')
    return str(int(hex_modulus, 16))


def compute_p_and_q(modulus):
    command = f'~/Utilities/CADO-NFS/cado-nfs.py {modulus}'
    pdb.set_trace()
    result = subprocess.check_output(['bash', '-c', command])
    # return p, q


def main():
    public_key = extract_public_key()
    rsa_data = extract_rsa_data()
    modulus = extract_modulus(rsa_data)
    # modulus = '90377629292003121684002147101760858109247336549001090677693'
    compute_p_and_q(modulus)

    pdb.set_trace()


if __name__ == '__main__':
    main()
