# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Canvases."""

from __future__ import annotations

import textwrap
from typing import Dict, Iterator, List, Tuple

from .colors import Color


class Canvas:
    """A rectangular grid of pixels."""

    _pixels: Dict[Tuple[int, int], Color]
    width: int
    height: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        pixels = [((x, y), Color(0.0, 0.0, 0.0))
                  for x in range(width)
                  for y in range(height)]
        self._pixels = dict(pixels)

    def __iter__(self) -> Iterator[Tuple[int, int]]:
        yield from self._pixels

    def __getitem__(self, pos: Tuple[int, int]) -> Color:
        if pos not in self:
            raise IndexError

        return self._pixels[pos]

    def __setitem__(self, pos: Tuple[int, int], color: Color):
        if pos not in self:
            raise IndexError

        self._pixels[pos] = color

    def __contains__(self, pos: Tuple[int, int]) -> bool:
        return pos in self._pixels


class _PPMBuilder:
    MAGIC_NUMBER: str = "P3"
    MAX_COLOR_VALUE: int = 255

    _buffer: List[str]

    def __init__(self):
        self._buffer = []

    def construct_header(self, canvas: Canvas):
        """Append the PPM header for a canvas."""
        self._buffer.append(self.MAGIC_NUMBER)
        self._buffer.append(f"{canvas.width} {canvas.height}")
        self._buffer.append(f"{self.MAX_COLOR_VALUE}")

    def construct_pixel_data(self, canvas: Canvas):
        """Append the PPM pixel data for a canvas."""
        for y in range(canvas.height):
            line_buffer = []

            for x in range(canvas.width):
                color = canvas[x, y]

                red = self._color_value(color.red)
                green = self._color_value(color.green)
                blue = self._color_value(color.blue)

                line_buffer.append(f"{red}")
                line_buffer.append(f"{green}")
                line_buffer.append(f"{blue}")

            for line in textwrap.wrap(" ".join(line_buffer)):
                self._buffer.append(line)

    def _color_value(self, intensity: float) -> int:
        intensity = min(max(0.0, intensity), 1.0)
        return round(self.MAX_COLOR_VALUE * intensity)

    def to_ppm(self) -> str:
        """Return a string representation."""
        return "\n".join(self._buffer) + "\n"


def ppm(canvas: Canvas) -> str:
    """Return a PPM-formatted string representation of a canvas."""
    builder = _PPMBuilder()
    builder.construct_header(canvas)
    builder.construct_pixel_data(canvas)
    return builder.to_ppm()
