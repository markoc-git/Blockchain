import hashlib
class Block():
    def __init__(self,data,prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block("Genesis Block","0")

    def add_block(self,data):
        prevBlock = self.chain[-1]
        newBlock = Block(data,prevBlock.hash)
        self.chain.append(newBlock)


blockchain = Blockchain()
blockchain.add_block("First")
blockchain.add_block("Second")

print("Blockchain")
for block in blockchain.chain:
    print("Data : " + block.data)
    print("Previous hash : " , block.prev_hash)
    print("Hash : " , block.hash )
