import arguments
import challenge
import oracle
import keyring

ARGS = arguments.get_arguments()


def main():
    if ARGS['type'] == 'oracle':
        oracle.run()
    else:
        challenge.run()


if __name__ == '__main__':
    main()
