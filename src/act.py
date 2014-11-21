from tools import *
from pygame.locals import *
import pygame
import libpy as lb
import numpy as np
from libpy import RGBcolor as RGB


def stim(stim):
    ret = np.zeros([stim.shape[0], stim.shape[1], 3], dtype=int)
    ret[:, :, 0] = stim[:, :]
    ret[:, :, 1] = stim[:, :]
    ret[:, :, 2] = stim[:, :]
    print ret
    return(ret)

def creation_stimulus(info, screen):
    from MotionClouds import envelope_gabor, random_cloud
    from numpy import rot90
    from numpy.random import rand
    from pygame import surfarray
    from pygame import transform

    ret = np.zeros([info[N_X], info[N_Y], 3], dtype=int)
    if (info[figure] == 1):
        stimulus = stim((rand(64, 64) > .5)) * 255
    elif (info[figure] == 2):
        stimulus = lena()
        stimulus = stim(rot90(stimulus, 2))
#    else:
#        fx, fy, ft = mc.get_grids(info[N_X], info[N_Y], info[N_frame])
#        env = envelope_gabor(fx, fy, ft)
#        mov = random_cloud(env)
#        mov = rot90(mov)
#        stimulus = mov[:, :, info[N_frame]/2]
    surface = pygame.Surface(stimulus.shape[:2])
    surfarray.blit_array(surface, stimulus)
    surface = transform.scale(surface, (info[N_X], info[N_Y]))
    x = (info[screen_width] - info[N_X]) / 2
    y = (info[screen_height] - info[N_Y]) / 2
    screen.blit(surface, (x, y))
    looping = True
    rep = 0
    while looping:
        pygame.display.flip()
        event = pygame.event.poll()
        looping = quit(event)
        rep = reponse(event)
        if (rep != 0): looping = False
        print rep
    return(stimulus)



def presentStimulus(win, stimulus, contrast, shift):
    win.background.fill(RGB.Gray)
    win.screen.blit(win.background, (0, 0))
    looping = True
    print 'presentStimulus'
#    while looping:
#        pygame.display.flip()
#        event = pygame.event.poll()
#        looping = quit(event)
#        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
#            looping = False
    return

def trials(win, info):
    from numpy import zeros
    from numpy.random import randint

    stimulus = creation_stimulus(info, win.screen)
    results = zeros((3, info[nTrials]))
    for i_trial in range(info[nTrials]):
        contrast = lb.toss()
        shift = lb.toss() * randint(info[shift_range])
        wait(win)
        presentStimulus(win, stimulus, contrast, shift)
#        wait_for_response.draw()
#        win.flip()
#        ans = getResponse()
#        results[0, i_trial] = ans
        results[1, i_trial] = contrast
        results[2, i_trial] = shift
    return(results)
