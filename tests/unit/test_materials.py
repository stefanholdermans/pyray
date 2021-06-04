# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Unit tests for materials."""

import math
import pyray
from .test_pyray import TestPyray


class TestMaterials(TestPyray):
    """Test case for materials."""

    def setUp(self):
        self._material = pyray.Material()
        self._position = pyray.point(0.0, 0.0, 0.0)

    def test_default_material(self):
        """Test the default material."""
        self.assertEqual(pyray.WHITE, self._material.color)
        self.assertEqual(0.1, self._material.ambient)
        self.assertEqual(0.9, self._material.diffuse)
        self.assertEqual(0.9, self._material.specular)
        self.assertEqual(200.0, self._material.shininess)

    def test_lighting_with_eye_between_light_and_surface(self):
        """Test lighting with the eye between the light and the surface."""
        eyev = pyray.vector(0.0, 0.0, -1.0)
        normalv = pyray.vector(0.0, 0.0, -1.0)
        light = pyray.PointLight(pyray.point(0.0, 0.0, -10.0), pyray.WHITE)
        result = self._material.lighting(light, self._position, eyev, normalv)
        self.assertColorsAlmostEqual(pyray.Color(1.9, 1.9, 1.9), result)

    def test_lighting_with_eye_between_light_and_surface_and_45_degrees_offset(
        self
    ):
        """Test lighting with the eye between the light and the surface and 45
        degrees off the normal.
        """
        eyev = pyray.vector(0.0, math.sqrt(2.0) / 2.0, -math.sqrt(2.0) / 2.0)
        normalv = pyray.vector(0.0, 0.0, -1.0)
        light = pyray.PointLight(pyray.point(0.0, 0.0, -10.0), pyray.WHITE)
        result = self._material.lighting(light, self._position, eyev, normalv)
        self.assertColorsAlmostEqual(pyray.Color(1.0, 1.0, 1.0), result)

    def test_lighting_with_eye_opposite_to_surface_and_45_degrees_offset(self):
        """Test lighting with the eye opposite to the surface and 45 degrees off
        the normal.
        """
        eyev = pyray.vector(0.0, 0.0, -1.0)
        normalv = pyray.vector(0.0, 0.0, -1.0)
        light = pyray.PointLight(pyray.point(0.0, 10.0, -10.0), pyray.WHITE)
        result = self._material.lighting(light, self._position, eyev, normalv)
        self.assertColorsAlmostEqual(pyray.Color(0.7364, 0.7364, 0.7364),
                                     result)

    def test_lighting_with_eye_in_path_of_reflection_vector(self):
        """Test lighting with the eye in the path of the reflection vector."""
        eyev = pyray.vector(0.0, -math.sqrt(2.0) / 2.0, -math.sqrt(2.0) / 2.0)
        normalv = pyray.vector(0.0, 0.0, -1.0)
        light = pyray.PointLight(pyray.point(0.0, 10.0, -10.0), pyray.WHITE)
        result = self._material.lighting(light, self._position, eyev, normalv)
        self.assertColorsAlmostEqual(pyray.Color(1.6364, 1.6364, 1.6364),
                                     result)

    def test_lighting_with_light_behind_surface(self):
        """Test lighting with the eye behind the surface."""
        eyev = pyray.vector(0.0, 0.0, -1.0)
        normalv = pyray.vector(0.0, 0.0, -1.0)
        light = pyray.PointLight(pyray.point(0.0, 0.0, 10.0), pyray.WHITE)
        result = self._material.lighting(light, self._position, eyev, normalv)
        self.assertColorsAlmostEqual(pyray.Color(0.1, 0.1, 0.1), result)
