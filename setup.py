# (c) 2022, Abhimanyu Dubey
# This code is licensed under the MIT License (see license.txt for details)

import codecs
import os
import re

import setuptools


def find_version(*file_paths):
    here = os.path.abspath(os.path.dirname(__file__))

    def read(*parts):
        with codecs.open(os.path.join(here, *parts), "r") as fp:
            return fp.read()

    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open("README.md", encoding="utf8") as f:
    readme = f.read()

DISTNAME = "bandits"
DESCRIPTION = "Multi-armed Bandits in PyTorch."
LONG_DESCRIPTION = readme
AUTHOR = "Abhimanyu Dubey"

if __name__ == "__main__":
    setuptools.setup(
        name=DISTNAME,
        packages=setuptools.find_packages(),
        version=find_version(DISTNAME, "version.py"),
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=AUTHOR,
        setup_requires=["pytest-runner"],
        test_requires=["pytest"],
    )
