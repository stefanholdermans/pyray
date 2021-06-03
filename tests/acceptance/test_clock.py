# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Acceptance test for matrix transformations."""


import math
import pyray
from .test_canvas import TestCanvas


class TestClock(TestCanvas):
    """Test case for picturing an analog clock."""

    def __init__(self, *args, **kwargs):
        super().__init__('clock.ppm', *args, **kwargs)

    def test_clock(self):
        """Test picturing an analog clock."""
        canvas_pixels = 100
        canvas = pyray.Canvas(canvas_pixels, canvas_pixels)

        radius = canvas_pixels * 3.0 / 8.0
        origin = canvas_pixels / 2.0
        scaling = pyray.scaling(radius, 0.0, radius)
        translation = pyray.translation(origin, 0.0, origin)

        twelve = pyray.point(0.0, 0.0, 1.0)
        for hour in range(12):
            rotation = pyray.rotation_y(hour * math.pi / 6.0)
            transform = pyray.Transformation()
            transform.add(rotation)
            transform.add(scaling)
            transform.add(translation)
            point = transform.apply(twelve)
            canvas[round(point.x), round(point.z)] = pyray.RED

        self.assertCanvas(canvas)
