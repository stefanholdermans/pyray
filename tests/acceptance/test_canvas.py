# Copyright (c) 2020-2021 Stefan Holdermans.
# Licensed under the MIT License.

"""Canvas-test utilities."""

import os
import unittest
import pyray


class TestCanvas(unittest.TestCase):
    """Test case that can assert whether a canvas' PPM-formatted string
    representation matches the contents of a golden file.
    """

    def __init__(self, golden_file_name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        golden_file_dirname = f'{os.path.dirname(__file__)}/golden_files'
        self._golden_file_path = f'{golden_file_dirname}/{golden_file_name}'

    def assertCanvas(self, canvas: pyray.Canvas):
        # pylint: disable=invalid-name
        """Assert that the PPM-formatted string representation of a canvas
        matches the contents of the test case's golden file.
        """
        ppm = canvas.ppm()
        with open(self._golden_file_path) as golden_file:
            self.assertEqual(golden_file.read(), ppm)
