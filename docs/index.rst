.. remove-old-files documentation master file, created by
   sphinx-quickstart on Sat Apr 15 20:37:34 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to remove-old-files's documentation!
============================================

Remove old files. It's a portable replacement for
`find start_dir -type f -mtime +31 -delete`.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   news

.. highlight:: none

Command line
------------

remove-old-files.py
~~~~~~~~~~~~~~~~~~~

Usage::

    remove-old-files.py -o days start_dir

Options::

    -e, --empty-dirs
                           remove empty directories
    -o days, --older days
                           remove files older than this number of days;
                           this is a required option

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
