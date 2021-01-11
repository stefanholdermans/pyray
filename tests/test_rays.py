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
