import sys

from ex01_json2csv import json_to_csv_with_pandas
from ex01_json2csv import json_to_csv_without_pandas


def main_json_to_csv():
    # json_to_csv_with_pandas(sys.argv[1])
    json_to_csv_without_pandas(sys.argv[1])


if __name__ == '__main__':
    main_json_to_csv()
