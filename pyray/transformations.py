# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Matrix transformations."""

import math
from typing import Tuple as Pair

from .matrices import Matrix, OrderError
from .tuples import Tuple


class Transformation:
    """A matrix transformation constructed by concatenating individual
    transformation matrices.
    """

    _transform: Matrix

    def __init__(self):
        self._transform = Matrix.identity(4)

    def add(self, transform: Matrix):
        """Add a transformation matrix.

        Raises `OrderError` if the matrix is not a 4x4 matrix.
        """
        if transform.order != 4:
            raise OrderError

        self._transform = transform * self._transform

    def apply(self, t: Tuple) -> Tuple:
        """Apply the transformation to a tuple."""
        return self._transform * t


def translation(x: float, y: float, z: float) -> Matrix:
    """Construct a translation matrix."""
    transform = Matrix.identity(4)
    transform[0, 3] = x
    transform[1, 3] = y
    transform[2, 3] = z
    return transform


def scaling(x: float, y: float, z: float) -> Matrix:
    """Construct a scaling matrix."""
    transform = Matrix.identity(4)
    transform[0, 0] = x
    transform[1, 1] = y
    transform[2, 2] = z
    return transform


def rotation_x(r: float) -> Matrix:
    """Construct a matrix for rotating around the x axis."""
    transform = Matrix.identity(4)
    transform[1, 1] = math.cos(r)
    transform[1, 2] = -math.sin(r)
    transform[2, 1] = math.sin(r)
    transform[2, 2] = math.cos(r)
    return transform


def rotation_y(r: float) -> Matrix:
    """Construct a matrix for rotating around the y axis."""
    transform = Matrix.identity(4)
    transform[0, 0] = math.cos(r)
    transform[0, 2] = math.sin(r)
    transform[2, 0] = -math.sin(r)
    transform[2, 2] = math.cos(r)
    return transform


def rotation_z(r: float) -> Matrix:
    """Construct a matrix for rotating around the z axis."""
    transform = Matrix.identity(4)
    transform[0, 0] = math.cos(r)
    transform[0, 1] = -math.sin(r)
    transform[1, 0] = math.sin(r)
    transform[1, 1] = math.cos(r)
    return transform


def shearing(x: Pair[float, float] = (0.0, 0.0),
             y: Pair[float, float] = (0.0, 0.0),
             z: Pair[float, float] = (0.0, 0.0)) -> Matrix:
    """Construct a shearing matrix."""
    x_y, x_z = x
    y_x, y_z = y
    z_x, z_y = z

    transform = Matrix.identity(4)
    transform[0, 1] = x_y
    transform[0, 2] = x_z
    transform[1, 0] = y_x
    transform[1, 2] = y_z
    transform[2, 0] = z_x
    transform[2, 1] = z_y
    return transform
