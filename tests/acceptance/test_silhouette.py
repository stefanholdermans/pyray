# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Acceptance test for ray-sphere intersection."""


import pyray
from .test_canvas import TestCanvas


class TestSilhouette(TestCanvas):
    """Test case for casting rays at a sphere and drawing the picture to a
    canvas.
    """

    def __init__(self, *args, **kwargs):
        super().__init__('silhouette.ppm', *args, **kwargs)

    def test_silhouette(self):
        """Test casting rays at a sphere and drawing the picture to a canvas."""
        ray_origin = pyray.point(0.0, 0.0, -5.0)
        wall_z = 10.0
        wall_size = 7.0
        half = wall_size / 2

        canvas_pixels = 100
        pixel_size = wall_size / canvas_pixels

        canvas = pyray.Canvas(canvas_pixels, canvas_pixels)
        shape = pyray.Sphere()

        for y in range(canvas.height):
            world_y = half - pixel_size * y

            for x in range(canvas.width):
                world_x = -half + pixel_size * x
                position = pyray.point(world_x, world_y, wall_z)

                r = pyray.Ray(ray_origin, (position - ray_origin).normalized())
                if pyray.hit(shape.intersections(r)):
                    canvas[x, y] = pyray.RED

        self.assertCanvas(canvas)
