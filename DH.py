from utils.generatePrime import generatePrimeNumber


class DH:
    n = 0
    g = 0
    privateKey = 0
    sharedKey = 0
    foreignKey = 0
    sessionKey = 0

    def __init__(self, n, g):
        self.n = n
        self.g = g

    def setPrivateKey(self, x):
        self.privateKey = x
        self.sharedKey = pow(self.g, x) % self.n
        return self

    def setForeignKey(self, key):
        self.foreignKey = key
        self.setSessionKey()
        return self

    def setSessionKey(self):
        self.sessionKey = pow(self.foreignKey, self.privateKey) % self.n
        return self
