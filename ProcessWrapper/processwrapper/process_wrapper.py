'''
Created on Mar 20, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

from contextlib import contextmanager


class ProcessWrapper:
    
    def __init__(self, process_utility):
        self.process_utility = process_utility

    @contextmanager
    def run_process(self, command):
        process = self.process_utility.request_new_process(command)
        try:
            yield process
        except:
            raise
        finally:
            try:
                self.kill_process_group(process.pid)
            except self.process_utility.ProcessDoesNotExist:
                pass
            except:
                raise


    def kill_process_group(self, pid):
        self.process_utility.kill_process_group(pid)
