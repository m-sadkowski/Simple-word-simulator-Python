from Roslina import Roslina


class BarszczSosnowskiego(Roslina):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=10, _inicjatywa=0, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'b', _wiek, _sila, _inicjatywa, _cooldown)

    def akcja(self):
        X = [0, 0, 1, -1]
        Y = [1, -1, 0, 0]
        for i in range(4):
            temp = self._swiat.getOrganizm(self._x + X[i], self._y + Y[i])
            if temp is not None:
                if not isinstance(temp, Roslina):
                    komunikat = ('Barszcz Sosnowskiego zabija ' + self._swiat.getOrganizm(self._x + X[i], self._y + Y[i]).nazwaOrganizmu(
                        self._swiat.getOrganizm(self._x + X[i], self._y + Y[i]).getSymbol()) + ' na pozycji ' + str(self.getX()) + ', ' + str(self.getY()))
                    self._swiat.dodajKomunikat(komunikat)
                    self._swiat.usunOrganizm(self._swiat.getOrganizm(self._x + X[i], self._y + Y[i]))
        super().akcja()

    def kolizja(self, organizm):
        komunikat = 'Barszcz Sosnowskiego zabija ' + organizm.nazwaOrganizmu(
            organizm.getSymbol()) + ' na pozycji ' + str(self.getX()) + ', ' + str(self.getY())
        self._swiat.dodajKomunikat(komunikat)
        self._swiat.usunOrganizm(organizm)
        self._swiat.usunOrganizm(self)

    def maSwojaKolizje(self):
        return True
