import pandas as pd

base_path = "/home/ubuntu/repos/electric_capital_pull/aggregated_outputs"


def read_file_and_pivot_table(filename: str):
    column_headers = ['second_index', 'Date', 'Value', 'Ecosystem']
    df = pd.read_csv(rf"{base_path}/{filename}")

    df.columns = column_headers
    df = pd.pivot_table(df, index='Date', columns=['Ecosystem'], values='Value', aggfunc=sum)
    sorted_columns = sorted(df.columns)

    return df[sorted_columns].copy()


def read_authors_file_and_pivot():
    df = pd.read_csv("authors.csv")
    df = df.groupby(by=['date', 'ecosystem']).count()
    df = df.reset_index()
    df.columns = ['Date', 'Ecosystem', 'n', 'Value']
    df = df[['Date', 'Ecosystem', 'Value']].copy()

    df = pd.pivot_table(df, index='Date', columns=['Ecosystem'], values='Value', aggfunc=sum)
    sorted_columns = sorted(df.columns)

    return df[sorted_columns].copy()


def pivot_main():
    read_file_and_pivot_table("authors_roll30.csv").to_csv(f"{base_path}/authors_roll30_pivot.csv")
    read_file_and_pivot_table("commits.csv").to_csv(f"{base_path}/commits_pivot.csv")
    read_authors_file_and_pivot().to_csv(f"{base_path}/authors_pivot.csv")


if __name__ == '__main__':
    pivot_main()
