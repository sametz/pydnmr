import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))
import pydnmr


if __name__ == '__main__':
    pydnmr.main()