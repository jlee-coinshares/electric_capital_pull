import os
import json

with open("eco_list.json", "r") as f:
    list_of_ecos = json.loads(f.read())


def toml_field_generator(path_of_toml_files):
    for ecosystems_by_numbers in os.listdir(path_of_toml_files):

        for toml_file_parser in os.listdir(f"{path_of_toml_files}/{ecosystems_by_numbers}"):
            if toml_file_parser.replace(".toml", "") in list_of_ecos:
                yield f"https://raw.githubusercontent.com/electric-capital/crypto-ecosystems/master/data/ecosystems/{toml_file_parser[0]}/{toml_file_parser}"
