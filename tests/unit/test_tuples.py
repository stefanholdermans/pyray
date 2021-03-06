# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Unit ests for tuples, points, and vectors."""

import math
import pyray
from .test_pyray import TestPyray


class TestTuples(TestPyray):
    """Test case for tuples, points, and vectors."""

    def test_tuple(self):
        """Assert that tuples have x, y, z, and w components."""
        a = pyray.Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(4.3, a.x)
        self.assertEqual(-4.2, a.y)
        self.assertEqual(3.1, a.z)
        self.assertEqual(1.0, a.w)

    def test_tuple_is_point(self):
        """Assert that a tuple with w=1 is a point."""
        a = pyray.Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertTrue(a.is_point())
        self.assertFalse(a.is_vector())

    def test_tuple_is_vector(self):
        """Assert that a tuple with w=0 is a vector."""
        a = pyray.Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertFalse(a.is_point())
        self.assertTrue(a.is_vector())

    def test_point(self):
        """Assert that `pyray.point` creates tuples with w=1."""
        p = pyray.point(4.0, -4.0, 3.0)
        self.assertEqual(pyray.Tuple(4.0, -4.0, 3.0, 1.0), p)

    def test_vector(self):
        """Assert that `pyray.vector` creates tuples with w=0."""
        v = pyray.vector(4.0, -4.0, 3.0)
        self.assertEqual(pyray.Tuple(4.0, -4.0, 3.0, 0.0), v)


class TestArithmeticTupleOperations(TestPyray):
    """Test case for arithmetic tuple operations."""

    def test_adding_tuples(self):
        """Test adding two tuples."""
        a1 = pyray.Tuple(3.0, -2.0, 5.0, 1.0)
        a2 = pyray.Tuple(-2.0, 3.0, 1.0, 0.0)
        self.assertTuplesAlmostEqual(pyray.Tuple(1.0, 1.0, 6.0, 1.0), a1 + a2)

    def test_subtracting_points(self):
        """Test subtracting two points."""
        p1 = pyray.point(3.0, 2.0, 1.0)
        p2 = pyray.point(5.0, 6.0, 7.0)
        self.assertTuplesAlmostEqual(pyray.vector(-2.0, -4.0, -6.0), p1 - p2)

    def test_subtracting_vector_from_point(self):
        """Test subtracting a vector from a point."""
        p = pyray.point(3.0, 2.0, 1.0)
        v = pyray.vector(5.0, 6.0, 7.0)
        self.assertTuplesAlmostEqual(pyray.point(-2.0, -4.0, -6.0), p - v)

    def test_subtracting_vectors(self):
        """Test subtracting two vectors."""
        v1 = pyray.vector(3.0, 2.0, 1.0)
        v2 = pyray.vector(5.0, 6.0, 7.0)
        self.assertTuplesAlmostEqual(pyray.vector(-2.0, -4.0, -6.0), v1 - v2)

    def test_subtracting_from_zero_vector(self):
        """Test subtracting a vector from the zero vector."""
        zero = pyray.vector(0.0, 0.0, 0.0)
        v = pyray.vector(1.0, -2.0, 3.0)
        self.assertTuplesAlmostEqual(pyray.vector(-1.0, 2.0, -3.0), zero - v)

    def test_tuple_negation(self):
        """Test negating a tuple."""
        a = pyray.Tuple(1.0, -2.0, 3.0, -4.0)
        self.assertTuplesAlmostEqual(pyray.Tuple(-1.0, 2.0, -3.0, 4.0), -a)

    def test_multiplying_tuple_by_scalar(self):
        """Test multiplying a tuple by a scalar."""
        a = pyray.Tuple(1.0, -2.0, 3.0, -4.0)
        self.assertTuplesAlmostEqual(
            pyray.Tuple(3.5, -7.0, 10.5, -14.0), 3.5 * a)

    def test_multiplying_scalar_by_tuple(self):
        """Test multiplying a scalar by a tuple."""
        a = pyray.Tuple(1.0, -2.0, 3.0, -4.0)
        self.assertTuplesAlmostEqual(
            pyray.Tuple(3.5, -7.0, 10.5, -14.0), a * 3.5)

    def test_multiplying_tuple_by_fraction(self):
        """Test multiplying a tuple by a fraction."""
        a = pyray.Tuple(1.0, -2.0, 3.0, -4.0)
        self.assertTuplesAlmostEqual(
            pyray.Tuple(0.5, -1.0, 1.5, -2.0), a * 0.5)

    def test_dividing_tuple_by_scalar(self):
        """Test dividing a tuple by a scalar."""
        a = pyray.Tuple(1.0, -2.0, 3.0, -4.0)
        self.assertTuplesAlmostEqual(pyray.Tuple(0.5, -1.0, 1.5, -2.0), a / 2)


class TestSpecificTupleOperations(TestPyray):
    """Test case for specific tuple operations."""

    def test_magnitude_of_x_aligned_unit_vector(self):
        """Test computing the magnitude of `pyray.vector(1.0, 0.0, 0.0)`."""
        v = pyray.vector(1.0, 0.0, 0.0)
        self.assertFloatsAlmostEqual(1.0, v.magnitude())

    def test_magnitude_of_y_aligned_unit_vector(self):
        """Test computing the magnitude of `pyray.vector(0.0, 1.0, 0.0)`."""
        v = pyray.vector(0.0, 1.0, 0.0)
        self.assertFloatsAlmostEqual(1.0, v.magnitude())

    def test_magnitude_of_z_aligned_unit_vector(self):
        """Test computing the magnitude of `pyray.vector(0.0, 0.0, 1.0)`."""
        v = pyray.vector(0.0, 0.0, 1.0)
        self.assertFloatsAlmostEqual(1.0, v.magnitude())

    def test_magnitude_of_positive_vector(self):
        """Test computing the magnitude of `pyray.vector(1.0, 2.0, 3.0)`."""
        v = pyray.vector(1.0, 2.0, 3.0)
        self.assertFloatsAlmostEqual(math.sqrt(14.0), v.magnitude())

    def test_magnitude_of_negative_vector(self):
        """Test computing the magnitude of `pyray.vector(-1.0, -2.0, -3.0)`."""
        v = pyray.vector(-1.0, -2.0, -3.0)
        self.assertFloatsAlmostEqual(math.sqrt(14.0), v.magnitude())

    def test_normalizing_aligned_vector(self):
        """Assert that normalizing `pyray.vector(4.0, 0.0, 0.0)` gives
        (1.0, 1.0, 0).
        """
        v = pyray.vector(4.0, 0.0, 0.0)
        self.assertTuplesAlmostEqual(pyray.vector(1.0, 0, 0), v.normalized())

    def test_normalizing_nonaligned_vector(self):
        """Test normalizing `pyray.vector(1.0, 2.0, 3.0)`."""
        v1 = pyray.vector(1.0, 2.0, 3.0)
        v2 = v1.normalized()
        self.assertTuplesAlmostEqual(
            pyray.vector(1.0 / math.sqrt(14.0),
                         2.0 / math.sqrt(14.0),
                         3.0 / math.sqrt(14.0)),
            v2)

    def test_magnitude_of_normalized_vector(self):
        """Test the magnitude of a normalized vector."""
        v = pyray.vector(1.0, 2.0, 3.0)
        norm = v.normalized()
        self.assertFloatsAlmostEqual(1.0, norm.magnitude())

    def test_dot_product(self):
        """Test the dot product of two tuples."""
        a = pyray.vector(1.0, 2.0, 3.0)
        b = pyray.vector(2.0, 3.0, 4.0)
        self.assertFloatsAlmostEqual(20.0, a.dot(b))

    def test_cross_product(self):
        """Test the cross product of two vectors."""
        a = pyray.vector(1.0, 2.0, 3.0)
        b = pyray.vector(2.0, 3.0, 4.0)
        self.assertTuplesAlmostEqual(pyray.vector(-1.0, 2.0, -1.0), a.cross(b))
        self.assertTuplesAlmostEqual(pyray.vector(1.0, -2.0, 1.0), b.cross(a))

    def test_cross_product_of_point(self):
        """Assert that computing the cross product of a point with a vector
        raises an exception.
        """
        a = pyray.point(1.0, 2.0, 3.0)
        b = pyray.vector(2.0, 3.0, 4.0)
        with self.assertRaises(pyray.TupleTypeMismatchError):
            _ = a.cross(b)

    def test_cross_product_with_point(self):
        """Assert that computing the cross product of a vector with a point
        raises an exception.
        """
        a = pyray.vector(1.0, 2.0, 3.0)
        b = pyray.point(2.0, 3.0, 4.0)
        with self.assertRaises(pyray.TupleTypeMismatchError):
            _ = a.cross(b)


class TestReflection(TestPyray):
    """Test case for reflecting vectors."""

    def test_reflecting_vector_approaching_at_45_degrees(self):
        """Test reflecting a vector approaching at 45 degrees."""
        v = pyray.vector(1.0, -1.0, 0.0)
        n = pyray.vector(0.0, 1.0, 0.0)
        r = v.reflected(n)
        self.assertTuplesAlmostEqual(pyray.vector(1.0, 1.0, 0.0), r)

    def test_reflecting_vector_off_slanted_surface(self):
        """Test reflecting a vector off a slanted surface."""
        v = pyray.vector(0.0, -1.0, 0.0)
        n = pyray.vector(math.sqrt(2.0) / 2.0, math.sqrt(2.0) / 2.0, 0.0)
        r = v.reflected(n)
        self.assertTuplesAlmostEqual(pyray.vector(1.0, 0.0, 0.0), r)
