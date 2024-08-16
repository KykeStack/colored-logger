from setuptools import setup, find_packages

setup(
    name="colored-logger",
    version="0.1.0",
    author="Enrique Orellana",
    description="A customized Python logger with color-coded log levels",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)