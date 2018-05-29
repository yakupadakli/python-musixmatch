#!/usr/bin/env python
# coding=utf-8

import uuid

from setuptools import setup, find_packages

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

install_requirements = parse_requirements('requirements.txt', session=uuid.uuid1())
requirements = [str(req.req) for req in install_requirements]

setup(
    name="python-musixmatch",
    version="1.0.0",
    description="A Python client for the Musixmatch API.",
    license="MIT",
    author="Yakup Adaklı",
    author_email="yakup.adakli@gmail.com",
    url="http://github.com/yakupadakli/python-musixmatch.git",
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    keywords="Musixmatch library lyrics tracks artist album music",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    zip_safe=True,
)
