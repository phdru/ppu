#!/usr/bin/env python

from imp import load_source
from os.path import abspath, dirname, join

try:
    from setuptools import setup
    is_setuptools = True
except ImportError:
    from distutils.core import setup
    is_setuptools = False

versionpath = join(abspath(dirname(__file__)), '{remove-old-files}', '__version__.py')
load_source('remove-old-files_version', versionpath)
# Ignore: E402 module level import not at top of file
from remove-old-files_version import __version__  # noqa

setup(name='{remove-old-files}',
      version=__version__,
      description='Broytman {remove-old-files}',
      long_description=open('README.txt', 'rtU').read(),
      author='Oleg Broytman',
      author_email='phd@phdru.name',
      url='http://phdru.name/Software/Python/',
      license='GPL',
      platforms=['any'],
      keywords=[''],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 2 :: Only',
      ],
      packages=['{remove-old-files}'],
      package_data={'{remove-old-files}': []},
      scripts=[],
      requires=[],
      )
