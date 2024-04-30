from Zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=9, _inicjatywa=5, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'W', _wiek, _sila, _inicjatywa, _cooldown)
