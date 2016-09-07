'''
Created on Mar 21, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass

class ProcessUtilityInterface(with_metaclass(ABCMeta)):
    
    ProcessDoesNotExist = BaseException

    @abstractmethod
    def request_new_process(self, *args, **kwargs):
        pass

    @abstractmethod
    def kill_process_group(self, pid):
        pass
