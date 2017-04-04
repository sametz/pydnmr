Installation and Use
====================

This is a work in progress. The main application (main.py) and its dependencies in the pydnmr subfolder should provide a basic, functional application, if the user is running Python 3.3+ and has the requirements listed in requirements.txt.

.. Warning::

    **Do not trust setup.py for installation** -- it has yet to be tested.

The brave and curious can copy main.py plus the pydnmr/pydnmr subfolder and its contents, install the dependencies, and run the program from the command line ::

    $ python main.py

If you are using Python 2 and/or PyQt5 in your default Python environment, it is recommended that you use a virtualenv, set it up with Python 3 and PyQt5, and install into that.

