from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'a advanced useless package'
LONG_DESCRIPTION = 'a package that do idk just found what they do.'

# Setting up
setup(
    name="useless-pkg",
    version=VERSION,
    author="zaki",
    author_email="<rzaki9353@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=None,
    keywords=['python','useles', 'useless-pkg', 'useless package', 'useless pkg', 'useless python package', 'useless py pkg', 'useless py package', 'useless-python-package', 'useless-python-pkg', 'useless-py-package', 'useless-py-pkg'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
