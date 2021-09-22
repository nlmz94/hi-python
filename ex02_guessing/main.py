import sys
from ex02_guessing import guess_number


def main():
    guess_number(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
