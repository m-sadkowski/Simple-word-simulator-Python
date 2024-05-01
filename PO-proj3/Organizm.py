class Organizm:
    def __init__(self, x, y, swiat, symbol, wiek=0, sila=0, inicjatywa=0, cooldown=0):
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._symbol = symbol
        self._x = x
        self._y = y
        self._swiat = swiat
        self._wiek = wiek
        self._cooldown = cooldown

    def akcja(self):
        pass

    def kolizja(self, organizm):
        pass

    def maSwojaKolizje(self):
        return False

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def zwiekszWiek(self):
        self._wiek += 1

    def zmniejszCooldown(self):
        self._cooldown -= 1

    def getSila(self):
        return self._sila

    def getInicjatywa(self):
        return self._inicjatywa

    def getSymbol(self):
        return self._symbol

    def getWiek(self):
        return self._wiek

    def getCooldown(self):
        return self._cooldown

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def setSila(self, sila):
        self._sila = sila

    def setCooldown(self, cooldown):
        self._sila = cooldown

    def jestesCyberOwca(self):
        return False

    def nazwaOrganizmu(self, symbol):
        switcher = {
            'C': "Czlowiek",
            'W': "Wilk",
            'O': "Owca",
            'Z': "Zolw",
            'L': "Lis",
            'A': "Antylopa",
            'X': "CyberOwca",
            't': "Trawa",
            'm': "Mlecz",
            'g': "Guarana",
            'w': "Wilcze Jagody",
            'b': "Barszcz Sosnowskiego",
        }
        return switcher.get(symbol, "Nieznany")
