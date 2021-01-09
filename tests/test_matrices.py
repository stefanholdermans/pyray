# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests for matrices."""

import pyray
from .test_pyray import TestPyray


class TestMatrices(TestPyray):
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


class TestMatrixMultiplication(TestPyray):
    """Test case for matrix multiplication."""

    def test_matrix_multiplication(self):
        """Test multiplying two matrices."""
        a = pyray.matrix4x4([1.0, 2.0, 3.0, 4.0,
                             5.0, 6.0, 7.0, 8.0,
                             9.0, 8.0, 7.0, 6.0,
                             5.0, 4.0, 3.0, 2.0])
        b = pyray.matrix4x4([-2.0, 1.0, 2.0, 3.0,
                             3.0, 2.0, 1.0, -1.0,
                             4.0, 3.0, 6.0, 5.0,
                             1.0, 2.0, 7.0, 8.0])
        self.assertMatricesAlmostEqual(
            pyray.matrix4x4([20.0, 22.0, 50.0, 48.0,
                             44.0, 54.0, 114.0, 108.0,
                             40.0, 58.0, 110.0, 102.0,
                             16.0, 26.0, 46.0, 42.0]),
            a * b)

    def test_multiplying_matrix_by_tuple(self):
        """Test multiplying a matrix by a tuple."""
        a = pyray.matrix4x4([1.0, 2.0, 3.0, 4.0,
                             2.0, 4.0, 4.0, 2.0,
                             8.0, 6.0, 4.0, 1.0,
                             0.0, 0.0, 0.0, 1.0])
        b = pyray.Tuple(1.0, 2.0, 3.0, 1.0)
        self.assertTuplesAlmostEqual(pyray.Tuple(18.0, 24.0, 33.0, 1.0), a * b)

    def test_multiplying_by_identity_matrix(self):
        """Test multiplying a matrix by the identity matrix."""
        a = pyray.matrix4x4([0.0, 1.0, 2.0, 4.0,
                             1.0, 2.0, 4.0, 8.0,
                             2.0, 4.0, 8.0, 16.0,
                             4.0, 8.0, 16.0, 32.0])
        self.assertMatricesAlmostEqual(a, a * pyray.Matrix.identity(4))


class TestMatrixTransposition(TestPyray):
    """Test case for matrix transposition."""

    def test_matrix_transposition(self):
        """Test transposing a matrix."""
        a = pyray.matrix4x4([0.0, 9.0, 3.0, 0.0,
                             9.0, 8.0, 0.0, 8.0,
                             1.0, 8.0, 5.0, 3.0,
                             0.0, 0.0, 5.0, 8.0])
        self.assertEqual(pyray.matrix4x4([0.0, 9.0, 1.0, 0.0,
                                          9.0, 8.0, 8.0, 0.0,
                                          3.0, 0.0, 5.0, 5.0,
                                          0.0, 8.0, 3.0, 8.0]),
                         a.transposed())

    def test_identity_matrix_transposition(self):
        """Test transposing the identity matrix."""
        a = pyray.Matrix.identity(4).transposed()
        self.assertEqual(pyray.Matrix.identity(4), a)


class TestMatrixInversion(TestPyray):
    """Test case for matrix inversion."""

    def test_determinant_of_2x2_matrix(self):
        """Test calculating the determinant of a 2x2 matrix."""
        a = pyray.matrix2x2([1.0, 5.0,
                             -3.0, 2.0])
        self.assertFloatsAlmostEqual(17.0, a.determinant())

    def test_submatrix_of_3x3_matrix(self):
        """Assert that a submatrix of a 3x3 matrix is a 2x2 matrix."""
        a = pyray.matrix3x3([1.0, 5.0, 0.0,
                             -3.0, 2.0, 7.0,
                             0.0, 6.0, -3.0])
        self.assertEqual(pyray.matrix2x2([-3.0, 2.0,
                                          0.0, 6.0]),
                         a.submatrix(0, 2))

    def test_submatrix_of_4x4_matrix(self):
        """Assert that a submatrix of a 4x4 matrix is a 3x3 matrix."""
        a = pyray.matrix4x4([-6.0, 1.0, 1.0, 6.0,
                             -8.0, 5.0, 8.0, 6.0,
                             -1.0, 0.0, 8.0, 2.0,
                             -7.0, 1.0, -1.0, 1.0])
        self.assertEqual(pyray.matrix3x3([-6.0, 1.0, 6.0,
                                          -8.0, 8.0, 6.0,
                                          -7.0, -1.0, 1.0]),
                         a.submatrix(2, 1))

    def test_minor_of_3x3_matrix(self):
        """Test calculating a minor of a 3x3 matrix."""
        a = pyray.matrix3x3([3.0, 5.0, 0.0,
                             2.0, -1.0, -7.0,
                             6.0, -1.0, 5.0])
        self.assertFloatsAlmostEqual(25.0, a.minor(1, 0))

    def test_cofactor_of_3x3_matrix(self):
        """Test calculating a cofactor of a 3x3 matrix."""
        a = pyray.matrix3x3([3.0, 5.0, 0.0,
                             2.0, -1.0, -7.0,
                             6.0, -1.0, 5.0])
        self.assertFloatsAlmostEqual(-12.0, a.cofactor(0, 0))
        self.assertFloatsAlmostEqual(-25.0, a.cofactor(1, 0))

    def test_deteriminant_of_3x3_matrix(self):
        """Test calculating the determinant of a 3x3 matrix."""
        a = pyray.matrix3x3([1.0, 2.0, 6.0,
                             -5.0, 8.0, -4.0,
                             2.0, 6.0, 4.0])
        self.assertFloatsAlmostEqual(-196.0, a.determinant())

    def test_minor_of_4x4_matrix(self):
        """Test calculating a minor of a 4x4 matrix."""
        a = pyray.matrix4x4([-2.0, -8.0, 3.0, 5.0,
                             -3.0, 1.0, 7.0, 3.0,
                             1.0, 2.0, -9.0, 6.0,
                             -6.0, 7.0, 7.0, -9.0])
        self.assertFloatsAlmostEqual(690.0, a.minor(0, 0))
        self.assertFloatsAlmostEqual(-447.0, a.minor(0, 1))

    def test_cofactor_of_4x4_matrix(self):
        """Test calculating a cofactor of a 4x4 matrix."""
        a = pyray.matrix4x4([-2.0, -8.0, 3.0, 5.0,
                             -3.0, 1.0, 7.0, 3.0,
                             1.0, 2.0, -9.0, 6.0,
                             -6.0, 7.0, 7.0, -9.0])
        self.assertFloatsAlmostEqual(690.0, a.cofactor(0, 0))
        self.assertFloatsAlmostEqual(447.0, a.cofactor(0, 1))

    def test_determinant_of_4x4_matrix(self):
        """Test calculating the determinant of a 4x4 matrix."""
        a = pyray.matrix4x4([-2.0, -8.0, 3.0, 5.0,
                             -3.0, 1.0, 7.0, 3.0,
                             1.0, 2.0, -9.0, 6.0,
                             -6.0, 7.0, 7.0, -9.0])
        self.assertFloatsAlmostEqual(-4071.0, a.determinant())

    def test_invertibility(self):
        """Test testing an invertible matrix for invertibility."""
        a = pyray.matrix4x4([6.0, 4.0, 4.0, 4.0,
                             5.0, 5.0, 7.0, 6.0,
                             4.0, -9.0, 3.0, -7.0,
                             9.0, 1.0, 7.0, -6.0])
        self.assertTrue(a.is_invertible())

    def test_noninvertibility(self):
        """Test testing a noninvertible matrix for invertibility."""
        a = pyray.matrix4x4([-4.0, 2.0, -2.0, -3.0,
                             9.0, 6.0, 2.0, 6.0,
                             0.0, -5.0, 1.0, -5.0,
                             0.0, 0.0, 0.0, 0.0])
        self.assertFalse(a.is_invertible())

    def test_inverse_1(self):
        """Test calculating the inverse of a matrix."""
        a = pyray.matrix4x4([-5.0, 2.0, 6.0, -8.0,
                             1.0, -5.0, 1.0, 8.0,
                             7.0, 7.0, -6.0, -7.0,
                             1.0, -3.0, 7.0, 4.0])
        self.assertMatricesAlmostEqual(
            pyray.matrix4x4([0.21805, 0.45113, 0.24060, -0.04511,
                             -0.80827, -1.45677, -0.44361, 0.52068,
                             -0.07895, -0.22368, -0.05263, 0.19737,
                             -0.52256, -0.81391, -0.30075, 0.30639]),
            a.inverse())

    def test_inverse_2(self):
        """Test calculating the inverse of another matrix."""
        a = pyray.matrix4x4([8.0, -5.0, 9.0, 2.0,
                             7.0, 5.0, 6.0, 1.0,
                             -6.0, 0.0, 9.0, 6.0,
                             -3.0, 0.0, -9.0, -4.0])
        self.assertMatricesAlmostEqual(
            pyray.matrix4x4([-0.15385, -0.15385, -0.28205, -0.53846,
                             -0.07692, 0.12308, 0.02564, 0.03077,
                             0.35897, 0.35897, 0.43590, 0.92308,
                             -0.69231, -0.69231, -0.76923, -1.92308]),
            a.inverse())

    def test_inverse_3(self):
        """Test calculating the inverse of a third matrix."""
        a = pyray.matrix4x4([9.0, 3.0, 0.0, 9.0,
                             -5.0, -2.0, -6.0, -3.0,
                             -4.0,  9.0,  6.0,  4.0,
                             -7.0,  6.0,  6.0,  2.0])
        self.assertMatricesAlmostEqual(
            pyray.matrix4x4([-0.04074, -0.07778, 0.14444, -0.22222,
                             -0.07778,  0.03333, 0.36667, -0.33333,
                             -0.02901, -0.14630, -0.10926, 0.12963,
                             0.17778,  0.06667, -0.26667, 0.33333]),
            a.inverse())

    def test_multiplying_product_by_inverse(self):
        """Test multiplying a product by its inverse."""
        a = pyray.matrix4x4([3.0, -9.0, 7.0, 3.0,
                             3.0, -8.0, 2.0, -9,
                             -4.0, 4.0, 4.0, 1.0,
                             -6.0, 5.0, -1.0, 1.0])
        b = pyray.matrix4x4([8.0, 2.0, 2.0, 2.0,
                             3.0, -1.0, 7.0, 0.0,
                             7.0, 0.0, 5.0, 4.0,
                             6.0, -2.0, 0.0, 5.0])
        c = a * b
        self.assertMatricesAlmostEqual(a, c * b.inverse())


class TestMatrixTransformation(TestPyray):
    """Test case for matrix inversion."""

    def test_point_translation(self):
        """Test multiplying by a translation matrix."""
        transform = pyray.translation(5.0, -3.0, 2.0)
        p = pyray.point(-3.0, 4.0, 5.0)
        self.assertTuplesAlmostEqual(pyray.point(2.0, 1.0, 7.0), transform * p)

    def test_vector_translation(self):
        """Assert that translation does not affect vectors."""
        transform = pyray.translation(5.0, -3.0, 2.0)
        v = pyray.vector(-3.0, 4.0, 5.0)
        self.assertEqual(v, transform * v)

    def test_inverse_translation(self):
        """Test multiplying by the inverse of a translation matrix."""
        transform = pyray.translation(5.0, -3.0, 2.0)
        inv = transform.inverse()
        p = pyray.point(-3.0, 4.0, 5.0)
        self.assertTuplesAlmostEqual(pyray.point(-8.0, 7.0, 3.0), inv * p)

    def test_point_scaling(self):
        """Test applying a scaling matrix to a point."""
        transform = pyray.scaling(2.0, 3.0, 4.0)
        p = pyray.point(-4.0, 6.0, 8.0)
        self.assertTuplesAlmostEqual(pyray.point(-8.0, 18.0, 32.0),
                                     transform * p)

    def test_vector_scaling(self):
        """Test applying a scaling matrix to a vector."""
        transform = pyray.scaling(2.0, 3.0, 4.0)
        v = pyray.vector(-4.0, 6.0, 8.0)
        self.assertTuplesAlmostEqual(pyray.vector(-8.0, 18.0, 32.0),
                                     transform * v)

    def test_inverse_scaling(self):
        """Test multiplying by the inverse of a scaling matrix."""
        transform = pyray.scaling(2.0, 3.0, 4.0)
        inv = transform.inverse()
        v = pyray.vector(-4.0, 6.0, 8.0)
        self.assertTuplesAlmostEqual(pyray.vector(-2.0, 2.0, 2.0),
                                     inv * v)
