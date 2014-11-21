### act.py ###

from tools import *
from pygame.locals import *
import pygame
import libpy as lb
import numpy as np
from libpy import RGBcolor as RGB
from NeuroTools.parameters import ParameterSet
from SLIP import Image


def stim(stim):
    ret = (stim[:, :, np.newaxis] * np.ones((1, 1, 3)) * 255).astype(int)
    return ret

def creation_stimulus(info, screen, param, name_database='Yelmo'):
    import MotionClouds as mc
    from libpy import lena

    if (param.figure == 1):
        stimulus = (np.random.rand(info[NS_X], info[NS_Y]) > .5)
    elif (param.figure == 2):
        im = Image(ParameterSet({'N_X' : info[NS_X], 'N_Y' : info[NS_Y], 'figpath':'.', 'matpath':'.', 'datapath':'database/', 'do_mask':False, 'seed':None}))
        stimulus, filename, croparea = im.patch(name_database)
#         stimulus = lena()
        stimulus = np.rot90(np.fliplr(stimulus))
        stimulus = mc.rectif(stimulus, contrast=1.)
    else:
        fx, fy, ft = mc.get_grids(info[NS_X], info[NS_Y], 1)
        cloud = mc.random_cloud(mc.envelope_gabor(fx, fy, ft))
        cloud = mc.rectif(cloud, contrast=1.)
        stimulus = cloud[:, :, 0]

    return (stimulus)

def winblit(img, win, info):
    from pygame import transform
    from pygame import surfarray

    surface = pygame.Surface(img.shape[:2])
    surfarray.blit_array(surface, img)
    surface = transform.scale(surface, (info[N_X], info[N_Y]))
    x = (info[screen_width] - info[N_X]) / 2
    y = (info[screen_height] - info[N_Y]) / 2
    win.screen.blit(surface, (x, y))
    pygame.display.flip()
    time.sleep(info[duration_image])

def presentStimulus(win, stimulus, param, info, do_mask=True):
    import time
    pe = ParameterSet({'N_X' : info[NS_X], 'N_Y' : info[NS_Y], 'figpath':'.', 'matpath':'.'})
    im = Image(pe)
    if (stimulus.ndim == 3):
        img1 = stim(stimulus[:, :, 0])
        img2 = stim(im.translate(stimulus[:, :, 0], [param.shift, 0]))# np.roll(stimulus[:, :, 0], param.shift, 1))
    else:
        img1 = stim(stimulus)
        img2 = stim(im.translate(stimulus, [param.shift, 0]))# np.roll(stimulus, param.shift, 0))

    if param.contrast == -1:
        img2 = 255 - img2

    if do_mask:
        im = Image(ParameterSet({'N_X' : info[NS_X], 'N_Y' : info[NS_Y], 'figpath':'.', 'matpath':'.'}))
        mask = im.mask[:, :, np.newaxis] 
        img1 = ((img1 - 127)*mask + 127).astype(int)
        img2 = ((img2 - 127)*mask + 127).astype(int)

    win.background.fill(RGB.Gray)
    win.screen.blit(win.background, (0, 0))
    winblit(img1, win, info)
    winblit(img2, win, info)

def get_reponse(win):
    win.background.fill(RGB.Gray)
    win.screen.blit(win.background, (0, 0))
    pygame.display.flip()
    ans = 0
    while (ans == 0):
        event = pygame.event.poll()
        ans = reponse(event)
    return (ans)

class parameters:
    def __init__(self, shift_range):
        self.contrast = lb.toss()
        self.shift = np.random.randn() * shift_range
        self.figure = np.random.randint(3) + 1

def trials(win, info):
    import time

    results = np.zeros((5, info[nTrials]))
    for i_trial in range(info[nTrials]):
        param = parameters(info[shift_range])
        stimulus = creation_stimulus(info, win.screen, param)
        wait(win, info[wait_stimulus])
        presentStimulus(win, stimulus, param, info)
        t0 = time.time()
        ans = get_reponse(win)
        t1 = time.time()
        delay = t1 - t0
        results[0, i_trial] = ans
        results[1, i_trial] = param.contrast
        results[2, i_trial] = param.shift
        results[3, i_trial] = delay
        results[4, i_trial] = param.figure
        print "essai numero %d, figure %d, contrast = %d, shift = %f, answer = %d, delay = %f" % (i_trial, param.figure, param.contrast, param.shift, ans, delay)
    return(results)
