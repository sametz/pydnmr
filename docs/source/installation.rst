Installation and Execution
==========================

For Windows and Mac OS X, the application is frozen as a single-file,
double-click-to-run application (see link above). Nothing besides the executable file needs to be installed. The description below is only for users that
want to download and run the Python source code itself.

The essential package components required to run the application are main.py plus the pydnmr subfolder and its contents. The application can be launched by running main.py: ::

    $ python main.py

The code should work for Python version 3.5 and up. The dependencies listed in requirements.txt are also required.
If pip is installed, the following command should automatically install the required dependencies::


>>>pip install -r requirements.txt

If you are familiar with virtual environments (e.g. using virtualenv, venv, or conda), you may wish to create one specifically for running this code, and install requirements there. If you use an Anaconda installation of Python, it is quite easy to set up and switch between different environments. See `the conda documentation`_ for details.

.. _the conda documentation: https://conda.io/docs/using/envs.html

