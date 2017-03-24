from distutils.core import setup

setup(
    name='pydnmr',
    version='0.1.0',
    packages=['tests', 'pydnmr'],
    url='',
    license='MIT',
    author='Geoffrey M. Sametz',
    author_email='sametz@udel.edu',
    description='Simulation of dynamic nuclear magnetic resonance (DNMR) spectra',
    requires=['PyQt5']
)
