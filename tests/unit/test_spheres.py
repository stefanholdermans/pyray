# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Unit tests for spheres."""

import math
import pyray
from .test_pyray import TestPyray


class TestSpheres(TestPyray):
    """Test case for spheres."""

    def test_intersections_object(self):
        """Assert that `Sphere.intersections` sets the object on the
        intersection.
        """
        r = pyray.Ray(pyray.point(0.0, 0.0, -5.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        xs = s.intersections(r)
        self.assertEqual(2, len(xs))
        self.assertEqual(s, xs[0].object)
        self.assertEqual(s, xs[1].object)

    def test_ray_intersecting_sphere_at_two_points(self):
        """Testing a ray intersecting a sphere at two points."""
        r = pyray.Ray(pyray.point(0.0, 0.0, -5.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        xs = s.intersections(r)
        self.assertEqual(2, len(xs))
        self.assertFloatsAlmostEqual(4.0, xs[0].t)
        self.assertFloatsAlmostEqual(6.0, xs[1].t)

    def test_ray_intersecting_sphere_at_tangent(self):
        """Test a ray intersecting a sphere at a tangent."""
        r = pyray.Ray(pyray.point(0.0, 1.0, -5.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        xs = s.intersections(r)
        self.assertEqual(2, len(xs))
        self.assertFloatsAlmostEqual(5.0, xs[0].t)
        self.assertFloatsAlmostEqual(5.0, xs[1].t)

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
        self.assertFloatsAlmostEqual(-1.0, xs[0].t)
        self.assertFloatsAlmostEqual(1.0, xs[1].t)

    def test_sphere_behind_ray(self):
        """Test a sphere behind a ray."""
        r = pyray.Ray(pyray.point(0.0, 0.0, 5.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        xs = s.intersections(r)
        self.assertEqual(2, len(xs))
        self.assertFloatsAlmostEqual(-6.0, xs[0].t)
        self.assertFloatsAlmostEqual(-4.0, xs[1].t)

    def test_default_sphere_transformation(self):
        """Test a sphere's default transformation."""
        s = pyray.Sphere()
        self.assertMatricesAlmostEqual(pyray.Matrix.identity(4), s.transform)

    def test_changing_sphere_transformation(self):
        """Test changing a sphere's transformation."""
        s = pyray.Sphere()
        s.translate(2.0, 3.0, 4.0)
        self.assertMatricesAlmostEqual(pyray.translation(2.0, 3.0, 4.0),
                                       s.transform)

    def test_scaled_sphere_intersection(self):
        """Test intersecting a scaled sphere with a ray."""
        r = pyray.Ray(pyray.point(0.0, 0.0, -5.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        s.scale(2.0, 2.0, 2.0)
        xs = s.intersections(r)
        self.assertEqual(2, len(xs))
        self.assertFloatsAlmostEqual(3.0, xs[0].t)
        self.assertFloatsAlmostEqual(7.0, xs[1].t)

    def test_translated_sphere_intersection(self):
        """Test intersecting a translated sphere with a ray."""
        r = pyray.Ray(pyray.point(0.0, 0.0, -5.0), pyray.vector(0.0, 0.0, 1.0))
        s = pyray.Sphere()
        s.translate(5.0, 0.0, 0.0)
        xs = s.intersections(r)
        self.assertEqual(0, len(xs))

    def test_normal_at_point_on_x_axis(self):
        """Test the normal on a sphere at a point on the x axis."""
        s = pyray.Sphere()
        n = s.normal_at(pyray.point(1.0, 0.0, 0.0))
        self.assertTuplesAlmostEqual(pyray.vector(1.0, 0.0, 0.0), n)

    def test_normal_at_point_on_y_axis(self):
        """Test the normal on a sphere at a point on the y axis."""
        s = pyray.Sphere()
        n = s.normal_at(pyray.point(0.0, 1.0, 0.0))
        self.assertTuplesAlmostEqual(pyray.vector(0.0, 1.0, 0.0), n)

    def test_normal_at_point_on_z_axis(self):
        """Test the normal on a sphere at a point on the z axis."""
        s = pyray.Sphere()
        n = s.normal_at(pyray.point(0.0, 0.0, 1.0))
        self.assertTuplesAlmostEqual(pyray.vector(0.0, 0.0, 1.0), n)

    def test_normal_at_nonaxial_point(self):
        """Test the normal on a sphere at a nonaxial point."""
        s = pyray.Sphere()
        n = s.normal_at(pyray.point(math.sqrt(3.0) / 3.0,
                                    math.sqrt(3.0) / 3.0,
                                    math.sqrt(3.0) / 3.0))
        self.assertTuplesAlmostEqual(pyray.vector(math.sqrt(3.0) / 3.0,
                                                  math.sqrt(3.0) / 3.0,
                                                  math.sqrt(3.0) / 3.0),
                                     n)

    def test_normal_is_normalized(self):
        """Assert that the normal is a normalized vector."""
        s = pyray.Sphere()
        n = s.normal_at(pyray.point(math.sqrt(3.0) / 3.0,
                                    math.sqrt(3.0) / 3.0,
                                    math.sqrt(3.0) / 3.0))
        self.assertTuplesAlmostEqual(n.normalized(),
                                     n)

    def test_normal_on_a_translated_sphere(self):
        """Test computing the normal on a translated sphere."""
        s = pyray.Sphere()
        s.translate(0.0, 1.0, 0.0)
        n = s.normal_at(pyray.point(0.0, 1.70711, -0.70711))
        self.assertTuplesAlmostEqual(pyray.vector(0.0, 0.70711, -0.70711), n)

    def test_normal_on_a_transformed_sphere(self):
        """Test computing the normal on a transformed sphere."""
        s = pyray.Sphere()
        s.rotate_z(math.pi / 5.0)
        s.scale(1.0, 0.5, 1.0)
        n = s.normal_at(
            pyray.point(0.0, math.sqrt(2.0) / 2.0, -math.sqrt(2.0) / 2.0))
        self.assertTuplesAlmostEqual(pyray.vector(0.0, 0.97014, -0.24254), n)
