import random

from Punkt import Punkt


class Swiat:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.plansza = [['.' for _ in range(n)] for _ in range(m)]
        self.komunikaty = []
        self.organizmy = []

    def przeniesOrganizm(self, organizm, x, y):
        organizm.setX(x)
        organizm.setY(y)

    def generujOrganizm(self):
        while True:
            X = random.randint(0, self.m - 1)
            Y = random.randint(0, self.n - 1)
            if self.getOrganizm(X, Y) is None:
                return Punkt(X, Y)

    def dodajOrganizm(self, organizm):
        self.organizmy.append(organizm)

    def usunOrganizm(self, organizm):
        self.organizmy = [x for x in self.organizmy if x != organizm]

    def posortujOrganizmy(self):
        self.organizmy = [org for org in self.organizmy if org is not None]
        self.organizmy.sort(key=lambda org: org.getInicjatywa(), reverse=True)

    def dodajKomunikat(self, komunikat):
        self.komunikaty.append(komunikat)

    def getWysokosc(self):
        return self.m

    def getSzerokosc(self):
        return self.n

    def getIloscOrganizmow(self):
        return len(self.organizmy)

    def getOrganizm(self, x, y):
        for organizm in self.organizmy:
            if organizm is not None:
                if organizm.getX() == x and organizm.getY() == y:
                    return organizm
        return None

    def getPlansza(self):
        return self.plansza

    def generujSwiat(self):
        from Fabryka import generujOrganizmySwiat
        generujOrganizmySwiat(self, self)

    def wykonajTure(self, strzalka):
        if not (strzalka == 0 or strzalka == 1 or strzalka == 2 or strzalka == 3 or strzalka == 4):
            return
        for _ in range(20):
            print('\n')
        self.komunikaty.clear()
        self.posortujOrganizmy()
        for organizm in self.organizmy:
            if organizm is not None:
                if organizm._cooldown > 0:
                    organizm.zmniejszCooldown()
                if organizm.getSymbol() == 'C':
                    organizm.akcjaCzlowieka(strzalka)
                else:
                    organizm.akcja()

