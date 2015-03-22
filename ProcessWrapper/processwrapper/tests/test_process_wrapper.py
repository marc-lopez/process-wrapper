'''
Created on Mar 20, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

from mock import ANY

from .mocks import ProcessUtilityMock

from processwrapper import ProcessWrapper


class TestProcessWrapper(object):

    def setup_method(self, method):
        self.process_wrapper = ProcessWrapper(ProcessUtilityMock())
        self.process_utility = self.process_wrapper.process_utility
        self.sample_command = 'background_process run'

    def teardown_method(self, method):
        self.process_utility.kill_process_group_mock.assert_any_call(ANY)

    def test__process_wrapper__kills_parent_and_child_processes_on_exit(self):
        with self.process_wrapper.run_process(self.sample_command):
            self.process_utility.request_new_process_mock.assert_any_call(
                self.sample_command)

    def test__process_wrapper__handles_in_context_exceptions(self):
        from pytest import raises

        SampleException = BaseException
        with raises(SampleException):
            with self.process_wrapper.run_process(self.sample_command):
                raise SampleException

    def test__process_wrapper__does_nothing_with_zombie_processes(self):
        sample_pid = 1
        mock = self.process_utility.kill_process_group_mock.side_effect = \
            self.process_utility.ProcessDoesNotExist

        try:
            with self.process_wrapper.run_process(self.sample_command):
                pass
        except:
            fail_msg = 'Exception raised when it should not'
            raise AssertionError(fail_msg)


def test__sample_usage__works():
    import time
    from psutil import Process
    from processwrapper import run_process

    with run_process(
            'python bin/sample_background_process.py 1') as process:
        sample_process = Process(process.pid)
        assert sample_process.is_running()
        time.sleep(2)
    assert not sample_process.is_running()
