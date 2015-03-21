'''
Created on Mar 20, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

import unittest
from mock import Mock
from mock import ANY
from .. import process_wrapper

class ProcessWrapperTests(unittest.TestCase):

    def test__process_wrapper__kills_parent_and_child_processes(self):
        parent_process_mock = Mock()
        child_process_mock = Mock()
        process_wrapper.subprocess_module = Mock()
        process_wrapper.process_utility = Mock()
        process_wrapper.process_utility.Process = Mock(return_value=parent_process_mock)
        process_wrapper.process_utility.Process().children = Mock(return_value=iter([child_process_mock]))
        
        sample_command = 'background_process run'
        with process_wrapper.run_process('background_process run'):
            process_wrapper.subprocess_module.Popen.assert_any_call(
                sample_command.split(' '),
                stdout=ANY,
                stderr=ANY)
        
        parent_process_mock.kill.assert_any_call()
        child_process_mock.kill.assert_any_call()


if __name__ == "__main__":
    unittest.main()