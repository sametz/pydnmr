"""
Currently tests scripts are in the same directory as the python files being
tested. Attempts to use a separate 'tests' directory have failed because the
imports of main/nmrmath/nmrplot don't work. The solution from The
Hitchhiker's Guide to Python involves creating this context.py file in the
test folder and including "from .context import {name}" in the test
scripts....but that does not seem to work. Even the author's GitHub example
project structure results in tests failing to import modules if the code is
amended to actually use the module.

I am at a loss, but I'm preserving the tests directory in hopes that I'll be
able to get it to work in the future.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))
import pydnmr


if __name__ == '__main__':
    # for key in pydnmr.__dict__:
    #     print(key, pydnmr.__dict__[key])
    pydnmr.dnmrplot()
