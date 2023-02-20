import os

base_path = r"/Users/jlee/PycharmProjects/ec"


def pull_or_clone_ce():
    if os.path.exists(f"{base_path}/crypto-ecosystems/"):
        cmd = f"cd {base_path}/crypto-ecosystems/ && git pull"
        os.system(cmd)
    else:
        crypto_ecosystems_url = "git@github.com:electric-capital/crypto-ecosystems.git"
        cmd = f"cd {base_path} && git clone {crypto_ecosystems_url}"
        os.system(cmd)


def create_other_paths():
    if not os.path.exists(f"{base_path}/eco"):
        os.mkdir(f"{base_path}/eco")

    if not os.path.exists(f"{base_path}/aggregated_outputs"):
        os.mkdir(f"{base_path}/aggregated_outputs")
