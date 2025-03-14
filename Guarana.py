from Roslina import Roslina


class Guarana(Roslina):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=0, _inicjatywa=0, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'g', _wiek, _sila, _inicjatywa, _cooldown)

    def kolizja(self, organizm):
        organizm.setSila(organizm.getSila() + 3)
        komunikat = ('Guarana zjedzona przez ' + organizm.nazwaOrganizmu(organizm.getSymbol()) + ' na pozycji ' +
                     str(self.getX()) + ', ' + str(self.getY()) + ', jego sila wzrasta do ' + str(organizm.getSila()))
        newX = self.getX()
        newY = self.getY()
        self._swiat.dodajKomunikat(komunikat)
        self._swiat.usunOrganizm(self)
        organizm._swiat.przeniesOrganizm(organizm, newX, newY)

    def maSwojaKolizje(self):
        return True
