from libpy import psychoclone as psy
from libpy import RGBcolor as RGB
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
import time
import sys

observer = 0
screen_width = 1
screen_height = 2
N_X = 3
N_Y = 4
nTrials = 5
figure = 6
wait_stimulus = 7
duration_image = 8
shift_range = 9

class win:
    def __init__(self, background, screen):
        self.screen = screen
        self.background = background


def fileSave(experiment, observer, info):
    """
    save as 'experiment_observer_00_Jan_00h00.pickle'
    """
    import time
    import sys

    info_time = {}
    info_time['timeStr'] = time.strftime("%d_%b_%Hh%M", time.localtime())
    fileName = experiment + '_' + observer + '_' + info_time['timeStr']
    fileName = psy.fileSaveDlg(initFilePath = "", initFileName = fileName)
    if not isinstance(fileName, unicode):
        sys.exit()
    psy.toFile((fileName + '.pickle'), info)
    return(fileName)

def wait(win):
    print 'WAAAAIT!'
    win.background.fill(RGB.Gray)
    win.screen.blit(win.background, (0, 0))
    pygame.display.flip()
    time.sleep(2)
    return

def quit(event):
    _continue = True
    if event.type == QUIT:
        _continue = False
    if (event.type == KEYDOWN) and (event.key == K_ESCAPE):
        _continue = False
    if _continue == False:
        import sys
        pygame.quit()
        sys.exit()
    return(_continue)

def reponse(event):
    reponse = 0
    if (event.type == pygame.KEYDOWN):
        if (event.key == pygame.K_RIGHT): reponse = 1
        if (event.key == pygame.K_LEFT): reponse = -1
    return (reponse)

def Dlg():
    observer = 'none'
    screen_width = 1280
    screen_height = 800
    N_X = 128
    N_Y = 128
    nTrials = 2
    figure = 1
    wait_stimulus = 0.5
    duration_image = 1
    shift_range = 4
    myDlg = psy.Dlg(title="Reverse-phi's experiment")
    myDlg.addText('Subject Info')
    myDlg.addField('observer', observer)
    myDlg.addText('Screen size')
    myDlg.addField('screen_width', screen_width)
    myDlg.addField('screen_height', screen_height)
    myDlg.addText('Stimuli\'s size')
    myDlg.addField('N_X', N_X)
    myDlg.addField('N_Y', N_Y)
    myDlg.addField('nTrials', nTrials)
    myDlg.addText('Stimulus\'s figure')
    myDlg.addText('1- Pictogramm')
    myDlg.addText('2- Lena')
    myDlg.addText('3- MotionClouds')
    myDlg.addField('figure', figure)
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
