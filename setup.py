from setuptools import setup, find_packages

setup(
    name="ctf-toolkit",
    version="1.0.0",
    description="An automation toolkit for CTFs, Bug Bounties, and Vuln Disclosure.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "pwntools>=4.10.0",
        "requests>=2.28.0",
        "urllib3>=1.26.0",
        "colorama>=0.4.6"
    ],
    entry_points={
        "console_scripts": [
            "ctf-toolkit=core.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
