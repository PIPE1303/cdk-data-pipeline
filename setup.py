#!/usr/bin/env python3
"""
Setup script for CDK Data Pipeline
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="cdk-data-pipeline",
    version="1.0.0",
    author="PIPE1303",
    author_email="your-email@example.com",
    description="A complete AWS data pipeline built with AWS CDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PIPE1303/cdk-data-pipeline",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black==23.3.0",
            "flake8==6.0.0",
            "mypy==1.3.0",
            "pytest==7.3.1",
            "pytest-cov==4.1.0",
            "pre-commit==3.3.2",
        ],
    },
    entry_points={
        "console_scripts": [
            "cdk-data-pipeline=app:main",
        ],
    },
)
