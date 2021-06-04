# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""A photorealistic 3D renderer."""

from .canvases import Canvas
from .colors import Color, RED, GREEN, BLUE, BLACK, WHITE
from .intersections import Intersection, intersections, hit
from .lights import PointLight
from .materials import Material
from .matrices import Matrix, OrderError, NotInvertibleError
from .matrices import matrix2x2, matrix3x3, matrix4x4
from .rays import Ray
from .spheres import Sphere
from .transformations import translation, scaling
from .transformations import rotation_x, rotation_y, rotation_z
from .transformations import shearing
from .transformations import Transformation
from .tuples import Tuple, TupleTypeMismatchError, point, vector
