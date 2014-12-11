from src import *
from libpy import RGBcolor as RGB
from numpy import save
import sys

experiment = 'Reverse-phi-experiment'
#if (len(sys.argv) != 2):
#	sys.exit("set argv[1] to \'default\', \'B_theta\', \'theta\' or \'B_sf\'")
#else:
#	exp = sys.argv[1]
#if (exp != 'default' and exp != 'B_theta' and exp != 'theta' and exp != 'B_sf'):
#	sys.exit("set argv[1] to \'default\', \'B_theta\', \'theta\' or \'B_sf\'")

expT = ['default', 'B_theta', 'theta', 'B_sf']
i = 0

info = Dlg()
while (True):
    exp = expT[i]
    fileName = fileSave2()
    window = tools.init(info, experiment)
    fileName = startend.intro(window, experiment, fileName)
    results = act.trials(window, info, exp)
    startend.end(window)
    saveResults(fileName, results, info[9], ext='.csv')
    #analyse(results)
    i += 1
    if (i == 4): i = 0
