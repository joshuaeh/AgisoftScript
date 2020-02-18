from Code.agisoftModularity import render_ply
import os
from pathlib import Path
from subprocess import Popen


results_folder = os.path.join('Results', 'testFolder')
render_ply(results_folder, 0)
