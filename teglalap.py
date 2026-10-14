
class Teglalap:

    def validal(self, a_oldal, b_oldal):
        if (a_oldal<=0) or (b_oldal<=0):
            raise ValueError(f"Csak pozitív szám lehet az oldalak hossza: {a_oldal}, {b_oldal}")
        
    def __init__(self, a_oldal, b_oldal):
        self.validal(a_oldal, b_oldal)
        self.a_oldal = a_oldal
        self.b_oldal = b_oldal

    def kerulet(self):
        return 2 * (self.a_oldal * self.b_oldal)

    def terulet(self):
        return self.a_oldal * self.b_oldal


