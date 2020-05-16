from utils.generatePrime import generatePrimeNumber


class DH:
    n = 0

    def __init__(self):
        self.n = generatePrimeNumber()
