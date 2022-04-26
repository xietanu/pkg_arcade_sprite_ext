"""Classes and functions for handling components in spaces"""
from dataclasses import dataclass


@dataclass
class Coords:
    """Class for storing 2D coords"""

    x_coord: int
    y_coord: int

    def __add__(self, other):
        if not isinstance(other, Coords):
            raise ValueError("Cannot add Coords to non-Coords")
        return Coords(self.x_coord + other.x_coord, self.y_coord + other.y_coord)
