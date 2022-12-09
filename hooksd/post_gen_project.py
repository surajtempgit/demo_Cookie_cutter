#!/usr/bin/python python

import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

print(PROJECT_DIRECTORY)

def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(path: str) -> None:
    shutil.rmtree(path)


if __name__ == '__main__':

    # if '{{ cookiecutter.UnitTesting }}' != 'y':
    #     print("=========================")
    #     remove_dir('project/src/test')
    pass