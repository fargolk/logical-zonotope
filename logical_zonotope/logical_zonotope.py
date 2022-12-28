class LogicalZonotope:

    def __init__(self):
        self.center = (0, 0)
        self.generators = []

    def set(self, center, generators):
        self.center = center
        self.generators = generators

    def print(self):
        print("Zonotope center:", self.center)
        print("Zonotope generators:", self.generators)


