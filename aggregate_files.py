import pandas as pd
import os


def aggregate_files(base_path: str):
    for csv_file in os.listdir(f"{base_path}/outputs"):
        eco_name = csv_file.split("_")[0]
        temp = pd.read_csv(os.path.join(f"{base_path}/outputs", csv_file))
        if not temp.empty:
            temp['ecosystem'] = eco_name

            column = csv_file.replace(".csv", "").replace(f"{eco_name}_", "")
            output_path = f"{base_path}/aggregated_outputs/{column}.csv"

            temp.to_csv(output_path, mode="a", header=not os.path.exists(output_path))


if __name__ == '__main__':
    aggregate_files(r"/Users/jlee/PycharmProjects/ec/")
