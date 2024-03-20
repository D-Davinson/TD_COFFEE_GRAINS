class Sachet:
    def __init__(self, poids, type_paquet, composition):
        self.poids = poids
        self.type_paquet = type_paquet
        self.composition = composition
        self.grains = []

    def composition_grain(self):
        if (self.poids % 500 == 0 and self.poids <= 2000 and self.type_paquet in ["pure", "mixte"] and sum(self.composition) == 100):
            return True
        else:
            return False