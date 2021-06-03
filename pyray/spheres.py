# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Spheres."""

from collections.abc import Sequence
import math
from typing import Tuple as Pair

from .intersections import Intersection
from .matrices import Matrix
from .rays import Ray
from .transformations import Transformation
from .transformations import translation, scaling
from .transformations import rotation_x, rotation_y, rotation_z
from .transformations import shearing
from .tuples import Tuple, TupleTypeMismatchError, point


class Sphere:
    """A sphere."""

    def __init__(self):
        self._transformation = Transformation()

    @property
    def transform(self) -> Matrix:
        """The sphere's transformation matrix."""
        return self._transformation.matrix

    @property
    def inverse_transform(self) -> Matrix:
        """The sphere's inversed transformation matrix."""
        return self.transform.inverse()

    def translate(self, x: float, y: float, z: float):
        """Translate the sphere."""
        transform = translation(x, y, z)
        self._transformation.add(transform)

    def scale(self, x: float, y: float, z: float):
        """Scale the sphere."""
        transform = scaling(x, y, z)
        self._transformation.add(transform)

    def rotate_x(self, r: float):
        """Rotate the sphere around the x axis."""
        transform = rotation_x(r)
        self._transformation.add(transform)

    def rotate_y(self, r: float):
        """Rotate the sphere around the y axis."""
        transform = rotation_y(r)
        self._transformation.add(transform)

    def rotate_z(self, r: float):
        """Rotate the sphere around the z axis."""
        transform = rotation_z(r)
        self._transformation.add(transform)

    def shear(self,
              x: Pair[float, float] = (0.0, 0.0),
              y: Pair[float, float] = (0.0, 0.0),
              z: Pair[float, float] = (0.0, 0.0)):
        """Shear the sphere."""
        transform = shearing(x, y, z)
        self._transformation.add(transform)

    def intersections(self, ray: Ray) -> Sequence[Intersection]:
        """Return the intersections of a given ray with the sphere."""
        ray = ray.transformed(self.inverse_transform)
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

    def normal_at(self, world_point: Tuple) -> Tuple:
        """Return the normal on the sphere at a given point."""
        if not world_point.is_point():
            raise TupleTypeMismatchError

        object_point = self.inverse_transform * world_point
        object_normal = object_point - point(0.0, 0.0, 0.0)
        world_normal = self.inverse_transform.transposed() * object_normal
        world_normal.w = 0.0
        return world_normal.normalized()
