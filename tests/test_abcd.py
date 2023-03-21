# PyTest
import sys
import pytest
import logging as log
import os
from pathlib import Path
from os.path import expanduser
import python_cli_paths

"""
# Readme Python 3 Paths
* Path.home()
* PureWindowsPath('c:')
* Path.samefile(other_path)
* Path.mkdir(mode=0o777, parents=False, exist_ok=False)
* Path(__file__)
  * str(Path(__file__).parent.parent) 
    * root folder if __file__ is located. or import pkg.__file__
* Path(__path__[0])
  * not recommended
* Path.cwd()
* PurePath.parent

* shutils
  * copy2
```python
# project_dir = str(Path(python_cli_paths.__file__).parent.parent)
project_dir = str(Path.home().joinpath('PycharmProjects/python-cli-paths'))
Path.cwd()
```
"""



def test_name():
    log.warning("hi")
    path_input = "a/index.txt"
    cwd = os.getcwd()
    # os.chdir(path)
    log.warning(cwd)
    with open(str(Path(path_input))) as file_stream:
        for line in file_stream:
            log.warning(line)


# project_dir = str(Path(python_cli_paths.__file__).parent.parent)
project_dir = str(Path.home().joinpath('PycharmProjects/python-cli-paths'))
@pytest.mark.parametrize("test_input,expected", [
    (".", project_dir),
    ("..", project_dir),
    ("c:", project_dir),
    ("C:\\ProgramData\\ssh", project_dir),
])
def test_cwd_with_file_multi( test_input, expected):
    """
    Assuming cwd is tests/
    :param test_input:
    :param expected:
    :return:
    """
    try:
        os.chdir(test_input)
        log.warning(Path.cwd())
        actual = str(Path(python_cli_paths.__file__).parent.parent)
        assert actual == expected
    except AssertionError as aex:
        log.warning(actual)
        raise aex
    except Exception as ex:
        raise ex


def test_cwd_with_file():pass


if __name__ == '__main__':
    pytest.main(sys.argv)
