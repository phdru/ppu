#!/usr/bin/env python

from imp import load_source
from os.path import abspath, dirname, join
from setuptools import setup

versionpath = join(abspath(dirname(__file__)), "ppu", "__version__.py")
ppu_version = load_source("ppu_version", versionpath)

setup(
    name='ppu',
    version=ppu_version.__version__,
    description='Broytman Portable Python Utilities',
    long_description=open('README.rst', 'rU').read(),
    long_description_content_type="text/x-rst",
    author='Oleg Broytman',
    author_email='phd@phdru.name',
    url='http://phdru.name/Software/Python/ppu/',
    project_urls={
        'Homepage': 'http://phdru.name/Software/Python/ppu/',
        'Documentation': 'http://phdru.name/Software/Python/ppu/docs/',
        'Download': 'https://pypi.python.org/pypi/ppu/%s'
        % ppu_version.__version__,
        'Git repo': 'http://git.phdru.name/ppu.git/',
        'Github repo': 'https://github.com/phdru/ppu',
        'Issue tracker': 'https://github.com/phdru/ppu/issues',
    },
    license='GPL',
    platforms='Any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['ppu'],
    scripts=[
        'scripts/cmp.py', 'scripts/remove-old-files.py', 'scripts/rm.py',
        'scripts/which.py',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
)
