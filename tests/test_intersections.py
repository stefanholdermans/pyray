# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests for tracking intersections."""

import pyray
from .test_pyray import TestPyray


class TestIntersections(TestPyray):
    """Test case for tracking intersections."""

    def test_intersection(self):
        """Assert that an intersection encapsulates distance and object."""
        s = pyray.Sphere()
        i = pyray.Intersection(3.5, s)
        self.assertEqual(3.5, i.t)
        self.assertEqual(s, i.object)

    def test_aggregating_intersections(self):
        """Test aggregating intersections."""
        s = pyray.Sphere()
        i1 = pyray.Intersection(1.0, s)
        i2 = pyray.Intersection(2.0, s)
        xs = pyray.intersections(i1, i2)
        self.assertEqual(2, len(xs))
        self.assertEqual(1.0, xs[0].t)
        self.assertEqual(2.0, xs[1].t)
