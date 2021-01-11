# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests for matrix transformations."""

import math
import pyray
from .test_pyray import TestPyray


class TestTransformations(TestPyray):
    """Test case for matrix transformations."""

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

    def test_reflection(self):
        """Assert that reflection is scaling by a negative value."""
        transform = pyray.scaling(-1.0, 1.0, 1.0)
        p = pyray.point(2.0, 3.0, 4.0)
        self.assertTuplesAlmostEqual(
            pyray.point(-2.0, 3.0, 4.0), transform * p)

    def test_x_axis_rotation(self):
        """Test rotating a point around the x axis."""
        p = pyray.point(0.0, 1.0, 0.0)
        half_quarter = pyray.rotation_x(math.pi / 4.0)
        full_quarter = pyray.rotation_x(math.pi / 2.0)
        self.assertTuplesAlmostEqual(
            pyray.point(0.0, math.sqrt(2.0) / 2.0, math.sqrt(2.0) / 2.0),
            half_quarter * p)
        self.assertTuplesAlmostEqual(
            pyray.point(0.0, 0.0, 1.0),
            full_quarter * p)

    def test_y_axis_rotation(self):
        """Test rotating a point around the y axis."""
        p = pyray.point(0.0, 0.0, 1.0)
        half_quarter = pyray.rotation_y(math.pi / 4.0)
        full_quarter = pyray.rotation_y(math.pi / 2.0)
        self.assertTuplesAlmostEqual(
            pyray.point(math.sqrt(2.0) / 2.0, 0.0, math.sqrt(2.0) / 2.0),
            half_quarter * p)
        self.assertTuplesAlmostEqual(
            pyray.point(1.0, 0.0, 0.0),
            full_quarter * p)

    def test_z_axis_rotation(self):
        """Test rotating a point around the z axis."""
        p = pyray.point(0.0, 1.0, 0.0)
        half_quarter = pyray.rotation_z(math.pi / 4.0)
        full_quarter = pyray.rotation_z(math.pi / 2.0)
        self.assertTuplesAlmostEqual(
            pyray.point(-math.sqrt(2.0) / 2.0, math.sqrt(2.0) / 2.0, 0.0),
            half_quarter * p)
        self.assertTuplesAlmostEqual(
            pyray.point(-1.0, 0.0, 0.0),
            full_quarter * p)

    def test_inverse_rotation(self):
        """Assert that the inverse of an x-axis rotation rotates in the opposite
        direction.
        """
        p = pyray.point(0.0, 1.0, 0.0)
        half_quarter = pyray.rotation_x(math.pi / 4.0)
        inv = half_quarter.inverse()
        self.assertTuplesAlmostEqual(
            pyray.point(0.0, math.sqrt(2.0) / 2.0, -math.sqrt(2.0) / 2.0),
            inv * p)

    def test_skewing_x_in_proportion_to_y(self):
        """Assert that a shearing transformation moves x in proportion to y."""
        transform = pyray.shearing(x=(1.0, 0.0))
        p = pyray.point(2.0, 3.0, 4.0)
        self.assertTuplesAlmostEqual(pyray.point(5.0, 3.0, 4.0), transform * p)

    def test_skewing_x_in_proportion_to_z(self):
        """Assert that a shearing transformation moves x in proportion to z."""
        transform = pyray.shearing(x=(0.0, 1.0))
        p = pyray.point(2.0, 3.0, 4.0)
        self.assertTuplesAlmostEqual(pyray.point(6.0, 3.0, 4.0), transform * p)

    def test_skewing_y_in_proportion_to_x(self):
        """Assert that a shearing transformation moves y in proportion to x."""
        transform = pyray.shearing(y=(1.0, 0.0))
        p = pyray.point(2.0, 3.0, 4.0)
        self.assertTuplesAlmostEqual(pyray.point(2.0, 5.0, 4.0), transform * p)

    def test_skewing_y_in_proportion_to_z(self):
        """Assert that a shearing transformation moves y in proportion to z."""
        transform = pyray.shearing(y=(0.0, 1.0))
        p = pyray.point(2.0, 3.0, 4.0)
        self.assertTuplesAlmostEqual(pyray.point(2.0, 7.0, 4.0), transform * p)

    def test_skewing_z_in_proportion_to_x(self):
        """Assert that a shearing transformation moves z in proportion to x."""
        transform = pyray.shearing(z=(1.0, 0.0))
        p = pyray.point(2.0, 3.0, 4.0)
        self.assertTuplesAlmostEqual(pyray.point(2.0, 3.0, 6.0), transform * p)

    def test_skewing_z_in_proportion_to_y(self):
        """Assert that a shearing transformation moves z in proportion to y."""
        transform = pyray.shearing(z=(0.0, 1.0))
        p = pyray.point(2.0, 3.0, 4.0)
        self.assertTuplesAlmostEqual(pyray.point(2.0, 3.0, 7.0), transform * p)
