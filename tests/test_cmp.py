#! /usr/bin/env python

import os
import shutil
import subprocess
import sys
from tempfile import mkdtemp
from find_in_path import find_in_path


tmp_dir = None

test_prog_path = find_in_path('cmp.py')
if not test_prog_path:
    sys.exit("Cannot find cmp.py in %s" % os.environ["PATH"])


def setup():
    global tmp_dir
    tmp_dir = mkdtemp()
    os.chdir(tmp_dir)


def teardown():
    os.chdir(os.sep)  # To the root of the FS
    shutil.rmtree(tmp_dir)


def create_file(name, content):
    with open(name, 'w') as fp:
        fp.write(content)


def test_cmp_equal():
    create_file('test1', 'test')
    create_file('test2', 'test')
    assert subprocess.call(
        [sys.executable, test_prog_path, "-i", "test1", "test2"]) == 0

    create_file('test3', 'test3')
    create_file('test4', 'test4')
    assert subprocess.call(
        [sys.executable, test_prog_path, "-i", "test3", "test4"]) == 1
