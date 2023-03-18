# PyTest
import sys
import pytest
import logging as log

from dataclasses import dataclass, asdict
# import bla bla from "str_package_name"
def test_name():
    @dataclass
    class InventoryItem:
        """Class for keeping track of an item in inventory."""
        name: str
        unit_price: float = None
        quantity_on_hand: int = None
        def as_dict(self):
            return asdict(self)

        def __init__(self):
            pass
        def dict_filtered(self):
            """"""
            # self.ssh.ex

    ii = InventoryItem()
    ii.name = 'hi'
    log.warning(ii.as_dict())


if __name__ == '__main__':
    pytest.main(sys.argv)
