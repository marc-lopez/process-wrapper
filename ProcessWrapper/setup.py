'''
Created on Mar 20, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='process-wrapper',
    version='0.2.0',
    author='Marc Lopez',
    author_email='marc.rainier.lopez@gmail.com',
    packages=['processwrapper'],
    scripts=[],
    url='https://github.com/marc-lopez/process-wrapper',
    platforms=['linux2','win32'],
    license='LICENSE.txt',
    description='Context manager for background command-line programs',
    long_description=open('README.txt').read(),
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    install_requires=[
        'psutil>=2.2.1'
        ],
    tests_require=[
        'pytest',
        ],
    cmdclass={'test': PyTest},
    )
