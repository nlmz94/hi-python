from re import escape
import pandas as pd
import json
import csv


def json_to_csv_with_pandas(file_path):
    new_data = pd.read_json(file_path)
    new_data.to_csv("generated_csv.csv", index=None)


def json_to_csv_without_pandas(file_path):
    with open(file_path) as file_json:
        json_data = json.loads(file_json.read())
    new_csv_file = open('generated_csv_not_pandas.csv', 'wt')
    csv_writer = csv.writer(
        new_csv_file, escapechar='\n', quoting=csv.QUOTE_NONE)
    top_row = ''
    for key in json_data.keys():
        top_row += key + ';'
    csv_writer.writerow([top_row])
    for key in json_data.keys():
        normal_row = ''
        value_row = ''
        for sub_key in json_data[key].keys():
            normal_row += sub_key.strip(' ') + ';'
            value_row += json_data[key][sub_key].strip(' ') + ';'
        csv_writer.writerow([normal_row.strip(' ')])
        csv_writer.writerow([value_row.strip(' ')])
    new_csv_file.close()
