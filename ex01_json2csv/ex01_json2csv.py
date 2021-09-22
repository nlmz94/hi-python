import pandas as pd


def json_to_csv(file_path):
    new_data = pd.read_json(file_path)
    new_data.to_csv("generated_csv.csv", index=None)
