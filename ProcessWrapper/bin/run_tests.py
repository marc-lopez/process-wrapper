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

test_command = 'nosetests'
working_directory_change = '-w ..'
activate_coverage_flag = '--with-coverage'
erase_previous_coverage_flag = '--cover-erase'
cover_branches_flag = '--cover-branches'
dump_cover_data_to_xml_flag = '--cover-xml'
xml_coverage_file = '--cover-xml-file=../coverage.xml'
coveraged_package = '--cover-package=processwrapper'

os.system(' '.join([
   test_command,
   working_directory_change,
   activate_coverage_flag,
   erase_previous_coverage_flag,
   cover_branches_flag,
   dump_cover_data_to_xml_flag,
   xml_coverage_file,
   coveraged_package]))