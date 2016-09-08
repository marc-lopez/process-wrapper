===============
Process Wrapper
===============

[![Build Status](https://travis-ci.org/marc-lopez/process-wrapper.svg?branch=v0.2.x)](https://travis-ci.org/marc-lopez/process-wrapper)
[![Coverage Status](https://coveralls.io/repos/marc-lopez/process-wrapper/badge.svg?branch=v0.2.x)](https://coveralls.io/r/marc-lopez/process-wrapper?branch=master)

Process Wrapper is a simple module that executes a command-line style
program via a context manager. This is useful if you want your script
to do something that relies on a background process.

This module is conceived because of a need to automate the setup and
teardown of the Django server when running Robotframework tests. Sample
usage would look like this::

    #!/usr/bin/env python

    import robot
    from process_wrapper import run_process

    with run_process('python manage.py runserver'):
        robot.run('blackbox_test.robot')

Right now, the process being run is forcefully terminated with a SIGKILL
or equivalent signal on context exit. Caution is advised.

To install
==========
Run in command line:

    pip install process-wrapper

Dependencies
============
psutil

Tested Capabilities
===================
- Kills parent and child processes on exit
- Handles in-context exceptions: It still kills the called process and its children
- Process wrapper will do nothing if it encounters a Process Not Found exception for the parent process and raise all others
- Tested to work in win32 and linux2 platforms

Test Command Used
=================
Includes line and branch coverage. . Includes line and branch coverage:

    py.test processwrapper/tests --cov processwrapper --cov-report term-missing --pep8


Thanks to
=========
[jung rhew](http://stackoverflow.com/users/821632/jung-rhew) for providing 
[basis of process teardown code that I used](http://stackoverflow.com/a/27034438>)