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
        for _ in range(100):
            X = random.randint(0, self.m - 1)
            Y = random.randint(0, self.n - 1)
            if self.getOrganizm(X, Y) is None:
                return Punkt(X, Y)
        return None

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

    def zapiszSwiat(self, nazwa):
        print("zapisano do pliku:", nazwa)
        try:
            with open(str(nazwa) + ".txt", 'w') as writer:
                czy_czlowiek_zyje = False
                czlowiek = None

                writer.write(str(self.getWysokosc()) + " " + str(self.getSzerokosc()) + "\n")
                writer.write(str(self.getIloscOrganizmow()) + "\n")

                for organizm in self.organizmy:
                    if organizm.getSymbol() == 'C':
                        czy_czlowiek_zyje = True
                        czlowiek = organizm
                    writer.write(organizm.getSymbol() + " ")
                    writer.write(str(organizm.getX()) + " ")
                    writer.write(str(organizm.getY()) + " ")
                    writer.write(str(organizm.getWiek()) + " ")
                    writer.write(str(organizm.getSila()) + " ")
                    writer.write(str(organizm.getInicjatywa()) + " ")
                    writer.write(str(organizm.getCooldown()) + "\n")

                if czy_czlowiek_zyje:
                    writer.write(str(czlowiek.getCzasMocy()) + " ")
                    writer.write(str(int(czlowiek.getMocUzyta())) + "\n")

            print("Dane zostały zapisane do pliku.")

        except IOError:
            print("Wystąpił błąd podczas zapisu do pliku.")

    def wykonajTure(self, strzalka):
        if not (strzalka == 0 or strzalka == 1 or strzalka == 2 or strzalka == 3 or strzalka == 4):
            return
        for _ in range(20):
            print('\n')
        self.komunikaty.clear()
        self.posortujOrganizmy()
        for organizm in self.organizmy:
            if organizm is not None:
                if organizm.getCooldown() > 0:
                    organizm.zmniejszCooldown()
                if organizm.getSymbol() == 'C':
                    organizm.akcjaCzlowieka(strzalka)
                else:
                    organizm.akcja()

    def czySaBarszczeSosnowskiego(self):
        from BarszczSosnowskiego import BarszczSosnowskiego
        for organizm in self.organizmy:
            if isinstance(organizm, BarszczSosnowskiego):
                return True
        return False

    def getCzlowiek(self):
        for organizm in self.organizmy:
            if organizm.getSymbol() == 'C':
                return True
        return False