# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Colors."""

from __future__ import annotations

from dataclasses import dataclass
import numbers


@dataclass
class Color:
    """A color."""

    red: float
    green: float
    blue: float

    def hadamard(self, other: Color) -> Color:
        """Compute the Hadamard product of the color with another color."""
        red = self.red * other.red
        green = self.green * other.green
        blue = self.blue * other.blue
        return Color(red, green, blue)

    def __add__(self, other):
        if isinstance(other, Color):
            red = self.red + other.red
            green = self.green + other.green
            blue = self.blue + other.blue
            return Color(red, green, blue)

        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Color):
            red = self.red - other.red
            green = self.green - other.green
            blue = self.blue - other.blue
            return Color(red, green, blue)

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Color):
            return self.hadamard(other)

        if isinstance(other, numbers.Number):
            red = self.red * other
            green = self.green * other
            blue = self.blue * other
            return Color(red, green, blue)

        return NotImplemented

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
