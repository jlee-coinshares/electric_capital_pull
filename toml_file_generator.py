import os

list_of_ecos = ['truffle', 'polkadot', 'ethereum', 'near', 'near-protocol', 'gitcoin-grants', 'the-graph', 'dappradar',
                'bitcoin', 'general', 'solana', 'friktion-labs', 'cosmos', 'ethereum-consensus', 'cardano', 'celo',
                'lightning', 'ethereum-classic', 'web3-js', 'tezos', 'filecoin', 'zero-knowledge-cryptography',
                'internet-computer', 'zcash', 'defillama', 'flow', 'ouroboros', 'dfinity-iou', 'manta-network',
                'ethereum-execution', 'tendermint', 'web3-python', 'zksync', 'move', 'stacks', 'rose-on-aurora',
                'rubic', 'basic-attention-token', 'maskbook', 'mina-protocol', 'dxdao', 'parity', 'gnosis',
                'cowswap-exchange', 'vega-protocol', 'webaverse', 'embark', 'plutonomicon', 'beethoven-x', 'uniswap',
                'hyperledger', 'monero', '0l-network', 'sora', 'solidity', 'groestlcoin', 'mercurial-finance', 'ipfs',
                'eos', 'bitcoin-js', 'unique-network', 'kodadot', 'badger-finance', 'badger-dao', 'otter-finance',
                'threefold-token', 'ethereum-virtual-machine', 'maker', 'mahadao', 'arthx', 'aladdindao', 'lisk', 'xrp',
                'descartesnetwork', 'xyo', 'nervos', 'avalanche', 'elrond', 'polygon', 'maiar-exchange', 'arbitrum',
                'oddz', 'balancer', 'klaytn', 'aleo', 'polygon-hermez', 'chia', 'ledger', 'keep-network', 'berty',
                'kalmar', 'decentraland', 'quiknode-labs', 'optimism', 'nethermind', 'snapshot', 'lukso', 'neo',
                'oasis', 'aeternity', 'interledger', 'walletconnect', 'zeroswap', 'quarry-protocol', 'aptos', 'iota',
                'status', 'mobius-money', 'blockchain-com', 'fabric', 'stellar', 'maidsafecoin', 'mlabs',
                'energy-web-token', 'sushi-swap', 'darwinia-network', 'darwinia network', 'darwinia', 'aavegotchi',
                'bitfrost-finance', 'bifrost', 'algorand', 'satellite', 'ergo', 'rubicon', 'mean-dao', 'agoric',
                'pooltogether', 'astar-network', 'interlay', 'interbtc', 'gitcoin', 'skycoin', 'zenlink', 'hummingbot',
                'beefy-finance', 'osmosis', 'synthetix', 'sxrp', 'sxmr', 'sbnb', 'sbch', 'sada', 'ilink',
                'ibtc-synthetix', 'hydradx', 'giveth', 'galactic-council', 'thales', 'opensquare-network']


def toml_field_generator(path_of_toml_files):
    for ecosystems_by_numbers in os.listdir(path_of_toml_files):

        for toml_file_parser in os.listdir(f"{path_of_toml_files}/{ecosystems_by_numbers}"):
            if toml_file_parser.replace(".toml", "") in list_of_ecos:
                yield f"https://raw.githubusercontent.com/electric-capital/crypto-ecosystems/master/data/ecosystems/{toml_file_parser[0]}/{toml_file_parser}"
