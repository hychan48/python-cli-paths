import os
from pathlib import Path

import fire


# Description here

def hello(name="World"):
    """
    detail name here\n
    then description here
    name:str='World'
    hi
    """
    print(os.getcwd())  # wherever the terminal is at the moment
    # print(str(Path(__file__))) # need to combine perhaps
    # https://stackoverflow.com/questions/73440891/how-to-customize-the-default-help-text-for-the-command-line-python-fire-by-googl
    return "Hello %s!" % name


if __name__ == '__main__':
    fire.Fire(hello)
