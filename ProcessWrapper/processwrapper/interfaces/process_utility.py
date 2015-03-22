'''
Created on Mar 21, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

import subprocess

from psutil import NoSuchProcess

from process_utility_interface import ProcessUtilityInterface


class DefaultProcessUtility(ProcessUtilityInterface):
    
    ProcessDoesNotExist = NoSuchProcess

    def request_new_process(self, command):
        return subprocess.Popen(
            command.split(' '),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    def kill_process_group(self, pid):
        from psutil import Process
        parent = Process(pid)
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()
