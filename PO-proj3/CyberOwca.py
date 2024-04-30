from Zwierze import Zwierze


class CyberOwca(Zwierze):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=6, _inicjatywa=9, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'X', _wiek, _sila, _inicjatywa, _cooldown)
