#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='ppu',
      version='0.2.0',
      description='Broytman Portable Python Utilities',
      long_description=open('README.txt', 'rU').read(),
      author='Oleg Broytman',
      author_email='phd@phdru.name',
      url='http://phdru.name/Software/Python/ppu/',
      license='GPL',
      platforms=['any'],
      keywords=[''],
      classifiers=[
          'Development Status :: 3 - Alpha',
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
      scripts=['cmp.py', 'remove-old-files.py', 'rm.py'],
      )
