from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
	long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = 'Python module to store data and encrypt it with two security layers.'


# Setting up
setup(
	name="pySafeSave",
	version=VERSION,
	author="LowRezCat (Ivan Resetnikov)",
	author_email="ivan.resetnikov.alpha@gmail.com",
	description=DESCRIPTION,
	packages=find_packages(),
	install_requires=[],
	keywords=['python', 'save', 'safe', 'write', 'encrypt', 'encode', 'security'],
	classifiers=[
		"Development Status :: 1 - Releasing",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3",
		"Operating System :: Unix",
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: Microsoft :: Windows",
	]
)