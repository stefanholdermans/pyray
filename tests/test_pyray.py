# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests utilities."""

import unittest
import pyray


class TestPyray(unittest.TestCase):
    """Test case for photorealistic 3D rendering."""

    def assertFloatsAlmostEqual(self, first: float, second: float):
        #pylint: disable=invalid-name
        """Assert that two floating-point values are equal as determined by
        their difference rounded to 5 decimal places.
        """
        self.assertAlmostEqual(first, second, 5)

    def assertTuplesAlmostEqual(self, first: pyray.Tuple, second: pyray.Tuple):
        # pylint: disable=invalid-name
        """Assert that two tuples are equal as determined by the pointwise
        differences of their components rounded to 5 decimal places.
        """
        self.assertFloatsAlmostEqual(first.x, second.x)
        self.assertFloatsAlmostEqual(first.y, second.y)
        self.assertFloatsAlmostEqual(first.z, second.z)
        self.assertFloatsAlmostEqual(first.w, second.w)

    def assertColorsAlmostEqual(self, first: pyray.Color, second: pyray.Color):
        # pylint: disable=invalid-name
        """Assert that two colors are equal as determined by the pointwise
        differences of their components rounded to 5 decimal places.
        """
        self.assertFloatsAlmostEqual(first.red, second.red)
        self.assertFloatsAlmostEqual(first.green, second.green)
        self.assertFloatsAlmostEqual(first.blue, second.blue)

    def assertMatricesAlmostEqual(
            self, first: pyray.Matrix, second: pyray.Matrix):
        # pylint: disable=invalid-name
        """Assert that two matrices are equal as determined by the pointwise
        differences of their cells rounded to 5 decimal places.
        """
        self.assertEqual(first.order, second.order)

        for row, col in first:
            self.assertFloatsAlmostEqual(first[row, col], second[row, col])
