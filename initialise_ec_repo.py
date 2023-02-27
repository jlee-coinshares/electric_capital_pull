import os


def pull_or_clone_ce(base_path: str):
    if os.path.exists(f"{base_path}/crypto-ecosystems/"):
        cmd = f"cd {base_path}/crypto-ecosystems/ && git pull"
        os.system(cmd)
    else:
        crypto_ecosystems_url = "git@github.com:electric-capital/crypto-ecosystems.git"
        cmd = f"cd {base_path} && git clone {crypto_ecosystems_url}"
        os.system(cmd)


def create_other_paths(base_path: str):
    if not os.path.exists(f"{base_path}/eco"):
        os.mkdir(f"{base_path}/eco")

    if not os.path.exists(f"{base_path}/aggregated_outputs"):
        os.mkdir(f"{base_path}/aggregated_outputs")

    """if os.path.exists(f"{base_path}/repos"):
        cmd = f"rm -rf {base_path}/repos && mkdir {base_path}/repos"
        os.system(cmd)"""

