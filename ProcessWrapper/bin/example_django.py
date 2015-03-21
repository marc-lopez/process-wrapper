'''
Created on Mar 20, 2015

@author: Marc Lopez (marc.rainier.lopez@gmail.com)

Example usage of the process_wrapper package
'''

from processwrapper import run_process

with run_process('python manage.py runserver'):
    'Do something that requires the Django server running'