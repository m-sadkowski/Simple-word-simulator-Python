import random

from Fabryka import utworzRosline
from Organizm import Organizm


class Roslina(Organizm):
    def __init__(self, _x, _y, _swiat, _symbol, _wiek=0, _sila=0, _inicjatywa=0, _cooldown=0):
        super().__init__(_x, _y, _swiat, _symbol, _wiek, _sila, _inicjatywa, _cooldown)

    def akcja(self):
        rand = random.Random()
        prawdopodobienstwo = rand.randint(0, 100)
        if prawdopodobienstwo > 95:
            ruch = rand.randint(-1, 1)
            newX = self._x + ruch
            ruch = rand.randint(-1, 1)
            newY = self._y + ruch
            organizm_na_nowym_polu = self._swiat.getOrganizm(newX, newY)

            if (newX < 0 or newX > self._swiat.getWysokosc() - 1 or newY < 0 or newY > self._swiat.getSzerokosc() - 1
                    or organizm_na_nowym_polu):
                return

            nowa = utworzRosline(self.getSymbol(), newX, newY, self._swiat)
            self._swiat.dodajOrganizm(nowa)
            komunikat = (self.nazwaOrganizmu(self.getSymbol()) + ' rozprzestrzenia sie na pozycji ' +
                         str(self.getX()) + ', ' + str(self.getY()))
            self._swiat.dodajKomunikat(komunikat)

    def kolizja(self, organizm):
        return

    def maSwojaKolizje(self):
        return False
