#! /usr/bin/env python

import shutil
import os
from tempfile import mkdtemp


tmp_dir = None


def setup():
    global tmp_dir
    tmp_dir = mkdtemp()
    os.chdir(tmp_dir)


def teardown():
    os.chdir(os.sep)  # To the root of the FS
    shutil.rmtree(tmp_dir)


def create_files(files, subdirectory=None):
    if subdirectory:
        os.makedirs(subdirectory)
    else:
        subdirectory = ''
    for fname in files:
        with open(os.path.join(subdirectory, fname), 'w'):
            pass


def _test_files_exist(files):
    for fname in files:
        assert os.path.exists(fname)


def _test_files_not_exist(files):
    for fname in files:
        assert not os.path.exists(fname)


def test_rof():
    create_files(['test'])
    os.utime('test', (0, 0))
    _test_files_exist(['test'])
    assert os.system("remove-old-files.py --older 100 .") == 0
    _test_files_not_exist(['test'])


def test_recursive():
    create_files(['test2'], 'subdir')
    test_file = os.path.join('subdir', 'test2')
    os.utime(test_file, (0, 0))
    _test_files_exist([test_file])
    assert os.system("remove-old-files.py --older 100 .") == 0
    _test_files_not_exist([test_file])
