# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests for canvases."""

import pyray
from .test_pyray import TestPyray


class TestCanvasCreation(TestPyray):
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


class TestCanvasPersistence(TestPyray):
    """Test case for canvas persistence."""

    def test_ppm_header(self):
        """Test constructing the PPM header."""
        c = pyray.Canvas(5, 3)
        ppm = c.to_ppm()
        self.assertEqual(["P3", "5 3", "255"], ppm.split("\n")[:3])

    def test_ppm_pixel_data(self):
        """Test constructing the PPM pixel data."""
        c = pyray.Canvas(5, 3)

        c1 = pyray.Color(1.5, 0.0, 0.0)
        c2 = pyray.Color(0.0, 0.5, 0.0)
        c3 = pyray.Color(-0.5, 0.0, 1.0)

        c[0, 0] = c1
        c[2, 1] = c2
        c[4, 2] = c3

        ppm = c.to_ppm()
        self.assertEqual(["255 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
                          "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0",
                          "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"],
                         ppm.split("\n")[3:6])

    def test_long_lines_in_ppm_files(self):
        """Test splitting long lines in PPM files."""
        c = pyray.Canvas(10, 2)
        for x, y in c:
            c[x, y] = pyray.Color(1.0, 0.8, 0.6)
        ppm = c.to_ppm()
        self.assertEqual(
            ["255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255"
             " 204",
             "153 255 204 153 255 204 153 255 204 153 255 204 153",
             "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255"
             " 204",
             "153 255 204 153 255 204 153 255 204 153 255 204 153"],
            ppm.split("\n")[3:7])

    def test_newline_termination_of_ppm_files(self):
        """Assert that PPM files are terminated by a newline character."""
        c = pyray.Canvas(5, 3)
        ppm = c.to_ppm()
        self.assertEqual("", ppm.split("\n")[-1])
