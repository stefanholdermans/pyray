# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Intersections."""

from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class Intersection:
    """An intersection."""

    t: float
    object: object


def intersections(*xs: Intersection) -> Sequence[Intersection]:
    """Create a sequence of intersections."""
    return xs
