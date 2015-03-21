===========
Process Wrapper
===========

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

Dependencies
=========

psutil

For running tests
-------------

1. nose (for running tests conveniently, not essential)

2. mock

Thanks to
=========

`jung rhew <http://stackoverflow.com/users/821632/jung-rhew>` for providing 
the `basis of process teardown code that I used<http://stackoverflow.com/a/27034438>`