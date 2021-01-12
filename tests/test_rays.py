# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests for rays."""

import pyray
from .test_pyray import TestPyray


class TestRays(TestPyray):
    """Test case for rays."""

    def test_ray(self):
        """Test creating and querying a ray."""
        origin = pyray.point(1.0, 2.0, 3.0)
        direction = pyray.vector(4.0, 5.0, 6.0)
        r = pyray.Ray(origin, direction)
        self.assertEqual(origin, r.origin)
        self.assertEqual(direction, r.direction)

    def test_position(self):
        """Test computing a point from a distance."""
        r = pyray.Ray(pyray.point(2.0, 3.0, 4.0), pyray.vector(1.0, 0.0, 0.0))
        self.assertTuplesAlmostEqual(pyray.point(2.0, 3.0, 4.0),
                                     r.position(0.0))
        self.assertTuplesAlmostEqual(pyray.point(3.0, 3.0, 4.0),
                                     r.position(1.0))
        self.assertTuplesAlmostEqual(pyray.point(1.0, 3.0, 4.0),
                                     r.position(-1.0))
        self.assertTuplesAlmostEqual(pyray.point(4.5, 3.0, 4.0),
                                     r.position(2.5))

    def test_ray_translation(self):
        """Test translating a ray."""
        r = pyray.Ray(pyray.point(1.0, 2.0, 3.0), pyray.vector(0.0, 1.0, 0.0))
        m = pyray.translation(3.0, 4.0, 5.0)
        r2 = r.transformed(m)
        self.assertTuplesAlmostEqual(pyray.point(4.0, 6.0, 8.0), r2.origin)
        self.assertTuplesAlmostEqual(pyray.vector(0.0, 1.0, 0.0), r2.direction)

    def test_ray_scaling(self):
        """Test scaling a ray."""
        r = pyray.Ray(pyray.point(1.0, 2.0, 3.0), pyray.vector(0.0, 1.0, 0.0))
        m = pyray.scaling(2.0, 3.0, 4.0)
        r2 = r.transformed(m)
        self.assertTuplesAlmostEqual(pyray.point(2.0, 6.0, 12.0), r2.origin)
        self.assertTuplesAlmostEqual(pyray.vector(0.0, 3.0, 0.0), r2.direction)
