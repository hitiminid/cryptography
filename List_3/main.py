import pdb

import arguments
import challenge
import oracle
import keyring
from keystore_data import KeyStoreData

ARGS = arguments.get_arguments()


def main():
    keystore_data = KeyStoreData(
        key_identifier=ARGS['key_id'],
        path=ARGS['key_store'],
        password=ARGS['key_store_password'],
        encryption_mode=ARGS['enc_mode']
    )

    if ARGS['type'] == 'oracle':
        oracle.run(keystore_data)
    else:
        challenge.run(keystore_data)


if __name__ == '__main__':
    main()
    # import subprocess
    # message = 'ala ma kota'
    # b = bytes(message, 'utf-8')

    # open_ssl_commands = ['openssl', 'enc',
    #                      '-aes-256-cbc', '-nosalt',
    #                      '-k', 'f5746ab5a66e86da6cbf79c9878bff04'
    #                      ]
    # plaintext = subprocess.check_output(open_ssl_commands,
    #                                     input=b)

    # # ps = subprocess.Popen(echo_message, stdout=subprocess.PIPE)
    # # ciphertext = subprocess.check_output(open_ssl_commands, stdin=ps.stdout)

    # print(plaintext)
    # pdb.set_trace()
    # open_ssl_commands = ['openssl', 'enc', '-d',
    #                      '-aes-256-cbc', '-nosalt',
    #                      '-k', 'f5746ab5a66e86da6cbf79c9878bff04'
    #                      ]
    # plaintext = subprocess.check_output(open_ssl_commands,
    #                                     input=plaintext)
    # print(plaintext)
