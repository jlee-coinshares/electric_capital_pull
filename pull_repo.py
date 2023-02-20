import pandas as pd
import os

base_path = "/"


class repository_item:

    def __init__(self, repository_address: str):
        self.repository_address = repository_address

    @property
    def address_to_clone(self):
        return f"git@github.com:{self.repository_address.replace('https://github.com/', '')}.git"

    @property
    def get_org_name(self):
        return self.repository_address.split("/")[-2]

    def is_repo_on_github(self):
        if not self.repository_address.startswith("https://github.com/"):
            return False
        return True

    @property
    def get_repo_name(self):
        return self.repository_address.split("/")[-1]


def clone_repo(repo_path, repo_org, clone_addr):
    if not os.path.exists(repo_path):
        os.makedirs(repo_path, exist_ok=True)
        cmd = f'cd {repo_org} && git clone --bare {clone_addr} >/dev/null 2>&1'
        os.system(cmd)

    else:
        if not os.path.exists(f'{repo_path}'):
            return pd.DataFrame([])
        cmd = f'cd {repo_path} && git pull >/dev/null 2>&1'
        os.system(cmd)
