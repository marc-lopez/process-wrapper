'''
Created on Mar 20, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)
'''

import os
import inspect

this_script_location = inspect.stack()[0][1]
try:
    os.chdir(os.path.dirname(this_script_location))
except:
    pass
os.chdir('..')
os.system('python -m processwrapper.test')