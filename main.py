from src import *
from libpy import RGBcolor as RGB
from numpy import save
import sys

experiment = 'Reverse-phi-experiment'
if (len(sys.argv) != 2):
	sys.exit("set argv[1] to \'default\', \'B_theta\', \'theta\' or \'B_sf\'")
else:
	exp = sys.argv[1]
if (exp != 'default' and exp != 'B_theta' and exp != 'theta' and exp != 'B_sf'):
	sys.exit("set argv[1] to \'default\', \'B_theta\', \'theta\' or \'B_sf\'")

info = Dlg()
fileName = fileSave(experiment, info[observer], info)
window = tools.init(info, experiment)
startend.intro(window, experiment)
results = act.trials(window, info, exp)
startend.end(window)
print 'end of experience'
saveResults(fileName, results, ext='.csv')
#analyse(results)
