# setup.py
from setuptools import setup, find_packages

setup(
    name="serialization",
    version="0.1",
    packages=find_packages(),
    description="A package for serializing and deserializing data",
    author="sol239",
    author_email="239so239@gmail.com",
    url="https://github.com/sol239/ClassSerialization",
    license="GPL-3.0",
    install_requires=[],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
