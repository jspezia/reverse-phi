### act.py ###

from tools import *
from pygame.locals import *
import pygame
import libpy as lb
import numpy as np
from libpy import RGBcolor as RGB


def stim(stim):
    ret = np.zeros([stim.shape[0], stim.shape[1], 3], dtype=int)
#     ret[:, :, 0] = stim[:, :]
#     ret[:, :, 1] = stim[:, :]
#     ret[:, :, 2] = stim[:, :]
    ret = stim[:, :, np.newaxis].astype(int)
    return ret

def creation_stimulus(info, screen):
    import MotionClouds as mc
    from libpy import lena

    if (info[figure] == 1):
        stimulus = (np.random.rand(info[NS_X], info[NS_Y]) > .5) * 255
    elif (info[figure] == 2):
        stimulus = lena()
        stimulus = np.rot90(np.fliplr(stimulus))
    else:
        fx, fy, ft = mc.get_grids(info[NS_X], info[NS_Y], 1)
        cloud = mc.random_cloud(mc.envelope_gabor(fx, fy, ft))
        cloud = mc.rectif(cloud, contrast=1.) * 255
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

def presentStimulus(win, stimulus, param, info):
    import time

    if (stimulus.ndim == 3):
        img1 = stim(stimulus[:, :, 0])
        img2 = stim(np.roll(stimulus[:, :, 0], param.shift, 1))
    else:
        img1 = stim(stimulus)
        img2 = stim(np.roll(stimulus, param.shift, 0))

    if param.contrast == -1:
        img2 = 255 - img2

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
        self.shift = lb.toss() * np.random.randint(shift_range)

def trials(win, info):
    import time

    stimulus = creation_stimulus(info, win.screen)
    results = np.zeros((4, info[nTrials]))
    for i_trial in range(info[nTrials]):
        param = parameters(info[shift_range])
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
        print "essai numero %d, contrast = %d, shift = %d, answer = %d, delay = %d" % (i_trial, param.contrast, param.shift, ans, delay)
    return(results)
