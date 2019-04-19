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
                             '-k', f'{passphrase}'
                             ]
        subprocess.check_output(open_ssl_commands)


def perform_decryption(ciphertexts, key_store_password):
    ciphertexts = ciphertexts if isinstance(
        ciphertexts, list) else [ciphertexts]
    messages = []

    passphrase = key_store_password

    for c in ciphertexts:
        echo_message = ['echo', '-n', f"{c}"]
        open_ssl_commands = ['openssl', 'enc',
                             '-aes-256-cbc',  '-nosalt',
                             '-k', f'{passphrase}',
                             ]

        ps = subprocess.Popen(echo_message, stdout=subprocess.PIPE)
        msg = subprocess.check_output(
            open_ssl_commands, stdin=ps.stdout)
        # ciphertext = ciphertext.decode('ascii', 'ignore')
        messages.append(msg)

    for m, c in zip(messages, ciphertexts):
        print(f'm:{m} c:{c}')

    return ciphertexts
