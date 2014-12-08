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

def creation_stimulus(info, screen, param, name_database='blackwhite'):
    import MotionClouds as mc
    from MotionClouds.display import rectif

#   from libpy import lena

    if (param.condition == 1):
        stimulus = (np.random.rand(info[NS_X]/2, info[NS_Y]/2) > .5)
#        stimulus = (np.random.rand(64, 64) > .5)
    elif (param.condition == 2):
        im = Image(ParameterSet({'N_X' : info[NS_X], 'N_Y' : info[NS_Y], 'figpath':'.', 'matpath':'.', 'datapath':'database/', 'do_mask':False, 'seed':None}))
        stimulus, filename, croparea = im.patch(name_database)
#         stimulus = lena()
        stimulus = np.rot90(np.fliplr(stimulus))
        stimulus = rectif(stimulus, contrast=1.)
    else:
        fx, fy, ft = mc.get_grids(info[NS_X], info[NS_Y], 1)
        if (param.condition == 3):
            t, b, B_sf, sf_0 = 0, np.pi/32, 0.1, 0.15
        if (param.condition == 4):
            t, b, B_sf, sf_0= 0, np.pi/8, 0.1, 0.15
        if (param.condition == 5):
            t, b, B_sf, sf_0= 0, np.pi/2, 0.1, 0.15
        if (param.condition == 6):
            t, b, B_sf, sf_0= 0, np.pi/32, 0.1, 0.30
        if (param.condition == 7):
            t, b, B_sf, sf_0= 0, np.pi/32, 0.1, 0.075
        if (param.condition == 8):
            t, b, B_sf, sf_0= 0, np.pi/32, 0.25, 0.15
        if (param.condition == 9):
            t, b, B_sf, sf_0= 0, np.pi/32, 0.5, 0.15
        fx, fy, ft = mc.get_grids(info[NS_X], info[NS_Y], 1)
        cloud = mc.random_cloud(mc.envelope_gabor(fx, fy, ft, sf_0=sf_0, B_sf=B_sf, theta=t, B_theta=b, B_V=1000.))
        cloud = rectif(cloud, contrast=1.)
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
    if (param.condition == 1):
        pe = ParameterSet({'N_X' : info[NS_X]/2, 'N_Y' : info[NS_Y]/2, 'figpath':'.', 'matpath':'.'})
    else: pe = ParameterSet({'N_X' : info[NS_X], 'N_Y' : info[NS_Y], 'figpath':'.', 'matpath':'.'})
    im = Image(pe)
    if (stimulus.ndim == 3):
        img1 = stim(stimulus[:, :, 0])
        img2 = stim(im.translate(stimulus[:, :, 0], [param.shift, 0]))
    else:
        img1 = stim(stimulus)
        img2 = stim(im.translate(stimulus, [param.shift, 0]))

    if param.flip == -1:
        img2 = 255 - img2

    if do_mask:
        if (param.condition == 1):
            im = Image(ParameterSet({'N_X' : info[NS_X]/2, 'N_Y' : info[NS_Y]/2, 'figpath':'.', 'matpath':'.'}))
        else: im = Image(ParameterSet({'N_X' : info[NS_X], 'N_Y' : info[NS_Y], 'figpath':'.', 'matpath':'.'}))
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

class parameters():
    def __init__(self, exp, shift):#, shift_range):
        self.flip = lb.toss()
#         self.shift = (np.random.rand()*2 - 1) * shift_range
        if (exp == 'default'): a = [1, 2, 3]
        elif (exp == 'B_theta'): a = [3, 4, 5]
        elif (exp == 'theta'): a = [3, 6, 7]
        elif (exp == 'B_sf'): a = [3, 8, 9]
        if (abs(shift) - int(abs(shift)) < 0.334): index = 0
        elif (abs(shift) - int(abs(shift)) < 0.667): index = 1
        else: index = 2
#        index = np.random.randint(3)
        self.condition = a[index]
#        self.shift_ = index
        self.shift = shift

def trials(win, info, exp):
    import time
    shift_r = info[shift_range]
    shifts_ = np.linspace(-shift_r, shift_r, info[nTrials])
    shifts_ = np.random.permutation(shifts_)
#    shifts = []
#    for i in range(3):
#        shifts_ = np.linspace(-shift_r, shift_r, info[nTrials])
#        shifts_ = np.random.permutation(shifts_)
#        shifts.append(shifts_)
    results = np.zeros((5, info[nTrials]))
    for i_trial in range(info[nTrials]):
        param = parameters(exp, shifts_[i_trial])
#        param.shift = shifts[param.shift_][i_trial]
        stimulus = creation_stimulus(info, win.screen, param)
        wait(win, info[wait_stimulus])
        presentStimulus(win, stimulus, param, info)
        t0 = time.time()
        ans = get_reponse(win)
        t1 = time.time()
        delay = t1 - t0
        results[0, i_trial] = ans
        results[1, i_trial] = param.flip
        results[2, i_trial] = param.shift
        results[3, i_trial] = delay
        results[4, i_trial] = param.condition
        print "essai numero %d, condition %d, flip = %d, shift = %f, answer = %d, delay = %f" % (i_trial, param.condition, param.flip, param.shift, ans, delay)
    return(results)
