from Zwierze import Zwierze


class CyberOwca(Zwierze):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=11, _inicjatywa=4, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'X', _wiek, _sila, _inicjatywa, _cooldown)

    def jestesCyberOwca(self):
        return True

    def znajdzNajblizszy(self):
        x = 9999
        y = 9999
        znaleziono = False
        for organizm in self._swiat.organizmy:
            from BarszczSosnowskiego import BarszczSosnowskiego
            from Punkt import Punkt
            if isinstance(organizm, BarszczSosnowskiego):
                if abs(organizm.getX() - self.getX()) + abs(organizm.getY() - self.getY()) < abs(x - self.getX()) + abs(
                        y - self.getY()):
                    x = organizm.getX()
                    y = organizm.getY()
                    znaleziono = True
        if znaleziono:
            return Punkt(x, y)
        else:
            return False

    def akcja(self):
        if self._swiat.czySaBarszczeSosnowskiego():
            punkt = self.znajdzNajblizszy()
            if not punkt:
                self._swiat.dodajKomunikat('CyberOwca nie wyczuwa barszczu sosnowskiego na mapie.')
            else:
                newX = self.getX()
                newY = self.getY()
                barszcz = self._swiat.getOrganizm(punkt.x, punkt.y)
                if punkt.x > self.getX():
                    newX += 1
                elif punkt.y > self.getY():
                    newY += 1
                elif punkt.x < self.getX():
                    newX -= 1
                elif punkt.y < self.getY():
                    newY -= 1

                if punkt.y == newY and punkt.x == newX:
                    self._swiat.dodajKomunikat('CyberOwca dorwala barszcz sosnowskiego na pozycji ' + str(self.getX()) + ', ' + str(self.getY()))
                    self._swiat.usunOrganizm(barszcz)
                    self.setX(newX)
                    self.setY(newY)
                else:
                    self._swiat.dodajKomunikat('CyberOwca z pozycji ' + str(self.getX()) + ', ' + str(self.getY()) + ' zmierza do barszczu sosnowskiego z ' + str(punkt.x) + ', ' + str(punkt.y))
                    if not self._swiat.getOrganizm(newX, newY) is None:
                        self.kolizja(self._swiat.getOrganizm(newX, newY))
                    else:
                        self.setX(newX)
                        self.setY(newY)
        else:
            super().akcja()