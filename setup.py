"""Setup Python Library"""

import setuptools
import os

with open("README.md", "r" , encoding="utf-8" ) as fh:
    long_description = fh.read()

setuptools.setup(
    name="fs-client-test-lib-" + os.environ['SEMVAR'],
    version=os.environ['SEMVAR'] , 
    author="Steven Fawcett",
    author_email="Steven.fawcett@me.com",
    description="Flight Simulator Python Interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sfawcett123/PythonTest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
