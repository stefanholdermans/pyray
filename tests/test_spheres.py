# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Tests for spheres."""

import pyray
from .test_pyray import TestPyray


class TestSpheres(TestPyray):
    """Test case for spheres."""

    def test_ray_intersecting_sphere_at_two_points(self):
        """Testing a ray intersecting a sphere at two points."""
        r = pyray.Ray(pyray.point(0.0, 0.0, -5.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        xs = s.intersections(r)
        self.assertEqual(2, len(xs))
        self.assertFloatsAlmostEqual(4.0, xs[0])
        self.assertFloatsAlmostEqual(6.0, xs[1])

    def test_ray_intersecting_sphere_at_tangent(self):
        """Test a ray intersecting a sphere at a tangent."""
        r = pyray.Ray(pyray.point(0.0, 1.0, -5.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        xs = s.intersections(r)
        self.assertEqual(2, len(xs))
        self.assertFloatsAlmostEqual(5.0, xs[0])
        self.assertFloatsAlmostEqual(5.0, xs[1])

    def test_ray_missing_sphere(self):
        """Test a ray missing a sphere."""
        r = pyray.Ray(pyray.point(0.0, 2.0, -5.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        xs = s.intersections(r)
        self.assertEqual(0, len(xs))

    def test_ray_originating_inside_sphere(self):
        """Test a ray originiating inside a sphere."""
        r = pyray.Ray(pyray.point(0.0, 0.0, 0.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        xs = s.intersections(r)
        self.assertEqual(2, len(xs))
        self.assertFloatsAlmostEqual(-1.0, xs[0])
        self.assertFloatsAlmostEqual(1.0, xs[1])

    def test_sphere_behind_ray(self):
        """Test a sphere behind a ray."""
        r = pyray.Ray(pyray.point(0.0, 0.0, 5.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        xs = s.intersections(r)
        self.assertEqual(2, len(xs))
        self.assertFloatsAlmostEqual(-6.0, xs[0])
        self.assertFloatsAlmostEqual(-4.0, xs[1])
