from Roslina import Roslina


class Trawa(Roslina):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=0, _inicjatywa=0, _cooldown=0):
        super().__init__(_x, _y, _swiat, 't', _wiek, _sila, _inicjatywa, _cooldown)
