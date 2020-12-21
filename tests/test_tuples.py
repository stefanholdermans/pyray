# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.


"""Tests for tuples, points, and vectors."""

import unittest
import pyray


class TestTuples(unittest.TestCase):
    """Test case for tuples, points, and vectors."""

    def test_tuple(self):
        """Assert that tuples have x, y, z, and w components."""
        a = pyray.Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(4.3, a.x)
        self.assertEqual(-4.2, a.y)
        self.assertEqual(3.1, a.z)
        self.assertEqual(1.0, a.w)

    def test_tuple_is_point(self):
        """Assert that a tuple with w=1 is a point."""
        a = pyray.Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertTrue(a.is_point())
        self.assertFalse(a.is_vector())

    def test_tuple_is_vector(self):
        """Assert that a tuple with w=0 is a vector."""
        a = pyray.Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertFalse(a.is_point())
        self.assertTrue(a.is_vector())

    def test_point(self):
        """Assert that `pyray.point` creates tuples with w=1."""
        p = pyray.point(4.0, -4.0, 3.0)
        self.assertEqual(pyray.Tuple(4.0, -4.0, 3.0, 1.0), p)

    def test_vector(self):
        """Assert that `pyray.vector` creates tuples with w=0."""
        v = pyray.vector(4.0, -4.0, 3.0)
        self.assertEqual(pyray.Tuple(4.0, -4.0, 3.0, 0.0), v)
