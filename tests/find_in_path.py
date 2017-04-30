import os


def find_in_path(name):
    for path in os.environ["PATH"].split(os.pathsep):
        path = path.strip('"')
        test_prog_path = os.path.join(path, name)
        if os.path.exists(test_prog_path):
            return test_prog_path
