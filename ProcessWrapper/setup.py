'''
Created on Mar 20, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

from setuptools import setup

setup(
    name = 'process-wrapper',
    version = '0.1.2',
    author = 'Marc Lopez',
    author_email = 'marc.rainier.lopez@gmail.com',
    packages = ['processwrapper', 'processwrapper.test'],
    scripts = ['bin/run_tests.py'],
    url = 'http://pypi.python.org/pypi/process-wrapper/',
    license = 'LICENSE.txt',
    description = 'Context manager for background command-line programs',
    long_description = open('README.txt').read(),
    install_requires = [
        'psutil>=2.2.1'],
    extras_require = {
        'tests': [
           'coverage>=3.7.1',
           'mock>=1.0.1',
           'nose>=1.3.4']})