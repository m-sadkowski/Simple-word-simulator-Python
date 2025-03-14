import random

from Roslina import Roslina
from Zwierze import Zwierze


class Zolw(Zwierze):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=2, _inicjatywa=1, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'Z', _wiek, _sila, _inicjatywa, _cooldown)

    def akcja(self):
        rand = random.Random()
        szansa = rand.randint(0, 3)

        if szansa == 0:
            super().akcja()

    def kolizja(self, organizm):
        if organizm.getSymbol() == self.getSymbol():
            if organizm.getCooldown() == 0 and self.getCooldown() == 0:
                from Fabryka import utworzZwierze
                nowy = utworzZwierze(self.getSymbol(), self.getX() + 1, self.getY(), self._swiat)
                self._swiat.dodajOrganizm(nowy)
                komunikat = ('rozmnozenie ' + organizm.nazwaOrganizmu(
                    self.getSymbol()) + ' na pozycji (' +
                             str(self.getX()) + ', ' + str(self.getY()) + ')')
                self._swiat.dodajKomunikat(komunikat)
                self.setCooldown(20)
                organizm.setCooldown(20)
                nowy.setCooldown(20)
        elif organizm.getSila() < 5 and not isinstance(organizm, Roslina):
            komunikat = 'Zolw blokuje atak ' + organizm.nazwaOrganizmu(organizm.getSymbol()) + ' na pozycji ' + str(self.getX()) + ', ' + str(self.getY())
            self._swiat.dodajKomunikat(komunikat)
        else:
            komunikat = organizm.nazwaOrganizmu(organizm.getSymbol()) + ' zabija ' + self.nazwaOrganizmu(
                self.getSymbol()) + ' na pozycji ' + str(organizm.getX()) + ', ' + str(organizm.getY())
            self._swiat.dodajKomunikat(komunikat)
            self._swiat.przeniesOrganizm(organizm, self.getX(), self.getY())
            self._swiat.usunOrganizm(self)

    def maSwojaKolizje(self):
        return True
