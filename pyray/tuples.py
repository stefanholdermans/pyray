# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

"""Tuples, points, and vectors."""

from __future__ import annotations

from dataclasses import dataclass
import math
import numbers


@dataclass
class Tuple:
    """Tuples."""

    x: float
    y: float
    z: float
    w: float

    def is_point(self) -> bool:
        """Return whether the tuple is a point."""
        return self.w == 1.0

    def is_vector(self) -> bool:
        """Return whether the tuple is a vector."""
        return self.w == 0.0

    def magnitude(self) -> float:
        """Return the magnitude of the tuple."""
        return math.sqrt(self.x * self.x
                         + self.y * self.y
                         + self.z * self.z
                         + self.w * self.w)

    def normalize(self) -> Tuple:
        """Normalize the tuple."""
        magnitude = self.magnitude()
        x = self.x / magnitude
        y = self.y / magnitude
        z = self.z / magnitude
        w = self.w / magnitude
        return Tuple(x, y, z, w)

    def dot(self, other: Tuple) -> float:
        """Compute the dot product of the tuple with another tuple."""
        return (self.x * other.x
                + self.y * other.y
                + self.z * other.z
                + self.w * other.w)

    def cross(self, other: Tuple) -> Tuple:
        """For vectors, compute the cross product of the tuple with another
        vector.

        Raises `ValueError` if either tuple is not a vector.
        """
        if not (self.is_vector() and other.is_vector()):
            raise ValueError

        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Tuple(x, y, z, 0.0)

    def __add__(self, other):
        if not isinstance(other, Tuple):
            return NotImplemented

        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w
        return Tuple(x, y, z, w)

    def __sub__(self, other):
        if not isinstance(other, Tuple):
            return NotImplemented

        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        w = self.w - other.w
        return Tuple(x, y, z, w)

    def __neg__(self):
        x = -self.x
        y = -self.y
        z = -self.z
        w = -self.w
        return Tuple(x, y, z, w)

    def __mul__(self, scalar):
        if not isinstance(scalar, numbers.Number):
            return NotImplemented

        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        w = self.w * scalar
        return Tuple(x, y, z, w)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if not isinstance(scalar, numbers.Number):
            return NotImplemented

        x = self.x / scalar
        y = self.y / scalar
        z = self.z / scalar
        w = self.w / scalar
        return Tuple(x, y, z, w)


def point(x: float, y: float, z: float) -> Tuple:
    """Create a point."""
    return Tuple(x, y, z, 1.0)


def vector(x: float, y: float, z: float) -> Tuple:
    """Create a vector."""
    return Tuple(x, y, z, 0.0)
