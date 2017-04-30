#! /usr/bin/env python

from time import time
import os
import shutil
import subprocess
import sys
from tempfile import mkdtemp
from find_in_path import find_in_path


tmp_dir = None
old_time = time() - 1000 * 24 * 3600  # 1000 days ago

test_prog_path = find_in_path('remove-old-files.py')
if not test_prog_path:
    sys.exit("Cannot find remove-old-files.py in %s" % os.environ["PATH"])


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


def assert_files_exist(files):
    if isinstance(files, str):
        files = [files]
    for fname in files:
        assert os.path.exists(fname)


def assert_files_not_exist(files):
    if isinstance(files, str):
        files = [files]
    for fname in files:
        assert not os.path.exists(fname)


def test_remove_old_files():
    create_files(['test1', 'test2'])
    assert_files_exist(['test1', 'test2'])
    os.utime('test2', (old_time, old_time))
    assert subprocess.call(
        [sys.executable, test_prog_path, "--older", "100", "."]) == 0
    assert_files_exist('test1')
    assert_files_not_exist('test2')


def test_recursive():
    create_files(['test3', 'test4'], 'subdir')
    test3 = os.path.join('subdir', 'test3')
    test4 = os.path.join('subdir', 'test4')
    assert_files_exist([test3, test4])
    os.utime(test4, (old_time, old_time))
    assert subprocess.call(
        [sys.executable, test_prog_path, "--older", "100", "."]) == 0
    assert_files_exist(test3)
    assert_files_not_exist(test4)


def test_remove_empty_directory():
    create_files(['test3', 'test4'], 'subdir')
    test3 = os.path.join('subdir', 'test3')
    test4 = os.path.join('subdir', 'test4')
    assert_files_exist([test3, test4])
    os.utime(test3, (old_time, old_time))
    os.utime(test4, (old_time, old_time))
    assert subprocess.call(
        [sys.executable, test_prog_path, "--older", "100", "."]) == 0
    assert_files_exist('subdir')
    assert_files_not_exist([test3, test4])
    assert subprocess.call(
        [sys.executable, test_prog_path, "-e", "--older", "100", "."]) == 0
    assert_files_not_exist('subdir')
