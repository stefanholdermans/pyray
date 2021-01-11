# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Spheres."""

from dataclasses import dataclass
import math
from typing import List

from .rays import Ray
from .tuples import point


@dataclass
class Sphere:
    """A sphere."""

    def intersections(self, ray: Ray) -> List[float]:
        """Return the distances at which a given ray intersects the sphere."""
        del self  # Unused

        sphere_to_ray = ray.origin - point(0.0, 0.0, 0.0)

        a = ray.direction.dot(ray.direction)
        b = 2.0 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1.0

        discriminant = b * b - 4 * a * c

        if discriminant < 0.0:
            return []

        t1 = (-b - math.sqrt(discriminant)) / (2.0 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2.0 * a)

        return [t1, t2]
