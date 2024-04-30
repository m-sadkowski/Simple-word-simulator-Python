from Zwierze import Zwierze


class Owca(Zwierze):
    def __init__(self, _x, _y, _swiat, _wiek=0, _sila=4, _inicjatywa=4, _cooldown=0):
        super().__init__(_x, _y, _swiat, 'O', _wiek, _sila, _inicjatywa, _cooldown)
