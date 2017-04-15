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
    create_files(['test1', 'test2'])
    _test_files_exist(['test1', 'test2'])
    os.utime('test2', (0, 0))
    assert os.system("remove-old-files.py --older 100 .") == 0
    _test_files_exist(['test1'])
    _test_files_not_exist(['test2'])


def test_recursive():
    create_files(['test3', 'test4'], 'subdir')
    test3 = os.path.join('subdir', 'test3')
    test4 = os.path.join('subdir', 'test4')
    _test_files_exist([test3, test4])
    os.utime(test4, (0, 0))
    assert os.system("remove-old-files.py --older 100 .") == 0
    _test_files_exist([test3])
    _test_files_not_exist([test4])
