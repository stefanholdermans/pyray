# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Lights."""

from dataclasses import dataclass
from .colors import Color
from .tuples import Tuple, TupleTypeMismatchError


@dataclass
class PointLight:
    """A light source with no size, existing at a single point in space."""

    position: Tuple
    intensity: Color

    def __init__(self, position: Tuple, intensity: Color):
        if not position.is_point():
            raise TupleTypeMismatchError

        self.position = position
        self.intensity = intensity
