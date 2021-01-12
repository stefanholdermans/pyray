# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Picturing an analog clock."""

import math
import pyray


RED: pyray.Color = pyray.Color(1.0, 0.0, 0.0)


def main():
    """Run the demo."""
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
        canvas[round(point.x), round(point.z)] = RED

    ppm = canvas.ppm()
    print(ppm, end="")


if __name__ == "__main__":
    main()
