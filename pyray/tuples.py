# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

"""Tuples, points, and vectors."""

from dataclasses import dataclass


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


def point(x: float, y: float, z: float) -> Tuple:
    """Create a point."""
    return Tuple(x, y, z, 1.0)


def vector(x: float, y: float, z: float) -> Tuple:
    """Create a vector."""
    return Tuple(x, y, z, 0.0)
