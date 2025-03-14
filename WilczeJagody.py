from Roslina import Roslina


class WilczeJagody(Roslina):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=99, _inicjatywa=0, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'w', _wiek, _sila, _inicjatywa, _cooldown)

    def kolizja(self, organizm):
        komunikat = ('Wilcze Jagody zabijaja ' + organizm.nazwaOrganizmu(organizm.getSymbol()) + ' na pozycji ' +
                     str(self.getX()) + ', ' + str(self.getY()))
        self._swiat.dodajKomunikat(komunikat)
        self._swiat.usunOrganizm(organizm)
        self._swiat.usunOrganizm(self)

    def maSwojaKolizje(self):
        return True
