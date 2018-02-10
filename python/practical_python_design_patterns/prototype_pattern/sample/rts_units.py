# -*- coding: utf-8 -*-

from .unit import Unit
import os


class Knight(Unit):
    def __init__(self, path, level):
        super()
        self.unit_type = "Knight"
        filename = os.path.join(path, "{0}{1}".format(self.unit_type, level))
        self._init_from_file(filename)

    def __str__(self):
        return "[knight] {}".format(super().__str__())


class Archer(Unit):
    def __init__(self, path, level):
        super()
        self.unit_type = "Archer"
        filename = os.path.join(path, "{0}{1}".format(self.unit_type, level))
        self._init_from_file(filename)

    def __str__(self):
        return "[archer] {}".format(super().__str__())


class Barracks:
    def __init__(self, path):
        self.units = {
            "knight": {
                1: Knight(path, 1),
                2: Knight(path, 2)
            },
            "archer": {
                1: Archer(path, 1),
                2: Archer(path, 2)
            }
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()
