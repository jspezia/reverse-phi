import sys, pygame
from src import *
import MotionClouds as mc
from libpy import psychoclone as psy
from libpy import RGBcolor as RGB
from libpy import lena
from numpy import rot90, save
from numpy.random import rand
from pygame.locals import *

experiment = 'Reverse-phi experiment'

info = Dlg()

#fileName = fileSave(experiment, info[observer], info)

pygame.init()
pygame.display.set_caption(experiment)

size = (info[screen_width], info[screen_height])
screen = pygame.display.set_mode(size, RESIZABLE)

background = pygame.Surface(screen.get_size())
background.fill(RGB.Gray)

screen.blit(background, (0, 0))
window = win(background, screen)

startend.intro(window, experiment)
results = act.trials(window, info)
startend.end(window)
pygame.quit()
#save(fileName, results)
#analyse(results)
