import os
from glob import glob
from setuptools import setup

exec(open("bolift/version.py").read())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bolift",
    version=__version__,
    description="BayesOPT with LIFT",
    author="Andrew White",
    author_email="white.d.andrew@gmail.com",
    url="https://github.com/whitead/bolift",
    license="MIT",
    packages=["bolift"],
    install_requires=["numpy", "langchain"],
    package_data={"bolift": ["rxn_data/*.json", "rxn_data/*.bz2"]},
    test_suite="tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
1