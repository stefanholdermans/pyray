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

    def assertMatricesAlmostEqual(
            self, first: pyray.Matrix, second: pyray.Matrix):
        # pylint: disable=invalid-name
        """Assert that two matrices are equal as determined by the pointwise
        differences of their cells rounded to 7 decimal places.
        """
        self.assertEqual(first.dim, second.dim)

        for row, col in first:
            self.assertAlmostEqual(first[row, col], second[row, col])
