# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

"""Firing virtual projectiles and seeing how far they go."""

from dataclasses import dataclass
from typing import NamedTuple
import pyray


class Environment(NamedTuple):
    # pylint: disable=inherit-non-class
    # pylint: disable=too-few-public-methods
    """A simulation environment."""
    gravity: pyray.Vector
    wind: pyray.Vector


@dataclass
class Projectile:
    """A virtual projectile."""

    position: pyray.Point
    velocity: pyray.Vector
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


def run(env: Environment, proj: Projectile):
    """Repeatedly update a projectile by letting time pass until the
    projectile's y position is less than or equal to zero.

    Report the projectile's position after each tick and report the number of
    ticks it takes for the projetile to hit the ground.
    """
    while proj.position.y > 0.0:
        print(proj)
        proj.tick(env)
    print(f'Projectile hit the ground after {proj.clock} ticks!')


def main():
    """Run the demo."""
    gravity = pyray.vector(0.0, -0.1, 0.0)
    wind = pyray.vector(-0.01, 0.0, 0.0)
    env = Environment(gravity, wind)

    position = pyray.point(0.0, 1.0, 0.0)
    velocity = pyray.vector(1.0, 1.0, 0.0).normalize()
    proj = Projectile(position, velocity)

    run(env, proj)


if __name__ == "__main__":
    main()
