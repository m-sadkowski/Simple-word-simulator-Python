from Zwierze import Zwierze


class Czlowiek(Zwierze):
    stalaSila = 5
    COOLDOWN = 20

    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=5, _inicjatywa=4, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'C', _wiek, _sila, _inicjatywa, _cooldown)
        self.__mocUzyta = False
        self.__czasMocy = 0

    def getCzasMocy(self):
        return self.__czasMocy

    def getMocUzyta(self):
        return self.__mocUzyta

    def setCzasMocy(self, czasMocy):
        self.__czasMocy = czasMocy

    def setMocUzyta(self, mocUzyta):
        self.__mocUzyta = mocUzyta

    def akcjaCzlowieka(self, przycisk):
        if self._cooldown > 0:
            self._cooldown -= 1
        if self.__mocUzyta:
            self.__czasMocy += 1
        if self.__czasMocy == 5 + 1:
            self.__mocUzyta = False
            self.__czasMocy = 0
            self._cooldown = 20
        if self._sila > 5 and self.__mocUzyta:
            self._sila -= 1
            self._swiat.dodajKomunikat("Sila czlowieka wynosi " + str(self._sila))

        newX = self._x
        newY = self._y

        if przycisk == 0:
            if self._x > 0:
                newX -= 1
        elif przycisk == 1:
            if self._x < self._swiat.getWysokosc() - 1:
                newX += 1
        elif przycisk == 2:
            if self._y > 0:
                newY -= 1
        elif przycisk == 3:
            if self._y < self._swiat.getSzerokosc() - 1:
                newY += 1
        elif przycisk == 4:
            if not self.__mocUzyta and self._cooldown == 0:
                self.aktywujMoc()

        if newX != self._x or newY != self._y:
            if self._swiat.getOrganizm(newX, newY) is not None:
                super().kolizja(self._swiat.getOrganizm(newX, newY))
            else:
                self._swiat.przeniesOrganizm(self, newX, newY)

    def aktywujMoc(self):
        self._sila += 5
        self.__mocUzyta = True
        self._swiat.dodajKomunikat('Czlowiek wypil eliksir na pozycji ' + str(self.getX()) + ', ' + str(self.getY()))
