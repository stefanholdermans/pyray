# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

# Prevent pylint from mistakenly reporting that `Optional` is unsubscriptable:
#   pylint: disable=unsubscriptable-object
# See https://github.com/PyCQA/pylint/issues/3882.

"""Intersections."""

from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from typing import Optional


@dataclass
class Intersection:
    """An intersection."""

    t: float
    object: object


def intersections(*xs: Intersection) -> Sequence[Intersection]:
    """Create a sequence of intersections."""
    return xs


def hit(xs: Iterable[Intersection]) -> Optional[Intersection]:
    """Identify the visible intersection from a ray's origin."""
    xs = [i for i in xs if i.t >= 0.0]
    xs = sorted(xs, key=lambda i: i.t)
    return xs[0] if len(xs) > 0 else None
