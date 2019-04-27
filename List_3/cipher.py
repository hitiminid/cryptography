import subprocess
import key_store
import pdb


def perform_encryption(messages, keystore_data, is_text_encryption):

    messages = messages if isinstance(messages, list) else [messages]

    key = key_store.get_password(
        keystore_data.path, keystore_data.password, keystore_data.key_identifier)
    if is_text_encryption:
        return encrypt_text(messages, keystore_data.encryption_mode, key)
    else:
        return encrypt_files(messages, keystore_data.encryption_mode, key)


def encrypt_text(plaintexts, encryption_mode, key):

    ciphertexts = []

    for message in plaintexts:

        echo_message = ['echo', '-n', f"{message}"]
        open_ssl_commands = ['openssl', 'enc',
                             f'{encryption_mode}', '-nosalt',
                             '-k', f'{key}'
                             ]

        ps = subprocess.Popen(echo_message, stdout=subprocess.PIPE)
        ciphertext = subprocess.check_output(
            open_ssl_commands, stdin=ps.stdout)
        # ciphertext = ciphertext.decode('ascii', 'ignore')
        ciphertexts.append(ciphertext)
    print(ciphertexts)
    # pdb.set_trace()

    return ciphertexts


def encrypt_files(file_paths, encryption_mode, key, challenge):

    if challenge:

        for path in file_paths:
            open_ssl_commands = ['openssl', 'enc',
                                 f'{encryption_mode}', '-nosalt',
                                 '-K', f'{key}',
                                 '-in', f'{path}',
                                 'out', f'challenge.enc'
                                 ]
            subprocess.check_output(open_ssl_commands)

    else:
        for path in file_paths:
            open_ssl_commands = ['openssl', 'enc',
                                 f'{encryption_mode}', '-nosalt',
                                 '-K', f'{key}',
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
