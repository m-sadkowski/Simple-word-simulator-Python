import random

from Zwierze import Zwierze


class Antylopa(Zwierze):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=4, _inicjatywa=4, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'A', _wiek, _sila, _inicjatywa, _cooldown)

    def akcja(self):
        rand = random.Random()
        ruch = rand.randint(0, 3)
        newX = self._x
        newY = self._y

        if ruch == 0:
            newY -= 2
        elif ruch == 1:
            newX += 2
        elif ruch == 2:
            newY += 2
        elif ruch == 3:
            newX -= 2

        if newX < 0 or newX > self._swiat.getWysokosc() - 1 or newY < 0 or newY > self._swiat.getSzerokosc() - 1:
            return

        organizm_na_nowym_pol = self._swiat.getOrganizm(newX, newY)
        if organizm_na_nowym_pol is None:
            self._x = newX
            self._y = newY
        elif newX != self._x or newY != self._y:
            self.kolizja(organizm_na_nowym_pol)

    def kolizja(self, organizm):
        if organizm.getSila() > self.getSila():
            rand = random.Random()
            rng = rand.randint(0, 1)
            if rng == 1:
                komunikat = self.nazwaOrganizmu(self.getSymbol()) + ' ucieka przed ' + organizm.nazwaOrganizmu(organizm.getSymbol()) + ' na pozycji ' + str(organizm.getX()) + ', ' + str(organizm.getY())
                self._swiat.dodajKomunikat(komunikat)
                self.akcja()
            else:
                komunikat = organizm.nazwaOrganizmu(organizm.getSymbol()) + ' zabija ' + self.nazwaOrganizmu(
                    self.getSymbol()) + ' na pozycji ' + str(self.getX()) + ', ' + str(self.getY())
                self._swiat.dodajKomunikat(komunikat)
                self._swiat.przeniesOrganizm(organizm, self.getX(), self.getY())
                self._swiat.usunOrganizm(self)




