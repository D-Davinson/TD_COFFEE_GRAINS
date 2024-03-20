class Sachet:
    def __init__(self, poids, type_paquet, composition, grains):
        self.poids = poids
        self.type_paquet = type_paquet
        self.composition = composition
        self.grains = grains

    def composition_grain(self):
        if (self.poids % 500 == 0 or self.poids <= 2000 and len(self.grains) > 0 and self.type_paquet in ["pure", "mixte"] and sum(self.composition) == 100):
            return True
        else:
            return False