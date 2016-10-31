"""htmlmeta_hub installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()
README = README.split("\n\n", 1)[0] + "\n"

setup(
    name="import_logger",
    description="Quick tool to log import statements",
    version="0.1.0",
    url="https://github.com/jvanasco/import_logger",
    author="Jonathan Vanasco",
    author_email="jonathan@findmeon.com",
    long_description=README,
    zip_safe=False,
    keywords="import logging memory",
    test_suite="tests",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
)
