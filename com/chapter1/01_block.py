import hashlib
import json

class Block:
    def __init__(self, nonce, tstamp, transaction, prevhash=''):
        self.nonce = nonce
        self.tstamp = tstamp
        self.transaction = transaction
        self.prevhash = prevhash
        self.hash = self.calcHash()

    def calcHash(self):
        block_string = json.dumps(
            {"nonce":self.nonce, "tstamp":self.tstamp,
             "transaction":self.transaction,
             "prevhash":self.prevhash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        string = "nonce: " + str(self.nonce)
        string += " tstamp: " + str(self.tstamp)
        string += " transaction: " + str(self.transaction)
        string += " prevhas: " + str(self.prevhash)
        string += " hash: " + str(self.hash)
        return string

class BlockChain():
    def __init__(self):
        self.chain = [self.generateGenesisBlock(), ]
    def generateGenesisBlock(self):
        return Block(0, '2018-06-25', 'Genesis Block')
    def getLastBlock(self):
        return self.chain[-1]
    def addBlock(self, newBlock):
        newBlock.prevhash = self.getLastBlock().hash
        newBlock.hash = newBlock.calcHash()
        self.chain.append(newBlock)
    def isChainValid(self):
        for i in range(1, len(self.chain)):
            prevb = self.chain[i-1]
            currb = self.chain[i]
            if(currb.hash != currb.calcHash()):
                print("invalid block")
                return False
            if(currb.prevhash != prevb.hash):
                print("invalid chain")
                return False
        return True

krkCoin = BlockChain()
krkCoin.addBlock(Block(1, '2018-06-25', 100))
krkCoin.addBlock(Block(2, '2018-06-26', 20))
krkCoin.chain[1].transaction = 333
krkCoin.chain[1].hash = krkCoin.chain[1].calcHash()

for block in krkCoin.chain:
    print(block)
print(krkCoin.isChainValid())

