import os
from io import open

import versioneer
versioneer.versionfile_source = 'catchment_cutter/_version.py'
versioneer.versionfile_build = 'catchment_cutter/_version.py'
versioneer.tag_prefix = 'v'
versioneer.parentdir_prefix = 'catchment_cutter-'

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = ''.join([
            line for line in f.readlines() if 'travis-ci' not in line
        ])

setup(
    name='catchment_cutter',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Library for selecting grid points based on catchment boundaries.',
    long_description=long_description,
    author='Andrew MacDonald',
    author_email='andrew@maccas.net',
    license='BSD',
    url='https://github.com/amacd31/catchment_cutter',
    install_requires=['numpy', 'gdal', 'shapely', 'fiona'],
    packages = ['catchment_cutter'],
    test_suite = 'tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
