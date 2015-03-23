'''
Created on Mar 22, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

import subprocess
import inspect
from multiprocessing import Process, freeze_support

this_script_location = inspect.stack()[0][1]

def poll():
    while True:
        pass

if __name__ == '__main__':
    freeze_support()
    import time
    time.sleep(1)
    child = Process(target=subprocess.Popen, args=(
        'python {} child'.format(this_script_location),))
    child.start()
    
poll()
