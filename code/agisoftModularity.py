from subprocess import Popen
import os
from pathlib import Path


def render_ply(results_folder, iteration_number):
    # create a folder for storage
    iteration_folder = os.path.join(results_folder, 'iteration_', + str(iteration_number))
    os.mkdir(iteration_folder)
    
    # execute Metashape script
    print('GENERATING MODEL WITH AGISOFT METASHAPE:')
    results_folder_arg = os.path.normpath(results_folder)
    process = Popen('cmd /c metashape.exe -r Code\\agisoftExecutable.py' + results_folder_arg + ' ' + str(iteration_number))
    process.wait()
    print('RENDER PLY STEP COMPLETE')

