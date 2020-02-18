import os
#import PhotoScan
import sys
import time
from pathlib import Path
import Code.firefly as firefly
import code.omega.whipped_python

'''Instructions:


To run on a computer with PhotoScan Pro:
    Enter the following lines in the command line sequentially:
        cd ../..
        cd "Program Files\Agisoft\Photoscan Pro\photoscan.exe.exe" -r "Users\Civil\Desktop\firefly\[main].py"
    This is effectively 1) navigating to the upper directory 2) "cd [path to agisoft exe] -r [path to executing file]
    As an alternative:
        1) Open Agisoft
        2) tools>run script
        3) select the [main].py file (this file)
        note: there will be no text output of feedback with this method

'''



'''
User Parameters
'''

# ---------- Project parameters-------------------

# Be careful to not repeat parameters for simplicity and clearness' sake
# Enter Project name here
project_title = 'test'
project_date = [00, 00, 00]  # format DD, MM, YY
iteration = 0  # creates subfolder for results of each iteration starting at 0






'''
Directory Creation
'''


'''
Agisoft Model Creation
'''


'''
Omega Model Creation
'''



