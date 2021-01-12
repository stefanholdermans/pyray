# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Rays."""

from __future__ import annotations

from dataclasses import dataclass

from .matrices import Matrix
from .tuples import Tuple


@dataclass
class Ray:
    """A ray."""

    origin: Tuple
    direction: Tuple

    def __init__(self, origin: Tuple, direction: Tuple):
        if not origin.is_point() or not direction.is_vector():
            raise ValueError

        self.origin = origin
        self.direction = direction

    def position(self, t: float) -> Tuple:
        """Compute the point at a given distance along the ray."""
        return self.origin + self.direction * t

    def transformed(self, transform: Matrix) -> Ray:
        """Apply a transformation matrix to the ray."""
        return Ray(transform * self.origin, transform * self.direction)
