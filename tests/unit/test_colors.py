# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Unit tests for colors."""

import pyray
from .test_pyray import TestPyray


class TestColors(TestPyray):
    """Test case for colors."""

    def test_color(self):
        """Assert that colors are (red, green, blue) tuples."""
        c = pyray.Color(-0.5, 0.4, 1.7)
        self.assertEqual(-0.5, c.red)
        self.assertEqual(0.4, c.green)
        self.assertEqual(1.7, c.blue)


class TestColorOperations(TestPyray):
    """Test case for color operations."""

    def test_adding_colors(self):
        """Test adding colors."""
        c1 = pyray.Color(0.9, 0.6, 0.75)
        c2 = pyray.Color(0.7, 0.1, 0.25)
        self.assertColorsAlmostEqual(pyray.Color(1.6, 0.7, 1.0), c1 + c2)

    def test_subtracting_colors(self):
        """Test subtracting colors."""
        c1 = pyray.Color(0.9, 0.6, 0.75)
        c2 = pyray.Color(0.7, 0.1, 0.25)
        self.assertColorsAlmostEqual(pyray.Color(0.2, 0.5, 0.5), c1 - c2)

    def test_multiplying_color_by_scalar(self):
        """Test multiplying a color by a scalar."""
        c = pyray.Color(0.2, 0.3, 0.4)
        self.assertColorsAlmostEqual(pyray.Color(0.4, 0.6, 0.8), c * 2)

    def test_multiplying_scalar_by_color(self):
        """Test multiplying a scalar by a color."""
        c = pyray.Color(0.2, 0.3, 0.4)
        self.assertColorsAlmostEqual(pyray.Color(0.4, 0.6, 0.8), 2 * c)

    def test_multiplying_colors(self):
        """Test multiplying colors."""
        c1 = pyray.Color(1.0, 0.2, 0.4)
        c2 = pyray.Color(0.9, 1.0, 0.1)
        self.assertColorsAlmostEqual(pyray.Color(0.9, 0.2, 0.04), c1 * c2)
