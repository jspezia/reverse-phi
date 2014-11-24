from src import *
from libpy import RGBcolor as RGB
from numpy import save

experiment = 'Reverse-phi-experiment'

info = Dlg()
fileName = fileSave(experiment, info[observer], info)
window = tools.init(info, experiment)
startend.intro(window, experiment)
results = act.trials(window, info)
startend.end(window)
print 'end of experience'
save(fileName, results)
#analyse(results)
