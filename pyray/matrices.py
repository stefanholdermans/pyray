# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

# pylint: disable=unsubscriptable-object

"""Matrices."""

from __future__ import annotations
from typing import Iterator, List, Optional, Tuple as Pair
from .tuples import Tuple


class Matrix():
    """A square matrix, i.e., a matrix with the same number of rows and columns.
    """

    _dim: int
    _cells: List[float]

    def __init__(self, order: int, cells: Optional[List[float]] = None):
        if order < 1:
            raise ValueError

        self._order = order
        self._cells = [0.0] * order * order

        if cells is not None:
            self._init_cells(cells)

    def _init_cells(self, cells: List[float]):
        if len(cells) != self.order * self.order:
            raise ValueError

        self._cells = cells

    @property
    def order(self):
        """Return the order of the matrix."""
        return self._order

    def _check_not_first_order(self):
        if self.order == 1:
            raise OrderError

    def __iter__(self) -> Iterator[Pair[int, int]]:
        rows = range(self.order)
        cols = range(self.order)
        yield from [(row, col) for row in rows for col in cols]

    def __getitem__(self, index: Pair[int, int]) -> float:
        row, col = index
        return self._cells[row * self.order + col]

    def __setitem__(self, index: Pair[int, int], cell: float):
        row, col = index
        self._cells[row * self.order + col] = cell

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.order != other.order:
                return False

            for row, col in self:
                if self[row, col] != other[row, col]:
                    return False

            return True

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.order != other.order:
                raise OrderError

            m = Matrix(self.order)
            for row, col in self:
                prods = [self[row, i] * other[i, col]
                         for i in range(self.order)]
                m[row, col] = sum(prods)
            return m

        if isinstance(other, Tuple):
            if self.order != 4:
                raise OrderError

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

    @staticmethod
    def identity(order: int) -> Matrix:
        """Return a square identity matrix."""
        m = Matrix(order)
        for i in range(order):
            m[i, i] = 1.0
        return m

    def transposed(self) -> Matrix:
        """Return the transposition of the matrix."""
        m = Matrix(self.order)
        for row, col in m:
            m[row, col] = self[col, row]
        return m

    def submatrix(self, row: int, col: int) -> Matrix:
        """Return the submatrix obtained by removing the specified row and
        column.

        Raises `OrderError` if the matrix is first-order.
        """
        self._check_not_first_order()
        submatrix = Matrix(self.order - 1)
        for dst_row, dst_col in submatrix:
            src_row = dst_row if row > dst_row else dst_row + 1
            src_col = dst_col if col > dst_col else dst_col + 1
            submatrix[dst_row, dst_col] = self[src_row, src_col]
        return submatrix

    def minor(self, row: int, col: int) -> float:
        """Return the minor of the matrix at the specified index.

        Raises `OrderError` if the matrix is first-order.
        """
        self._check_not_first_order()
        return self.submatrix(row, col).determinant()

    def cofactor(self, row: int, col: int) -> float:
        """Return the cofactor of the matrix at the specified index.

        Raises `OrderError` if the matrix is first-order.
        """
        self._check_not_first_order()
        minor = self.minor(row, col)
        return minor if (row + col) % 2 == 0 else -minor

    def determinant(self) -> float:
        """Return the determinant of the matrix."""
        if self.order == 1:
            return self[0, 0]

        acc = 0.0
        for col in range(self.order):
            acc += self[0, col] * self.cofactor(0, col)
        return acc

    def is_invertible(self) -> bool:
        """Return whether the matrix is invertible."""
        return self.determinant() != 0.0

    def inverse(self) -> Matrix:
        """Return the inverse of the matrix.

        Raises `NotInvertibleError` if the matrix is not invertible.
        """
        if not self.is_invertible():
            raise NotInvertibleError()

        det = self.determinant()
        m = Matrix(self.order)
        for row, col in m:
            c = self.cofactor(row, col) if not self.order == 1 else 1.0
            m[col, row] = c / det
        return m


class OrderError(Exception):
    """Raised when a matrix operation is invoked on a matrix of incompatible
    order.
    """


class NotInvertibleError(Exception):
    """Raised when a matrix cannot be inverted."""


def matrix2x2(cells: List[float]) -> Matrix:
    """Initialize a 2x2 matrix.

    Raise `ValueError` if `cells` provide too few or too many cell values.
    """
    return Matrix(2, cells)


def matrix3x3(cells: List[float]) -> Matrix:
    """Initialize a 3x3 matrix.

    Raise `ValueError` if `cells` provide too few or too many cell values.
    """
    return Matrix(3, cells)


def matrix4x4(cells: List[float]) -> Matrix:
    """Initialize a 4x4 matrix.

    Raise `ValueError` if `cells` provide too few or too many cell values.
    """
    return Matrix(4, cells)


def translation(x: float, y: float, z: float) -> Matrix:
    """Construct a translation matrix."""
    _ = x, y, z  # Unused
    transform = Matrix.identity(4)
    transform[0, 3] = x
    transform[1, 3] = y
    transform[2, 3] = z
    return transform
