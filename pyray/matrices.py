# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

# pylint: disable=unsubscriptable-object

"""Matrices."""

from typing import List, Optional, Tuple as Pair
from .tuples import Tuple


class _Matrix:

    _num_rows: int
    _num_cols: int
    _cells: List[float]

    def __init__(self,
                 num_rows: int, num_cols: int,
                 cells: Optional[List[float]] = None):
        self._num_rows = num_rows
        self._num_cols = num_cols

        if cells is not None:
            assert len(cells) == num_rows * num_cols
            self._cells = cells
        else:
            self._cells = [0.0] * num_rows * num_cols

    def __getitem__(self, index: Pair[int, int]) -> float:
        row, col = index
        return self._cells[row * self._num_cols + col]

    def __setitem__(self, index: Pair[int, int], cell: float):
        row, col = index
        self._cells[row * self._num_cols + col] = cell

    def __eq__(self, other):
        if isinstance(other, _Matrix):
            if self._num_rows != other._num_rows:
                return False

            if self._num_cols != other._num_cols:
                return False

            for row in range(self._num_rows):
                for col in range(self._num_cols):
                    if self[row, col] != other[row, col]:
                        return False

            return True

        return NotImplemented


class Matrix2x2(_Matrix):
    # pylint: disable=too-few-public-methods
    """A 2x2 matrix."""

    def __init__(self, cells: Optional[List[float]] = None):
        super().__init__(2, 2, cells)


class Matrix3x3(_Matrix):
    # pylint: disable=too-few-public-methods
    """A 3x3 matrix."""

    def __init__(self, cells: Optional[List[float]] = None):
        super().__init__(3, 3, cells)


class Matrix4x4(_Matrix):
    # pylint: disable=too-few-public-methods
    """A 4x4 matrix."""

    def __init__(self, cells: Optional[List[float]] = None):
        super().__init__(4, 4, cells)

    def __mul__(self, other):
        if isinstance(other, Matrix4x4):
            m = Matrix4x4()
            for row in range(4):
                for col in range(4):
                    m[row, col] = (self[row, 0] * other[0, col]
                                   + self[row, 1] * other[1, col]
                                   + self[row, 2] * other[2, col]
                                   + self[row, 3] * other[3, col])
            return m

        if isinstance(other, Tuple):
            x = (self[0, 0] * other.x + self[0, 1] * other.y
                 + self[0, 2] * other.z + self[0, 3] * other.w)
            y = (self[1, 0] * other.x + self[1, 1] * other.y
                 + self[1, 2] * other.z + self[1, 3] * other.w)
            z = (self[2, 0] * other.x + self[2, 1] * other.y
                 + self[2, 2] * other.z + self[2, 3] * other.w)
            w = (self[3, 0] * other.x + self[3, 1] * other.y
                 + self[3, 2] * other.z + self[3, 3] * other.w)
            return Tuple(x, y, z, w)

        return NotImplemented
