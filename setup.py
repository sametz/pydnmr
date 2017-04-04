from distutils.core import setup

setup(
    name='pydnmr',
    version='0.3.0',
    packages=['tests', 'pydnmr'],
    url='https://github.com/sametz/pydnmr',
    license='MIT',
    author='Geoffrey M. Sametz',
    author_email='sametz@udel.edu',
    description='Simulation of dynamic nuclear magnetic resonance (DNMR) spectra',
    requires=['PyQt5', 'pyqtgraph']
)
