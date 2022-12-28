from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md')) as f:
    long_description = f.read()

setup(
    name="logical-zonotope",
    version="0.1.0",
    description="Logical Zonotope Functions Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://arxiv.org/abs/2210.08596",
    author="Fargol Karamiyar",
    author_email="f.karamiyar@protonmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["logical_zonotope"],
    include_package_data=True
)
