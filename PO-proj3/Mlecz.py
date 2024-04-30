from Roslina import Roslina


class Mlecz(Roslina):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=0, _inicjatywa=0, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'm', _wiek, _sila, _inicjatywa, _cooldown)

    def akcja(self):
        for i in range(3):
            iloscOrganizmow = self._swiat.getIloscOrganizmow()
            super().akcja()
            if iloscOrganizmow > self._swiat.getIloscOrganizmow():
                return
