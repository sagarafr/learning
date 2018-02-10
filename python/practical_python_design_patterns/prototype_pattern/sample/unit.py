# -*- coding: utf-8 -*-

from .prototype import Prototype
from copy import deepcopy


class Unit(Prototype):
    def __init__(self):
        self.unit_type = None
        self.life = None
        self.speed = None
        self.attack_power = None
        self.attack_range = None
        self.weapon = None

    def _init_from_file(self, filename):
        with open(filename, 'r') as fd_parameter:
            lines = fd_parameter.readlines()
            self.life = lines[0].rstrip('\n')
            self.speed = lines[1].rstrip('\n')
            self.attack_power = lines[2].rstrip('\n')
            self.attack_range = lines[3].rstrip('\n')
            self.weapon = lines[4].rstrip('\n')

    def __str__(self):
        return "\n".join(["Type: {}".format(self.unit_type),
                          "Life: {}".format(self.life),
                          "Speed: {}".format(self.speed),
                          "Attack Power: {}".format(self.attack_power),
                          "Attack Range: {}".format(self.attack_range),
                          "Weapon: {}".format(self.weapon)])

    def clone(self):
        return deepcopy(self)
