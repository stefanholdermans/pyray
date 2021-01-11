# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Rays."""

from dataclasses import dataclass
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
