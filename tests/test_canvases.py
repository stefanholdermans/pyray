# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests for canvases."""

import unittest
import pyray


class TestCanvasCreation(unittest.TestCase):
    """Test case for canvas creation."""

    def test_canvas(self):
        """Test creating a canvas."""
        c = pyray.Canvas(10, 20)
        self.assertEqual(10, c.width)
        self.assertEqual(20, c.height)

    def test_canvas_positions(self):
        """Test the positions of a newly created canvas."""
        c = pyray.Canvas(10, 20)
        self.assertEqual([(x, y) for x in range(10) for y in range(20)],
                         list(c))

    def test_pixel_initialization(self):
        """Assert that every pixel in a newly created canvas is initialized to
        black."""
        c = pyray.Canvas(10, 20)
        for x, y in c:
            self.assertEqual(pyray.Color(0.0, 0.0, 0.0), c[x, y])

    def test_writing_pixels(self):
        """Test writing pixels to a canvas."""
        c = pyray.Canvas(10, 20)
        red = pyray.Color(1.0, 0.0, 0.0)
        c[2, 3] = red
        self.assertEqual(red, c[2, 3])
