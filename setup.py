"""htmlmeta_hub installation script.
"""
import os
import re

from setuptools import setup
from setuptools import find_packages

long_description = description = "Quick tool to log import statements"
try:
    here = os.path.abspath(os.path.dirname(__file__))
    long_description = open(os.path.join(here, "README.md")).read()
except:
    pass

# store version in the init.py
with open(
    os.path.join(os.path.dirname(__file__), "imports_logger", "__init__.py")
) as v_file:
    VERSION = re.compile(r'.*__VERSION__ = "(.*?)"', re.S).match(v_file.read()).group(1)

requires = [
    "psutil",
    "six",
]
tests_require = [
    "pytest",
]
testing_extras = tests_require + []


setup(
    name="imports_logger",
    version=VERSION,
    url="https://github.com/jvanasco/imports_logger",
    author="Jonathan Vanasco",
    author_email="jonathan@findmeon.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    zip_safe=False,
    keywords="import logging memory",
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        "testing": testing_extras,
    },
    test_suite="tests",
    include_package_data=True,
)
