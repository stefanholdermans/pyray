# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Canvases."""

from __future__ import annotations

import textwrap
from typing import Iterator, List, Tuple as Pair

from .colors import Color


class Canvas:
    """A rectangular grid of pixels."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self._pixels = {(x, y): Color(0.0, 0.0, 0.0)
                        for x in range(width)
                        for y in range(height)}

    def __iter__(self) -> Iterator[Pair[int, int]]:
        yield from self._pixels

    def __getitem__(self, pos: Pair[int, int]) -> Color:
        if pos not in self:
            raise IndexError

        return self._pixels[pos]

    def __setitem__(self, pos: Pair[int, int], color: Color):
        if pos not in self:
            raise IndexError

        self._pixels[pos] = color

    def __contains__(self, pos: Pair[int, int]) -> bool:
        return pos in self._pixels

    def ppm(self) -> str:
        """Return a PPM-formatted string representation of the canvas."""
        buffer: List[str] = []
        self._construct_ppm_header(buffer)
        self._construct_ppm_pixel_data(buffer)
        return "\n".join(buffer) + "\n"

    MAGIC_NUMBER: str = "P3"
    MAX_COLOR_VALUE: int = 255

    def _construct_ppm_header(self, buffer: List[str]):
        buffer.append(self.MAGIC_NUMBER)
        buffer.append(f"{self.width} {self.height}")
        buffer.append(f"{self.MAX_COLOR_VALUE}")

    def _construct_ppm_pixel_data(self, buffer: List[str]):
        for y in range(self.height):
            line_buffer = []

            for x in range(self.width):
                color = self[x, y]

                red = self._color_value(color.red)
                green = self._color_value(color.green)
                blue = self._color_value(color.blue)

                line_buffer.append(f"{red}")
                line_buffer.append(f"{green}")
                line_buffer.append(f"{blue}")

            for line in textwrap.wrap(" ".join(line_buffer)):
                buffer.append(line)

    def _color_value(self, intensity: float) -> int:
        intensity = min(max(0.0, intensity), 1.0)
        return round(self.MAX_COLOR_VALUE * intensity)
