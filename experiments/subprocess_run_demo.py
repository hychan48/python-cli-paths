# PyTest
import sys
import pytest
import logging as log

"""
remove dev / test
/home/ubuntu/.local/bin/poetry
/home/ubuntu/.virtualenvs/python-cli-paths/bin/activate
cd /tmp/pycharm_project_840/
"""
def test_name():
    log.warning("hi")


if __name__ == '__main__':
    pytest.main(sys.argv)
