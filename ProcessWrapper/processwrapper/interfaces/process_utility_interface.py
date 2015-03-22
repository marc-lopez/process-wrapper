'''
Created on Mar 21, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

from abc import ABCMeta, abstractmethod
from _pyio import __metaclass__


class ProcessUtilityInterface:
    __metaclass__ = ABCMeta
    
    ProcessDoesNotExist = BaseException

    @abstractmethod
    def request_new_process(self, *args, **kwargs):
        pass

    @abstractmethod
    def kill_process_group(self, pid):
        pass
