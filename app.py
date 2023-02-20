from main import download_eco_def, generate_data, combine_data, post_process
from initialise_ec_repo import pull_or_clone_ce, create_other_paths
from toml_file_generator import toml_field_generator
from aggregate_files import aggregate_files
from tqdm import tqdm


if __name__ == '__main__':
    pull_or_clone_ce()
    create_other_paths()
    for url in tqdm(toml_field_generator(r"/Users/jlee/PycharmProjects/ec/crypto-ecosystems/data/ecosystems")):
        eco_file = download_eco_def(url)
        generate_data(eco_file, limit=None)
        combine_data(eco_file, 'commits')
        combine_data(eco_file, 'authors')
        post_process(eco_file)

    aggregate_files(r"/Users/jlee/PycharmProjects/ec/")

