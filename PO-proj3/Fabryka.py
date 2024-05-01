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
            if not punkt is None:
                swiat.dodajOrganizm(rodzaj(punkt.x, punkt.y, swiat))

    typy_organizmow = [Owca, Wilk, Zolw, Lis, Antylopa, Trawa, Mlecz, Guarana, WilczeJagody, BarszczSosnowskiego,
                       CyberOwca]

    for typ in typy_organizmow:
        ilosc = rand.randint(1, maxOrganizmow)
        dodajLosoweOrganizmy(typ, ilosc)

    para = swiat.generujOrganizm()
    if not para is None:
        swiat.dodajOrganizm(Czlowiek(para.x, para.y, swiat))

def wczytaj_swiat(nazwa):
    try:
        with open(nazwa + ".txt", 'r') as file:
            m, n = map(int, file.readline().split())
            ilosc_organizmow = int(file.readline())

            from Swiat import Swiat
            swiat = Swiat(m, n)

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

            for _ in range(ilosc_organizmow):
                line = file.readline().strip().split()
                symbol = line[0]

                x, y, wiek, sila, inicjatywa, cooldown = map(int, line[1:])

                if symbol == 'A':
                    swiat.dodajOrganizm(Antylopa(x, y, swiat, wiek, sila, inicjatywa, cooldown))
                elif symbol == 'b':
                    swiat.dodajOrganizm(BarszczSosnowskiego(x, y, swiat, wiek, sila, inicjatywa, cooldown))
                elif symbol == 'C':
                    swiat.dodajOrganizm(Czlowiek(x, y, swiat, wiek, sila, inicjatywa, cooldown))
                elif symbol == 'g':
                    swiat.dodajOrganizm(Guarana(x, y, swiat, wiek, sila, inicjatywa, cooldown))
                elif symbol == 'L':
                    swiat.dodajOrganizm(Lis(x, y, swiat, wiek, sila, inicjatywa, cooldown))
                elif symbol == 'm':
                    swiat.dodajOrganizm(Mlecz(x, y, swiat, wiek, sila, inicjatywa, cooldown))
                elif symbol == 'O':
                    swiat.dodajOrganizm(Owca(x, y, swiat, wiek, sila, inicjatywa, cooldown))
                elif symbol == 't':
                    swiat.dodajOrganizm(Trawa(x, y, swiat, wiek, sila, inicjatywa, cooldown))
                elif symbol == 'w':
                    swiat.dodajOrganizm(WilczeJagody(x, y, swiat, wiek, sila, inicjatywa, cooldown))
                elif symbol == 'W':
                    swiat.dodajOrganizm(Wilk(x, y, swiat, wiek, sila, inicjatywa, cooldown))
                elif symbol == 'Z':
                    swiat.dodajOrganizm(Zolw(x, y, swiat, wiek, sila, inicjatywa, cooldown))

            czas_mocy, moc_uzyta = map(int, file.readline().split())

            for organizm in swiat.organizmy:
                if isinstance(organizm, Czlowiek):
                    organizm.setCzasMocy(czas_mocy)
                    organizm.setMocUzyta(True if moc_uzyta == 1 else False)
                    break

            return swiat

    except FileNotFoundError as f:
        print("Nie znaleziono pliku:", f)
