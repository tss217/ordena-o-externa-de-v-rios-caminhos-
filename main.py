class Ordenacao:
    def __init__(self, fita, numberBlocks):
        self.blocks = []
        self.numberBlocks = numberBlocks
        self.fita = fita

    def setBlocks(self):
        blockSize = len(self.fita) // self.numberBlocks

        for i in range(0, len(self.fita), blockSize):
            currentlyBlock = self.fita[i:i+blockSize]
            self.blocks.append(currentlyBlock)

    def setOrdering(self):
        self.setBlocks()

        for i, block in enumerate(self.blocks):
            self.blocks[i] = sorted(block)

    def intercalation(self):
        self.setOrdering()

        while len(self.blocks) > 1:
            intercalated = []

            for i in range(0, len(self.blocks), 2):
                self.setOrdering()
                if i + 1 < len(self.blocks):
                    intercalated.append(self.blocks[i] + self.blocks[i + 1])

            self.blocks = intercalated

fita = ['B', 'T', 'P', 'S', 'U', 'J', 'M', 'H', 'B', 'M', 'E', 'N', 'F', 'S', 'H', 'J', 'M', 'H', 'F', 'Y', 'B', 'N', 'Q', 'M', 'F']

ord = Ordenacao(fita, 8)
ord.intercalation()

finalBlock = ord.blocks[0]
print(finalBlock)
