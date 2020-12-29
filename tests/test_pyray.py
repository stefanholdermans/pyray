# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests utilities."""

import unittest
import pyray


class TestPyray(unittest.TestCase):
    """Test case for photorealistic 3D rendering."""

    def assertTuplesAlmostEqual(self, first: pyray.Tuple, second: pyray.Tuple):
        # pylint: disable=invalid-name
        """Assert that two tuples are equal as determined by the pointwise
        differences of their components rounded to 7 decimal places.
        """
        self.assertAlmostEqual(first.x, second.x)
        self.assertAlmostEqual(first.y, second.y)
        self.assertAlmostEqual(first.z, second.z)
        self.assertAlmostEqual(first.w, second.w)

    def assert4x4MatricesAlmostEqual(
            self, first: pyray.Matrix4x4, second: pyray.Matrix4x4):
        # pylint: disable=invalid-name
        """Assert that two 4x4 matrices are equal as determined by the pointwise
        differences of their cells rounded to 7 decimal places.
        """
        for row in range(4):
            for col in range(4):
                self.assertAlmostEqual(first[row, col], second[row, col])
