# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests for matrices."""

import unittest
import pyray


class TestMatrices(unittest.TestCase):
    """Test case for matrices."""

    def test_4x4_matrix(self):
        """Test constructing and inspecting a 4x4 matrix."""
        m = pyray.matrix4x4([1.0, 2.0, 3.0, 4.0,
                             5.5, 6.5, 7.5, 8.5,
                             9.0, 10.0, 11.0, 12.0,
                             13.5, 14.5, 15.5, 16.5])
        self.assertEqual(1.0, m[0, 0])
        self.assertEqual(4.0, m[0, 3])
        self.assertEqual(5.5, m[1, 0])
        self.assertEqual(7.5, m[1, 2])
        self.assertEqual(11, m[2, 2])
        self.assertEqual(13.5, m[3, 0])
        self.assertEqual(15.5, m[3, 2])

    def test_2x2_matrix(self):
        """Assert that a 2x2 matrix is representable."""
        m = pyray.matrix2x2([-3.0, 5.0,
                             1.0, -2.0])
        self.assertEqual(-3.0, m[0, 0])
        self.assertEqual(5.0, m[0, 1])
        self.assertEqual(1.0, m[1, 0])
        self.assertEqual(-2.0, m[1, 1])

    def test_3x3_matrix(self):
        """Assert that a 3x3 matrix is representable."""
        m = pyray.matrix3x3([-3.0, 5.0, 0.0,
                             1.0, -2.0, -7.0,
                             0.0, 1.0, 1.0])
        self.assertEqual(-3.0, m[0, 0])
        self.assertEqual(-2.0, m[1, 1])
        self.assertEqual(1.0, m[2, 2])

    def test_matrix_equality(self):
        """Test matrix equality with identical matrices."""
        a = pyray.matrix4x4([1.0, 2.0, 3.0, 4.0,
                             5.0, 6.0, 7.0, 8.0,
                             9.0, 8.0, 7.0, 6.0,
                             5.0, 4.0, 3.0, 2.0])
        b = pyray.matrix4x4([1.0, 2.0, 3.0, 4.0,
                             5.0, 6.0, 7.0, 8.0,
                             9.0, 8.0, 7.0, 6.0,
                             5.0, 4.0, 3.0, 2.0])
        self.assertEqual(a, b)

    def test_matrix_inequality(self):
        """Test matrix equality with different matrices."""
        a = pyray.matrix4x4([1.0, 2.0, 3.0, 4.0,
                             5.0, 6.0, 7.0, 8.0,
                             9.0, 8.0, 7.0, 6.0,
                             5.0, 4.0, 3.0, 2.0])
        b = pyray.matrix4x4([2.0, 3.0, 4.0, 5.0,
                             6.0, 7.0, 8.0, 9.0,
                             8.0, 7.0, 6.0, 5.0,
                             4.0, 3.0, 2.0, 1.0])
        self.assertNotEqual(a, b)
