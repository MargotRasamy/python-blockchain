import time

def mine_block(last_block, data):
    """
    Miner un block à partir du dernier block et des données
    """
    timestamp = time.time_ns()
    last_hash = last_block.hash
    hash = f'{timestamp}-{last_hash}'

    return Block(timestamp, last_hash, hash, data)

def genesis():
    """
    Generer le block genesis
    """
    return Block('time.time_ns()', 'genesis_last_hash', 'genesis_hash', [])

class Block:
    """
    Block : une unité de stockage
    Stocke les transactions dans une blockchain qui supporte une cryptomonnaie
    """
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            'Block('
            f'timestamp : {self.timestamp}, '
            f'last_hash : {self.last_hash}, '
            f'hash : {self.hash}, '
            f'data : {self.data})'
        )

def main():
    genesis_block = genesis()
    block = mine_block(genesis_block, 'foo')
    print(block)

if __name__ == '__main__':
    main()

