import glob
import os
import pandas as pd
import requests
import tomli
from concurrent.futures import ProcessPoolExecutor
from ratelimit import limits, sleep_and_retry
from tqdm import tqdm
from pull_repo import repository_item, clone_repo

sep = ';'


def fetch_repo(repo_addr):
    repo_item = repository_item(repo_addr)
    org_name = repo_item.get_org_name
    repo_name = repo_item.get_repo_name
    clone_addr = repo_item.address_to_clone
    # Configure
    start_date = '2017-01-01'

    # Clone repo
    repo_org = os.path.join('repos', org_name)
    repo_path = os.path.join(repo_org, f'{repo_name}.git')
    clone_repo(repo_path, repo_org, clone_addr)

    # Extract commit info
    cmd = f'cd {repo_path} && git log --since "{start_date}" --pretty=format:"%cs{sep}%an%ae" > commit.csv'
    os.system(cmd)

    # Format result
    csv_path = os.path.join(repo_path, 'commit.csv')
    try:
        df = pd.read_csv(csv_path, header=None, sep=sep)
    except:
        return pd.DataFrame([])

    df.columns = ['date', 'author']
    commit_df = pd.DataFrame(df.groupby('date').size())
    commit_df.columns = ['commits']
    commit_df.index = pd.to_datetime(commit_df.index.values)
    df = df.drop_duplicates()
    df['date'] = pd.to_datetime(df['date'])
    author_df = df.set_index('date')
    fpath = os.path.join(f'{repo_path}', 'commits.csv')
    auth_fpath = os.path.join(f'{repo_path}', 'authors.csv')
    commit_df.to_csv(fpath, header=False, sep=sep)
    author_df.to_csv(auth_fpath, header=False, sep=sep)


def generate_data(fname, limit=None):
    with open(f'eco/{fname}', 'rb') as f:
        eco = tomli.load(f)
    urls = [x['url'] for x in eco['repo']]
    if limit is not None and isinstance(limit, int):
        urls = urls[:limit]
    with ProcessPoolExecutor(max_workers=8) as exe:
        list(tqdm(exe.map(fetch_repo, urls), total=len(urls)))


@sleep_and_retry
@limits(calls=2, period=5)
def request(url):
    rsp = requests.get(url, headers={'Authorization': 'token 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'})
    return rsp


def get_org_repo(fname):
    with open(f'eco/{fname}', 'rb') as f:
        eco = tomli.load(f)
    urls = [x['url'] for x in eco['repo']]
    paths = []
    for url in urls:
        org_name = url.split('/')[-2]
        repo_name = os.path.splitext(os.path.basename(url))[0]
        paths.append(os.path.join(org_name, repo_name))
    return paths


def combine_data(fname, fstat):
    eco_name = os.path.splitext(fname)[0]
    files = glob.glob(f'repos/*/*/{fstat}.csv')
    agg_df = None
    paths = get_org_repo(fname)
    adj_paths = [f'repos/{x}.git/{fstat}.csv' for x in paths]

    for f in files:
        if f not in adj_paths:
            continue
        df = pd.read_csv(f, header=None, sep=sep)
        df.columns = ['date', fstat]
        df.set_index('date', inplace=True)
        if agg_df is None:
            agg_df = df
        else:
            agg_df = pd.concat([agg_df, df], axis=0)
    if agg_df is not None:
        agg_df = agg_df.sort_index()
        eco_file = eco_name + '_' + fstat + '.csv'
        if not os.path.exists('outputs'):
            os.makedirs('outputs', exist_ok=True)
        csv_path = os.path.join('outputs', eco_file)
        agg_df.to_csv(csv_path)


def download_eco_def(url):
    file = os.path.basename(url)
    r = requests.get(url, allow_redirects=True)
    with open(f'eco/{file}', 'wb') as f:
        f.write(r.content)
    return file


def post_process(fname):
    eco_name = os.path.splitext(fname)[0]
    eco_file = f'{eco_name}_authors.csv'
    eco_path = os.path.join('outputs', eco_file)
    df = pd.read_csv(eco_path)
    author_df = pd.DataFrame([], columns=df['authors'].unique())
    for i, row in df.iterrows():
        author_df.loc[row['date'], row['authors']] = 1
    author_df = author_df.fillna(0)
    author_df.index = pd.to_datetime(author_df.index)
    author_df = author_df.resample('D').max().fillna(0)
    author_roll30 = author_df.rolling(30, min_periods=1).max()
    author_roll30_agg = pd.DataFrame(author_roll30.apply(lambda x: sum(x), axis=1))
    author_roll30_agg.columns = ['author_roll30']
    eco_roll_file = f'{eco_name}_authors_roll30.csv'
    eco_path = os.path.join('outputs', eco_roll_file)
    author_roll30_agg.to_csv(eco_path)
