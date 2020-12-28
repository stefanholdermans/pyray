# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

"""Canvases."""

from typing import Dict, Tuple
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

    def __iter__(self):
        yield from self._pixels

    def __getitem__(self, pos: Tuple[int, int]) -> Color:
        return self._pixels[pos]

    def __setitem__(self, pos: Tuple[int, int], color: Color):
        self._pixels[pos] = color
