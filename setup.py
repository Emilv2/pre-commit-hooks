import os

from setuptools import setup

if os.environ.get("CI_COMMIT_TAG"):
    version = os.environ["CI_COMMIT_TAG"]
else:
    version = "0.0.0"

setup(version=version)
