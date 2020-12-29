# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

"""Matrices."""

from typing import List, Tuple


class Matrix:
    """A matrix."""

    num_rows: int
    num_cols: int
    cells: List[float]

    def __init__(self, num_rows: int, num_cols: int, cells: List[float]):
        assert len(cells) == num_rows * num_cols
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cells = cells

    def __getitem__(self, index: Tuple[int, int]) -> float:
        row, col = index
        return self.cells[row * self.num_cols + col]

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.num_rows != other.num_rows:
                return False

            if self.num_cols != other.num_cols:
                return False

            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    if self[row, col] != other[row, col]:
                        return False

            return True

        return NotImplemented


def matrix2x2(cells: List[float]) -> Matrix:
    """Create a 2x2 matrix."""
    return Matrix(2, 2, cells)


def matrix3x3(cells: List[float]) -> Matrix:
    """Create a 3x3 matrix."""
    return Matrix(3, 3, cells)


def matrix4x4(cells: List[float]) -> Matrix:
    """Create a 4x4 matrix."""
    return Matrix(4, 4, cells)
