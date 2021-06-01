# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Acceptance test for tuples, points, and vectors."""


from dataclasses import dataclass
import logging
from typing import NamedTuple
import unittest

import pyray


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

    def __str__(self):
        return (f'@{self.clock}:'
                f' x={self.position.x:.2f}'
                f' y={self.position.y:.2f}'
                f' z={self.position.z:.2f}')


def run(env: Environment, proj: Projectile, logger: logging.Logger):
    """Repeatedly update a projectile by letting time pass until the
    projectile's y position is less than or equal to zero.

    Logss the projectile's position after each tick and logs the number of
    ticks it takes for the projetile to hit the ground.
    """
    while proj.position.y > 0.0:
        logger.info(proj)
        proj.tick(env)
    logger.info(
        f'Projectile hit the ground after {proj.clock} ticks!')


class TestPyray(unittest.TestCase):
    """Test case for firing virtual projectiles and seeing how far they go."""

    def test_tuples(self):
        """Test firing virtual projectiles and seeing how far they go."""
        gravity = pyray.vector(0.0, -0.1, 0.0)
        wind = pyray.vector(-0.01, 0.0, 0.0)
        env = Environment(gravity, wind)

        position = pyray.point(0.0, 1.0, 0.0)
        velocity = pyray.vector(1.0, 1.0, 0.0).normalized()
        proj = Projectile(position, velocity)

        with self.assertLogs(__name__) as recording:
            run(env, proj, logging.getLogger(__name__))
        self.assertEqual(
            [f'INFO:{__name__}:@0: x=0.00 y=1.00 z=0.00',
             f'INFO:{__name__}:@1: x=0.71 y=1.71 z=0.00',
             f'INFO:{__name__}:@2: x=1.40 y=2.31 z=0.00',
             f'INFO:{__name__}:@3: x=2.09 y=2.82 z=0.00',
             f'INFO:{__name__}:@4: x=2.77 y=3.23 z=0.00',
             f'INFO:{__name__}:@5: x=3.44 y=3.54 z=0.00',
             f'INFO:{__name__}:@6: x=4.09 y=3.74 z=0.00',
             f'INFO:{__name__}:@7: x=4.74 y=3.85 z=0.00',
             f'INFO:{__name__}:@8: x=5.38 y=3.86 z=0.00',
             f'INFO:{__name__}:@9: x=6.00 y=3.76 z=0.00',
             f'INFO:{__name__}:@10: x=6.62 y=3.57 z=0.00',
             f'INFO:{__name__}:@11: x=7.23 y=3.28 z=0.00',
             f'INFO:{__name__}:@12: x=7.83 y=2.89 z=0.00',
             f'INFO:{__name__}:@13: x=8.41 y=2.39 z=0.00',
             f'INFO:{__name__}:@14: x=8.99 y=1.80 z=0.00',
             f'INFO:{__name__}:@15: x=9.56 y=1.11 z=0.00',
             f'INFO:{__name__}:@16: x=10.11 y=0.31 z=0.00',
             f'INFO:{__name__}:Projectile hit the ground after 17 ticks!'],
            recording.output)
