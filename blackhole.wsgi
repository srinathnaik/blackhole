activate_this = '/home/siddu/testrun/blackhole/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0,'/home/siddu/testrun/blackhole')

from electron import app as application
