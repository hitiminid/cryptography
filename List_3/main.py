import pdb

import arguments
import challenge
import oracle
import keyring
from keystore_data import KeyStoreData

ARGS = arguments.get_arguments()


def main():
    keystore_data = KeyStoreData(
        key_identifier=ARGS["key_id"],
        path=ARGS["key_store"],
        password=ARGS["key_store_password"],
        encryption_mode=ARGS["enc_mode"],
    )

    if ARGS["type"] == "oracle":
        oracle.run(keystore_data)
    else:
        challenge.run(keystore_data)


if __name__ == "__main__":
    main()

