import json

import pandas as pd


def json_to_csv_with_pandas(file_path):
    new_data = pd.read_json(file_path)
    new_data.to_csv("generated_csv.csv", index=None)


def json_to_csv_without_pandas(file_path):
    with open(file_path) as file:
        file_dictionary = json.load(file)
        file_header = ''
        file_data = ''
        for key, item in file_dictionary.items():
            file_header += key + ';'
            file_data += json.dumps(item).strip() + ';'
        with open('generated_csv_not_pandas.csv', 'w', newline='') as csvfile:
            csvfile.write(file_header + '\n')
            csvfile.write(file_data + '\n')
