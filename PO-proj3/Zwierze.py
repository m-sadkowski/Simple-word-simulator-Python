import random
from Organizm import Organizm
from Roslina import Roslina


class Zwierze(Organizm):
    def __init__(self, _x, _y, _swiat, _symbol, _wiek=0, _sila=0, _inicjatywa=0, _cooldown=0):
        super().__init__(_x, _y, _swiat, _symbol, _wiek, _sila, _inicjatywa, _cooldown)

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
            self.kolizja(organizm_na_nowym_polu)

    def kolizja(self, organizm):
        if organizm.maSwojaKolizje():
            organizm.kolizja(self)
        elif organizm.getSymbol() == self.getSymbol():
            if organizm.getCooldown() == 0 and self.getCooldown() == 0:
                from Fabryka import utworzZwierze
                nowy = utworzZwierze(self.getSymbol(), self.getX() + 1, self.getY(), self._swiat)
                self._swiat.dodajOrganizm(nowy)
                komunikat = ('rozmnozenie ' + organizm.nazwaOrganizmu(self.getSymbol()) + ' na pozycji (' +
                             str(self.getX()) + ', ' + str(self.getY()) + ')')
                self._swiat.dodajKomunikat(komunikat)
                self.setCooldown(10)
                organizm.setCooldown(10)
                nowy.setCooldown(10)

        elif isinstance(organizm, Roslina):
            komunikat = (organizm.nazwaOrganizmu(self.getSymbol()) + ' zjada ' +
                         organizm.nazwaOrganizmu(organizm.getSymbol()) +
                         ' na pozycji ' + str(organizm.getX()) + ', ' + str(organizm.getY()))
            self._swiat.dodajKomunikat(komunikat)
            self._swiat.przeniesOrganizm(self, organizm.getX(), organizm.getY())
            self._swiat.usunOrganizm(organizm)

        elif organizm.getSila() > self.getSila():
            komunikat = organizm.nazwaOrganizmu(organizm.getSymbol()) + ' zabija ' + organizm.nazwaOrganizmu(
                self.getSymbol()) + ' na pozycji ' + str(organizm.getX()) + ', ' + str(organizm.getY())
            self._swiat.dodajKomunikat(komunikat)
            organizm._swiat.przeniesOrganizm(organizm, organizm.getX(), organizm.getY())
            self._swiat.usunOrganizm(self)

        elif organizm.getSila() <= self.getSila():
            komunikat = self.nazwaOrganizmu(self.getSymbol()) + ' zabija ' + organizm.nazwaOrganizmu(
                organizm.getSymbol()) + ' na pozycji ' + str(self.getX()) + ', ' + str(self.getY())
            self._swiat.dodajKomunikat(komunikat)
            self._swiat.przeniesOrganizm(self, organizm.getX(), organizm.getY())
            self._swiat.usunOrganizm(organizm)

    def maSwojaKolizje(self):
        return False
