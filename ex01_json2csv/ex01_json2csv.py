from re import escape
import pandas as pd
import json


def json_to_csv_with_pandas(file_path):
    new_data = pd.read_json(file_path)
    new_data.to_csv("generated_csv.csv", index=None)


def json_to_csv_without_pandas(file_path):
    with open(file_path) as file:
        filedictionary = json.load(file)
        fileheader = ''
        filedata = ''
        for key, item in filedictionary.items():
            fileheader += key + ';'
            filedata += json.dumps(item).strip() + ';'
        with open('generated_csv_not_pandas.csv', 'w', newline='') as csvfile:
            csvfile.write(fileheader + '\n')
            csvfile.write(filedata + '\n')
