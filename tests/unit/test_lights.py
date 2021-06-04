# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Unit tests for lights."""

import pyray
from .test_pyray import TestPyray


class TestLights(TestPyray):
    """Test case for lights."""

    def test_point_light_has_position_and_intensity(self):
        """Assert that a point light has a position and intensity."""
        position = pyray.point(0.0, 0.0, 0.0)
        intensity = pyray.Color(1.0, 1.0, 1.0)
        light = pyray.PointLight(position, intensity)
        self.assertEqual(position, light.position)
        self.assertEqual(intensity, light.intensity)
