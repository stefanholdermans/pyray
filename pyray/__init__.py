# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""A photorealistic 3D renderer."""

from .tuples import Tuple, Point, Vector, point, vector
from .canvases import Canvas, ppm
from .colors import Color
from .matrices import Matrix, OrderError, NotInvertibleError
from .matrices import matrix2x2, matrix3x3, matrix4x4
from .matrices import translation, scaling
from .matrices import rotation_x, rotation_y, rotation_z
from .matrices import shearing
