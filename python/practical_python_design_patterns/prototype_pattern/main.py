# -*- coding: utf-8 -*-

import os
from sample import rts_units

if __name__ == '__main__':
    path = os.path.join(os.getcwd(), "data")
    barracks = rts_units.Barracks(path)
    knight = barracks.build_unit("knight", 1)
    archer = barracks.build_unit("archer", 2)
    print(knight)
    print(archer)
