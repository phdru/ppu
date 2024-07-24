"""PPU test utilities"""

import os
import shutil
import sys
from tempfile import mkdtemp

import pytest


@pytest.fixture(autouse=True)
def tmp_dir():
    tmp_dir = mkdtemp()
    os.chdir(tmp_dir)
    yield
    os.chdir(os.sep)  # To the root of the FS
    shutil.rmtree(tmp_dir, ignore_errors=True)


def find_in_path(name):
    for path in os.environ["PATH"].split(os.pathsep):
        path = path.strip('"')
        test_prog_path = os.path.join(path, name)
        if os.path.exists(test_prog_path):
            return test_prog_path
    sys.exit("Cannot find %s in %s" % (name, os.environ["PATH"]))


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
