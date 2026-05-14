from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mini-coding-agent",
    version="0.1.0",
    author="Project K Team",
    description="A small agentic coder that produces patches for GitHub issues",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elinmelk/mini-coding-agent-SWE-Bench-Lite-Style",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
)
