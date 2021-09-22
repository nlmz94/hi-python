import sys

from ex00_ini2json import *


def main():
    ini_file = open(sys.argv[1], "r")
    print(ini_to_json(ini_file.read()))


if __name__ == '__main__':
    main()
