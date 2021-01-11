# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Spheres."""

from collections.abc import Sequence
from dataclasses import dataclass
import math

from .intersections import Intersection
from .rays import Ray
from .tuples import point


@dataclass
class Sphere:
    """A sphere."""

    def intersections(self, ray: Ray) -> Sequence[Intersection]:
        """Return the intersections of a given ray with the sphere."""
        sphere_to_ray = ray.origin - point(0.0, 0.0, 0.0)

        a = ray.direction.dot(ray.direction)
        b = 2.0 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1.0

        discriminant = b * b - 4 * a * c

        if discriminant < 0.0:
            return ()

        t1 = (-b - math.sqrt(discriminant)) / (2.0 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2.0 * a)

        return (Intersection(t1, self), Intersection(t2, self))
