# PyTest
import sys
import pytest
import logging as log
import subprocess
from subprocess import *
import os
"""
remove dev / test
/home/ubuntu/.local/bin/poetry
/home/ubuntu/.virtualenvs/python-cli-paths/bin/activate
cd /tmp/pycharm_project_840/
"""

"""
https://docs.python.org/3/library/subprocess.html

want stdout, stderr, and code


look at atexit / with commands
"""

def test_name():
    """
    check is true will catch error? confirm
    :return:
    """
    # tmp = subprocess.run("echo hi", check=True, stdout=subprocess.PIPE)
    # tmp = run("echo hi", check=True, stdout=subprocess.PIPE)
    # os.system('echo hi') # this works...

    """
    https://stackoverflow.com/questions/3172470/actual-meaning-of-shell-true-in-subprocess
    The statement "Both work." about those 2 calls is incorrect and misleading. The calls work differently. Just switching from shell=True to False and vice versa is an error. From docs: "On POSIX with shell=True, (...) If args is a sequence, the first item specifies the command string, and any additional items will be treated as additional arguments to the shell itself.". On Windows there's automatic conversion, which might be undesired.
    """
    # works with shell on... wth
    tmp = check_output("echo hi `hostname -I`",shell=True) # works on both windows and my ubuntu
    tmps = run("echo hi", shell=True, stdout=subprocess.PIPE, check=True)
    log.warning(tmp)
    log.warning(tmps.stdout)
    # tmp = check_output("echo hi",shell=False) # while this fails for both ... so
    # args, retcode, stdout, stderr

def test_err_with_check_true():
    """works... but stderr goes to out"""
    try:
        tmps = run("ls ERR CHECK TRUE", shell=True, stdout=subprocess.PIPE, check=True)
        log.warning(tmps.stdout)
    except CalledProcessError as ex:
        log.warning(ex.cmd)
        log.warning(ex.stdout)
        log.warning(ex.stderr)
        log.warning(ex.returncode)

def test_err_with_check_stderr_to_stdout():
    """works... but stderr goes to out"""
    try:
        tmps = run("ls ERR CHECK TRUE", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
        log.warning(tmps.stdout)
    except CalledProcessError as ex:
        log.warning(ex.cmd)
        # b"'ls' is not recognized as an internal or external command,\r\noperable program or batch file.\r\n"
        log.warning(ex.stdout)
        log.warning(ex.stderr)
        log.warning(ex.returncode)

def test_err_with_check_stderr_to_stderr():
    """
    doesnt exist only pipe stdout and devnull
    i think this is the format i want it as...
    """
    try:
        tmps = run("ls ERR CHECK TRUE", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        log.warning(tmps.stdout)
        assert False
    except CalledProcessError as ex:
        log.warning(ex.cmd)
        # b"'ls' is not recognized as an internal or external command,\r\noperable program or batch file.\r\n"
        log.warning('stdout: ' + bytes.decode(ex.stdout,'ASCII'))
        # log.warning('stderr ' + str.decode(ex.stderr) ) # stderr
        # log.warning(ex.stderr) # stderr
        log.warning('stderr: ' + bytes.decode(ex.stderr,'ASCII')) # stderr
        # log.warning(bytes.decode(ex.stderr,'UTF-8')) # stderr. not sure which encoding. they both work
        # log.warning(bytes.decode(ex.stderr)) # this one is auto?
        log.warning('isascii ' + str(bytes.isascii(ex.stderr))) # is ascii for windows at least
        log.warning(str(ex.returncode))
        assert True

def test_err_without_err():
    """
    doesnt exist only pipe stdout and devnull
    i think this is the format i want it as...
    """
    try:
        tmps = run("echo hi", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        log.warning(tmps.stdout)
        assert True
    except CalledProcessError as ex:
        assert False
        log.warning(ex.cmd)
        # b"'ls' is not recognized as an internal or external command,\r\noperable program or batch file.\r\n"
        log.warning('stdout: ' + bytes.decode(ex.stdout,'ASCII'))
        # log.warning('stderr ' + str.decode(ex.stderr) ) # stderr
        # log.warning(ex.stderr) # stderr
        log.warning('stderr: ' + bytes.decode(ex.stderr,'ASCII')) # stderr
        # log.warning(bytes.decode(ex.stderr,'UTF-8')) # stderr. not sure which encoding. they both work
        # log.warning(bytes.decode(ex.stderr)) # this one is auto?
        log.warning('isascii ' + str(bytes.isascii(ex.stderr))) # is ascii for windows at least
        log.warning(str(ex.returncode))

if __name__ == '__main__':
    pytest.main(sys.argv)
