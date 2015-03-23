'''
Created on Mar 21, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

from mock import Mock

import processwrapper.interfaces.process_utility_interface as process_utility


class ProcessUtilityMock(process_utility.ProcessUtilityInterface):

    class SampleException(Exception):
        pass

    def __init__(self):
        self.request_new_process_mock = Mock()
        self.kill_process_group_mock = Mock()
        self.ProcessDoesNotExist = self.SampleException

    def request_new_process(self, command):
        return self.request_new_process_mock(command)

    def kill_process_group(self, pid):
        return self.kill_process_group_mock(pid)
