# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Acceptance test for drawing on a canvas."""


from dataclasses import dataclass
from typing import NamedTuple

import pyray
from .test_canvas import TestCanvas


class Environment(NamedTuple):
    # pylint: disable=inherit-non-class
    # pylint: disable=too-few-public-methods
    """A simulation environment."""
    gravity: pyray.Tuple  # A vector
    wind: pyray.Tuple  # A vector


@dataclass
class Projectile:
    """A virtual projectile."""

    position: pyray.Tuple  # A point
    velocity: pyray.Tuple  # A vector
    clock: int = 0

    def tick(self, env: Environment):
        """Let one unit of time pass."""
        self.position += self.velocity
        self.velocity += env.gravity + env.wind
        self.clock += 1

    def plot(self, c: pyray.Canvas):
        """Plot the projectile on a canvas."""
        x = round(self.position.x)
        y = c.height - round(self.position.y)
        c[x, y] = pyray.RED


def run(c: pyray.Canvas, env: Environment, proj: Projectile):
    """Repeatedly update a projectile by letting time pass until the
    projectile's y position is less than or equal to zero.

    Plots the projectile's position on a given canvas after each tick.
    """
    while proj.position.y > 0.0:
        proj.plot(c)
        proj.tick(env)


class TestPlotting(TestCanvas):
    """Test case for plotting the course of a virtual projectile on a canvas."""

    def __init__(self, *args, **kwargs):
        super().__init__('plotting.ppm', *args, **kwargs)

    def test_plotting(self):
        """Test plotting the course of a virtual projectile on a canvas."""
        gravity = pyray.vector(0.0, -0.1, 0.0)
        wind = pyray.vector(-0.01, 0.0, 0.0)
        env = Environment(gravity, wind)

        position = pyray.point(0.0, 1.0, 0.0)
        velocity = pyray.vector(1.0, 1.8, 0.0).normalized() * 11.25
        proj = Projectile(position, velocity)

        canvas = pyray.Canvas(900, 550)
        run(canvas, env, proj)

        self.assertCanvas(canvas)
