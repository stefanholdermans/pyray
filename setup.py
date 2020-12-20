# Copyright (c) 2020 Stefan Holdermans.
# Licensed under the MIT License.

"""Setup script for pyray."""

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="pyray",
    version="0.0.1",
    author="Stefan Holdermans",
    author_email="stefan@holdermans.nl",
    description="A photorealistic 3D renderer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stefanholdermans/pyray",
    packages=["pyray"],
    data_files=["LICENSE"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7",
)
