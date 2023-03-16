# PyTest
import sys
import pytest
import logging as log

import pandas as pd

"""
trying pandas df as dict?
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
"""

def test_df_to_dict():
    """

    :return:
    """
    df = pd.DataFrame({'col1': [1, 2],
                       'col2': [0.5, 0.75]},
                      index=['row1', 'row2'])
    log.warning(df)
    dd = df.to_dict()

    log.warning(dd)

def test_rnd_dict_to_pd():
    dd = {
      "a": {
        "b": {
          "c": "chello"
        },
        "d": "dhello"
      }
    }
    df = pd.DataFrame.from_dict(dd)
    log.warning(dd)
    log.warning(df) # doesnt really work
    log.warning(df) # doesnt really work



if __name__ == '__main__':
    pytest.main(sys.argv)
