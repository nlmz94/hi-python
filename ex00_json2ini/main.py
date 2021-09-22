import sys
import json

from ex00_json2ini import ini_to_json
from ex00_json2ini import json_to_ini


def main_ini_to_json():
    ini_file = open(sys.argv[1], "r")
    ini_to_json(ini_file.read())


def main_json_to_ini():
    ini_file = open(sys.argv[1], "r")
    json_data = json.load(ini_file)
    ini_file.close
    json_to_ini(json_data)


if __name__ == '__main__':
    # main_ini_to_json()
    main_json_to_ini()
