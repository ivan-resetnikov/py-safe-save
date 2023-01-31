from setuptools import setup, find_packages



VERSION = '0.2'
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
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3",
		"Operating System :: Unix",
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: Microsoft :: Windows",
	]
)