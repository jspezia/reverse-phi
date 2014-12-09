### tools.py ###

from libpy import psychoclone as psy
from libpy import RGBcolor as RGB
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, RESIZABLE
import time
import sys

observer = 0
screen_width = 1
screen_height = 2
N_X = 3
N_Y = 4
NS_X = 5
NS_Y = 6
nTrials = 7
wait_stimulus = 8
duration_image = 9
shift_range = 10

class win:
    def __init__(self, background, screen):
        self.screen = screen
        self.background = background

def init(info, experiment):
    pygame.init()
    pygame.display.set_caption(experiment)
    size = (info[screen_width], info[screen_height])
    screen = pygame.display.set_mode(size, RESIZABLE)
    background = pygame.Surface(screen.get_size())
    background.fill(RGB.Gray)
    screen.blit(background, (0, 0))
    window = win(background, screen)
    return (window)

def saveResults(fileName, results, ext='.csv'):
    if (ext == '.npy'):
        import numpy
        numpy.save((fileName + '.npy'), results)
        return
    import pandas as pd

    ans = results[0][:]
    contrast = results[1][:]
    shift = results[2][:]
    delay = results[3][:]
    figure = results[4][:]
    Pd_results = zip(ans, contrast, shift, delay, figure)
    df = pd.DataFrame(data = Pd_results, columns=['ans', 'contrast', 'shift', 'delay', 'figure'])
    df.to_csv((fileName + '.csv'), index=False, header=True)

def fileSave(experiment, observer, info):
    """
    save info as 'experiment_observer_00_Jan_00h00.npy'
    and return a fileName without .ext
    """
    import time
    import sys

    info_time = {}
    info_time['timeStr'] = time.strftime("%d_%b_%Hh%M", time.localtime())
    dirName = 'ALL/'
    #fileName = dirName + experiment + '_' + observer + '_' + info_time['timeStr']
    fileName = dirName + experiment + '_' + info_time['timeStr']
    #fileName = psy.fileSaveDlg(initFilePath = "", initFileName = fileName)
    #if not isinstance(fileName, unicode):
    #    sys.exit()
    #psy.toFile((fileName + '.pickle'), info)
    return(fileName)

def wait(win, wait_stimulus):
    from startend import textedit

    win.background.fill(RGB.Gray)
    font = pygame.font.Font(None, 36)
    text = font.render('+', True, RGB.Black)
    textpos = text.get_rect(center=(win.background.get_width()/2, win.background.get_height()/2-18))
    win.background.blit(text, textpos)
    win.screen.blit(win.background, (0, 0))
    pygame.display.flip()
    time.sleep(wait_stimulus)
    return

def quit(event, option=0):
    _continue = True
    if event.type == QUIT:
        _continue = False
    if (event.type == KEYDOWN) and (event.key == K_ESCAPE):
        _continue = False
    if (_continue == False) and (option == 0):
        import sys
        pygame.quit()
        sys.exit()
    if (_continue == False) and (option == 1):
        pygame.quit()
    return(_continue)

def reponse(event):
    reponse = 0
    if (event.type == pygame.KEYDOWN):
        if (event.key == pygame.K_RIGHT): reponse = 1
        if (event.key == pygame.K_LEFT): reponse = -1
    return (reponse)

def Dlg2():
    name = 'anonymous'
    myDlg = psy.Dlg(title="info")
    myDlg.addField('Please enter your name or email:', name)
    myDlg.show()
    if myDlg.OK:
        info = myDlg.data
        ret = info[0]
    else: ret = 'anonymous'
    return(ret)

def Dlg():
    observer = 'none'
    screen_width = 1280
    screen_height = 800
    N_X = 512
    N_Y = 512
    NS_X = 512
    NS_Y = 512
    nTrials = 600
    figure = 2
    wait_stimulus = 0.1
    duration_image = .05
    shift_range = 30.
    myDlg = psy.Dlg(title="Reverse-phi's experiment")
    myDlg.addText('Subject Info')
    myDlg.addField('observer', observer)
    myDlg.addText('Screen size')
    myDlg.addField('screen_width', screen_width)
    myDlg.addField('screen_height', screen_height)
    myDlg.addText('Stimuli\'s size')
    myDlg.addField('N_X', N_X)
    myDlg.addField('N_Y', N_Y)
    myDlg.addText('Stimuli\'s definition')
    myDlg.addField('NS_X', NS_X)
    myDlg.addField('NS_Y', NS_Y)
    myDlg.addField('nTrials', nTrials)
    myDlg.addText('time data')
    myDlg.addField('wait_stimulus', wait_stimulus)
    myDlg.addField('duration_image', duration_image)
    myDlg.addText('Amplitude\'s range')
    myDlg.addField('shift_range', shift_range)
    myDlg.show()

    if myDlg.OK:
        info = myDlg.data
    else:
        print 'user cancelled'
        sys.exit()
    return(info)
