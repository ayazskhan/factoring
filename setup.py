from __future__ import absolute_import

import sys
import os
from setuptools import setup

# Change directories so this works when called from other locations. Useful in build systems that build from source.
setup_folder_loc = os.path.dirname(os.path.abspath(__file__))
os.chdir(setup_folder_loc)

# Add __version__, __author__, __authoremail__, __description__ to this namespace
path_to_package_info = os.path.join('.', 'factoring', 'package_info.py')
exec(open(path_to_package_info).read())

# These should be minimal requiments for the package to work, and avoid pinning dependencies unless required. See
# https://packaging.python.org/discussions/install-requires-vs-requirements/
install_requires = ['dwave-ocean-sdk>=3.0.0',
                    'jsonschema==3.2.0']

# Any extra requirements, to be used by pip install PACKAGENAME['keyname']
extras_require = {}

# The packages in this repo that are to be installed. Either list these explictly, or use setuptools.find_packages. If
# the latter, take care to filter unwanted packages (e.g. tests)
packages = ['factoring']

setup(
    name='factoring-demo',
    version=__version__,
    author=__author__,
    author_email=__authoremail__,
    description=__description__,
    long_description=open('README.md').read(),
    url='https://github.com/dwavesystems/factoring-demo',
    license='Apache 2.0',
    packages=packages,
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True
)
