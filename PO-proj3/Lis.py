import random

from Zwierze import Zwierze


class Lis(Zwierze):

    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=3, _inicjatywa=7, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'L', _wiek, _sila, _inicjatywa, _cooldown)

    def akcja(self):
        rand = random.Random()
        ruch = rand.randint(0, 3)
        newX = self._x
        newY = self._y

        if ruch == 0:
            newY -= 1
        elif ruch == 1:
            newX += 1
        elif ruch == 2:
            newY += 1
        elif ruch == 3:
            newX -= 1

        if newX < 0 or newX > self._swiat.getWysokosc() - 1 or newY < 0 or newY > self._swiat.getSzerokosc() - 1:
            return

        organizm_na_nowym_polu = self._swiat.getOrganizm(newX, newY)
        if organizm_na_nowym_polu is None:
            self._x = newX
            self._y = newY
        elif newX != self._x or newY != self._y:
            if organizm_na_nowym_polu.getSila() > self.getSila():
                komunikat = ('Lis korzysta z dobrego wechu i omija ' +
                             organizm_na_nowym_polu.nazwaOrganizmu(organizm_na_nowym_polu.getSymbol()) +
                             ' na pozycji ' + str(organizm_na_nowym_polu.getX()) + ', ' + str(organizm_na_nowym_polu.getY()))
                self._swiat.dodajKomunikat(komunikat)
