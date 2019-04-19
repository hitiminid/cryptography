import subprocess


def perform_encryption(messages, encryption_mode, key_store_password, is_text_encryption):
    messages = messages if isinstance(messages, list) else [messages]

    if is_text_encryption:
        encrypt_text(messages, encryption_mode, key_store_password)
    else:
        encrypt_files(messages, encryption_mode, key_store_password)


def encrypt_text(plaintexts, encryption_mode, passphrase):

    ciphertexts = []

    for message in plaintexts:

        echo_message = ['echo', '-n', f"{message}"]
        open_ssl_commands = ['openssl', 'enc',
                             f'{encryption_mode}', '-nosalt',
                             '-k', f'{passphrase}'
                             ]

        ps = subprocess.Popen(echo_message, stdout=subprocess.PIPE)
        ciphertext = subprocess.check_output(
            open_ssl_commands, stdin=ps.stdout)
        # ciphertext = ciphertext.decode('ascii', 'ignore')
        ciphertexts.append(ciphertext)

    # for m, c in zip(messages, ciphertexts):
    #     print(f'm:{m} c:{c}')

    return ciphertexts


def encrypt_files(file_paths, encryption_mode, passphrase):

    for path in file_paths:
        open_ssl_commands = ['openssl', 'enc',
                             f'{encryption_mode}', '-nosalt',
                             '-k', f'{passphrase}',
                             '-in', f'{path}',
                             'out', f'{path}.enc'
                             ]
        subprocess.check_output(open_ssl_commands)


##### DECRYPTION #####

def perform_decryption(ciphertexts, encryption_mode, key_store_password):
    # messages = messages if isinstance(messages, list) else [messages]

    # if is_text_encryption:
    #     encrypt_text(messages, encryption_mode, key_store_password)
    # else:
    decrypt_files(ciphertexts, encryption_mode, key_store_password)


def decrypt_text():
    raise NotImplementedError


def decrypt_files(file_paths, encryption_mode, passphrase):

    for path in file_paths:
        open_ssl_commands = ['openssl', 'enc',
                             f'{encryption_mode}', '-nosalt',
                             '-k', f'{passphrase}',
                             '-in', f'{path}',
                             '-out', f'{path}.dec'
                             ]
        output = subprocess.check_output(open_ssl_commands)
