"""htmlmeta_hub installation script.
"""
import os
import re

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()
README = README.split("\n\n", 1)[0] + "\n"

# store version in the init.py
with open(
    os.path.join(os.path.dirname(__file__), "import_logger", "__init__.py")
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
    name="import_logger",
    version=VERSION,
    url="https://github.com/jvanasco/import_logger",
    author="Jonathan Vanasco",
    author_email="jonathan@findmeon.com",
    description="Quick tool to log import statements",
    long_description=README,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    py_modules=["import_logger"],
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
