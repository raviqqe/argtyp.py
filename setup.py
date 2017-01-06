import re
import setuptools
import sys


PACKAGE = "argtyp"


setuptools.setup(
    name=PACKAGE,
    version=re.search(r"__version__ *= *'([0-9]+\.[0-9]+\.[0-9]+)' *\n",
                      open(PACKAGE + "/__init__.py").read()).group(1),
    description="Argument type collection for argparse",
    long_description=open("README.md").read(),
    license="Public Domain",
    author="Yota Toyama",
    author_email="raviqqe@gmail.com",
    url="https://github.com/raviqqe/{}/".format(PACKAGE),
    packages=[PACKAGE],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Programming Language :: Python :: 3.5",
        "Topic :: Utilities",
    ],
)
