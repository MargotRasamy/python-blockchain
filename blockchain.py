class Block:
    """
    Block : une unité de stockage
    Stocke les transactions dans une blockchain qui supporte une cryptomonnaie
    """
    def __init__(self, data):
        self.data = data

class Blockchain:
    

    """
    Blockchain: un registre publique de transactions.
    Une liste de blocks (set de données) contenant des transactions.
    """
    def __init__(self):
        self.chain = [] 
 
    def add_block(self, data):
        self.chain.append(Block(data))
    
