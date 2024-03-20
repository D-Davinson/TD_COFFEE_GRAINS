class Grain:
    def __init__(self,origine,arome,annee,corps):
        self.origine = origine
        self.arome = arome
        self.annee = annee
        self.corps = corps
    def is_valid(self):
        valid_origine = ["Vietnam", "Kenya", "Colombie", "Guatemala"]
        valid_arome = ["Floral", "Fruite", "Chocolate", "Epice"]
        if(self.origine in valid_origine and self.arome in valid_arome and self.annee %5 !=0 and 1 <= self.corps <= 9):
            return True
        else:
            return False
