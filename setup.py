from setuptools import find_packages, setup

setup(
    name="matrix_spiral_retrieval",
    packages=find_packages(include=["matrix_spiral_retrieval"]),
    version="0.1.0",
    description="Python library for spiral iterating through given matrix",
    author="Andriy Sydorenko",
    install_requires=[
        "aiohttp",
        "aiofiles",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==7.4.2"],
)
