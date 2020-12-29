# Copyright (c) 2020 Stefan Holdermans.
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
        return self._pixels[pos]

    def __setitem__(self, pos: Tuple[int, int], color: Color):
        self._pixels[pos] = color

    def to_ppm(self) -> str:
        """Return a PPM-formatted string representation of the canvas."""
        builder = self._PPMBuilder(self)
        builder.construct_header()
        builder.construct_pixel_data()
        return builder.to_ppm()

    class _PPMBuilder:
        MAGIC_NUMBER: str = "P3"
        MAX_COLOR_VALUE: int = 255

        canvas: Canvas
        buffer: List[str]

        def __init__(self, canvas: Canvas):
            self.canvas = canvas
            self.buffer = []

        def construct_header(self):
            """Append the PPM header."""
            self.buffer.append(self.MAGIC_NUMBER)
            self.buffer.append(f"{self.canvas.width} {self.canvas.height}")
            self.buffer.append(f"{self.MAX_COLOR_VALUE}")

        def construct_pixel_data(self):
            """Append the PPM pixel data."""
            for y in range(self.canvas.height):
                line_buffer = []

                for x in range(self.canvas.width):
                    color = self.canvas[x, y]

                    red = self._color_value(color.red)
                    green = self._color_value(color.green)
                    blue = self._color_value(color.blue)

                    line_buffer.append(f"{red}")
                    line_buffer.append(f"{green}")
                    line_buffer.append(f"{blue}")

                for line in textwrap.wrap(" ".join(line_buffer)):
                    self.buffer.append(line)

        def _color_value(self, intensity: float) -> int:
            intensity = min(max(0.0, intensity), 1.0)
            return round(self.MAX_COLOR_VALUE * intensity)

        def to_ppm(self) -> str:
            """Return a string representation."""
            return "\n".join(self.buffer) + "\n"
