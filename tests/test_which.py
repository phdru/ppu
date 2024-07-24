#! /usr/bin/env python

import os
import subprocess
import sys

from ppu_tu import find_in_path
from ppu_tu import tmp_dir  # noqa: F401 tmp_dir imported but unused


test_prog_path = find_in_path('which.py')

if sys.platform == 'win32':
    os_env_pathext = os.environ['PATHEXT']
    pathext = os_env_pathext.lower().split(os.pathsep)
    if '.py' not in pathext:
        os_env_pathext += ';.py'
        os.environ['PATHEXT'] = os_env_pathext


def test_which():
    assert subprocess.check_output(
        [sys.executable, test_prog_path, "which.py"],
        universal_newlines=True).strip() == test_prog_path
    assert subprocess.check_output(
        [sys.executable, test_prog_path, "WhoWhereWhenceWhichWhereIs.py"],
        universal_newlines=True).strip() == ''
