# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Materials."""

from dataclasses import dataclass
from .colors import Color, BLACK, WHITE
from .lights import PointLight
from .tuples import Tuple, TupleTypeMismatchError


@dataclass
class Material:
    """A material."""

    color: Color = WHITE
    ambient: float = 0.1
    diffuse: float = 0.9
    specular: float = 0.9
    shininess: float = 200.0

    def lighting(
        self, light: PointLight, point: Tuple, eyev: Tuple, normalv: Tuple
    ) -> Color:
        """Illuminate the material at a specified point for a given light source
        and given eye and normal vectors.

        Raises `TupleTypeMismatchError` if `point` is not a point or if any of
        `eyev` and `normalv` are not vectors.
        """
        if not (point.is_point() or eyev.is_vector() or normalv.is_vector()):
            raise TupleTypeMismatchError

        effective_color = self.color * light.intensity

        ambient = effective_color * self.ambient

        lightv = (light.position - point).normalized()
        light_dot_normal = lightv.dot(normalv)

        if light_dot_normal < 0.0:
            diffuse = BLACK
            specular = BLACK
        else:
            diffuse = effective_color * self.diffuse * light_dot_normal

            reflectv = -lightv.reflected(normalv)
            reflect_dot_eye = reflectv.dot(eyev)

            if reflect_dot_eye <= 0.0:
                specular = BLACK
            else:
                factor = reflect_dot_eye ** self.shininess
                specular = light.intensity * self.specular * factor

        return ambient + diffuse + specular
