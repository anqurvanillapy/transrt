# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

short_description = "A very simple translator of SubRip file"

try:
    long_description = open("README.md").read()
except IOError:
    long_description = short_description

setup(
    name="transrt",
    version="0.1.0",
    description=short_description,
    license="MIT",
    author="AnqurVanillapy",
    author_email="anqurvanillapy@gmail.com",
    url="https://github.com/anqurvanillapy/transrt",
    packages=['transrt'],
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'transrt=transrt.transrt:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
