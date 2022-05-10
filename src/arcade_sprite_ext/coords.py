"""Classes and functions for handling components in spaces."""
from dataclasses import dataclass
from math import sqrt


@dataclass
class Coords:
    """Class for storing 2D or 3D coordinates."""

    x_coord: int
    y_coord: int
    z_coord: int = 0

    def __add__(self, other):
        """Add two coordinates together."""
        if not isinstance(other, Coords):
            raise TypeError("Cannot add Coords to non-Coords")
        return Coords(
            self.x_coord + other.x_coord,
            self.y_coord + other.y_coord,
            self.z_coord + other.z_coord,
        )

    def __sub__(self, other):
        """Subtract another Coords from this one."""
        if not isinstance(other, Coords):
            raise TypeError("Cannot subtract Coords to non-Coords")
        return Coords(
            self.x_coord - other.x_coord,
            self.y_coord - other.y_coord,
            self.z_coord - other.z_coord,
        )

    def euclidean_distance_squared_to(self, other: "Coords") -> int:
        """Return the squared distance between the coordinates.

        Faster than calculating the euclidean distance.

        Parameters
        ----------
            other : Coords
                The coordinate to measure to.

        Returns
        -------
            int
                The squared distance between the coordinates.
        """
        difference = self - other
        return difference.x_coord ^ 2 + difference.y_coord ^ 2 + difference.z_coord ^ 2

    def euclidean_distance_to(self, other: "Coords") -> float:
        """Return the squared distance between the coordinates.

        Parameters
        ----------
            other : Coords
                The coordinate to measure to.

        Returns
        -------
            float
                The distance between the coordinates.
        """
        return sqrt((self.euclidean_distance_squared_to(other)))
