#!/usr/bin/env python

import sys

try:
    from setuptools import setup
    is_setuptools = True
except ImportError:
    from distutils.core import setup
    is_setuptools = False

kw = {}
if is_setuptools:
    if (sys.version_info[:2] == (2, 6)):
        kw['install_requires'].append('argparse')

setup(name='ppu',
      version='0.3.2',
      description='Broytman Portable Python Utilities',
      long_description=open('README.rst', 'rU').read(),
      author='Oleg Broytman',
      author_email='phd@phdru.name',
      url='http://phdru.name/Software/Python/ppu/',
      license='GPL',
      platforms=['any'],
      keywords=[''],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      scripts=[
          'scripts/cmp.py', 'scripts/remove-old-files.py', 'scripts/rm.py',
      ],
      **kw
      )
