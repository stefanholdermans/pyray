# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests for matrices."""

import pyray
from .test_pyray import TestPyray


class TestMatrices(TestPyray):
    """Test case for matrices."""

    def test_4x4_matrix(self):
        """Test constructing and inspecting a 4x4 matrix."""
        m = pyray.Matrix4x4([1.0, 2.0, 3.0, 4.0,
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
        m = pyray.Matrix2x2([-3.0, 5.0,
                             1.0, -2.0])
        self.assertEqual(-3.0, m[0, 0])
        self.assertEqual(5.0, m[0, 1])
        self.assertEqual(1.0, m[1, 0])
        self.assertEqual(-2.0, m[1, 1])

    def test_3x3_matrix(self):
        """Assert that a 3x3 matrix is representable."""
        m = pyray.Matrix3x3([-3.0, 5.0, 0.0,
                             1.0, -2.0, -7.0,
                             0.0, 1.0, 1.0])
        self.assertEqual(-3.0, m[0, 0])
        self.assertEqual(-2.0, m[1, 1])
        self.assertEqual(1.0, m[2, 2])

    def test_matrix_equality(self):
        """Test matrix equality with identical matrices."""
        a = pyray.Matrix4x4([1.0, 2.0, 3.0, 4.0,
                             5.0, 6.0, 7.0, 8.0,
                             9.0, 8.0, 7.0, 6.0,
                             5.0, 4.0, 3.0, 2.0])
        b = pyray.Matrix4x4([1.0, 2.0, 3.0, 4.0,
                             5.0, 6.0, 7.0, 8.0,
                             9.0, 8.0, 7.0, 6.0,
                             5.0, 4.0, 3.0, 2.0])
        self.assertEqual(a, b)

    def test_matrix_inequality(self):
        """Test matrix equality with different matrices."""
        a = pyray.Matrix4x4([1.0, 2.0, 3.0, 4.0,
                             5.0, 6.0, 7.0, 8.0,
                             9.0, 8.0, 7.0, 6.0,
                             5.0, 4.0, 3.0, 2.0])
        b = pyray.Matrix4x4([2.0, 3.0, 4.0, 5.0,
                             6.0, 7.0, 8.0, 9.0,
                             8.0, 7.0, 6.0, 5.0,
                             4.0, 3.0, 2.0, 1.0])
        self.assertNotEqual(a, b)


class TestMatrixMultiplication(TestPyray):
    """Test case for matrix multiplication."""

    def test_matrix_multiplication(self):
        """Test multiplying two matrices."""
        a = pyray.Matrix4x4([1.0, 2.0, 3.0, 4.0,
                             5.0, 6.0, 7.0, 8.0,
                             9.0, 8.0, 7.0, 6.0,
                             5.0, 4.0, 3.0, 2.0])
        b = pyray.Matrix4x4([-2.0, 1.0, 2.0, 3.0,
                             3.0, 2.0, 1.0, -1.0,
                             4.0, 3.0, 6.0, 5.0,
                             1.0, 2.0, 7.0, 8.0])
        self.assert4x4MatricesAlmostEqual(
            pyray.Matrix4x4([20.0, 22.0, 50.0, 48.0,
                             44.0, 54.0, 114.0, 108.0,
                             40.0, 58.0, 110.0, 102.0,
                             16.0, 26.0, 46.0, 42.0]),
            a * b)

    def test_multiplying_matrix_by_tuple(self):
        """Test multiplying a matrix by a tuple."""
        a = pyray.Matrix4x4([1.0, 2.0, 3.0, 4.0,
                             2.0, 4.0, 4.0, 2.0,
                             8.0, 6.0, 4.0, 1.0,
                             0.0, 0.0, 0.0, 1.0])
        b = pyray.Tuple(1.0, 2.0, 3.0, 1.0)
        self.assertTuplesAlmostEqual(pyray.Tuple(18.0, 24.0, 33.0, 1.0), a * b)

    def test_multiplying_by_identity_matrix(self):
        """Test multiplying a matrix by the identity matrix."""
        a = pyray.Matrix4x4([0.0, 1.0, 2.0, 4.0,
                             1.0, 2.0, 4.0, 8.0,
                             2.0, 4.0, 8.0, 16.0,
                             4.0, 8.0, 16.0, 32.0])
        self.assert4x4MatricesAlmostEqual(a, a * pyray.Matrix4x4.IDENTITY)
