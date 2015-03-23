from .process_wrapper import ProcessWrapper
from processwrapper.interfaces.process_utility import DefaultProcessUtility

from contextlib import contextmanager


default_process_wrapper = ProcessWrapper(DefaultProcessUtility())

@contextmanager
def run_process(command):
    """Runs a command-line program as a context.
    
    stdout and stderr are redirected to the subprocess pipe

    On exit, SIGKILL is sent to the parent and all of its
    child processes.

    Parameters
    ----------
    command : string
       Command-line program with necessary arguments and flags to be run.
       
    Tested Capabilities
    -------------------
    - Kills parent and child processes on exit
    - Handles in-context exceptions: It still kills the called process and its children
    - Processes are properly cleaned up when in-context exceptions occur
    - Process wrapper will do nothing if it encounters a Process Not Found exception for the parent process and raise all others
    - Tested to work in win32 and linux2 platforms

    Usage
    -----
    from processwrapper import run_process

    with run_process('program argument --flag'):
        do_something()
    """
    with default_process_wrapper.run_process(command) as process:
        yield process
