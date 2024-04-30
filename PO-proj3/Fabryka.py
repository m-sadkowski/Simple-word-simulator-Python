import random


def utworzZwierze(symbol, x, y, swiat):
    from Antylopa import Antylopa
    from Wilk import Wilk
    from Zolw import Zolw
    from CyberOwca import CyberOwca
    from Owca import Owca
    from Lis import Lis
    if symbol == 'W':
        return Wilk(x, y, swiat)
    elif symbol == 'Z':
        return Zolw(x, y, swiat)
    elif symbol == 'L':
        return Lis(x, y, swiat)
    elif symbol == 'A':
        return Antylopa(x, y, swiat)
    elif symbol == 'O':
        return Owca(x, y, swiat)
    elif symbol == 'X':
        return CyberOwca(x, y, swiat)
    else:
        pass


def utworzRosline(symbol, x, y, swiat):
    from BarszczSosnowskiego import BarszczSosnowskiego
    from Guarana import Guarana
    from Mlecz import Mlecz
    from Trawa import Trawa
    from WilczeJagody import WilczeJagody
    if symbol == 't':
        return Trawa(x, y, swiat)
    elif symbol == 'g':
        return Guarana(x, y, swiat)
    elif symbol == 'w':
        return WilczeJagody(x, y, swiat)
    elif symbol == 'b':
        return BarszczSosnowskiego(x, y, swiat)
    elif symbol == 'm':
        return Mlecz(x, y, swiat)
    else:
        pass


def generujOrganizmySwiat(self, swiat):
    from Czlowiek import Czlowiek
    from Antylopa import Antylopa
    from Wilk import Wilk
    from Zolw import Zolw
    from CyberOwca import CyberOwca
    from Owca import Owca
    from Lis import Lis
    from BarszczSosnowskiego import BarszczSosnowskiego
    from Guarana import Guarana
    from Mlecz import Mlecz
    from Trawa import Trawa
    from WilczeJagody import WilczeJagody
    maxOrganizmow = max((swiat.getWysokosc() + swiat.getWysokosc()) // 11, 1)
    rand = random.Random()

    def dodajLosoweOrganizmy(rodzaj, liczba):
        for _ in range(liczba):
            punkt = swiat.generujOrganizm()
            swiat.dodajOrganizm(rodzaj(punkt.x, punkt.y, swiat))

    typy_organizmow = [Owca, Wilk, Zolw, Lis, Antylopa, Trawa, Mlecz, Guarana, WilczeJagody, BarszczSosnowskiego,
                       CyberOwca]

    for typ in typy_organizmow:
        ilosc = rand.randint(1, maxOrganizmow)
        dodajLosoweOrganizmy(typ, ilosc)

    para = swiat.generujOrganizm()
    swiat.dodajOrganizm(Czlowiek(para.x, para.y, swiat))
