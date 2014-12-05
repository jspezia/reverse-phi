### startend.py ###

from tools import *
from pygame.locals import *
import pygame
from libpy import RGBcolor as RGB


def textedit(background, line, num):
    font = pygame.font.Font(None, 36)
    text = font.render(line, True, RGB.Black)
    textpos = text.get_rect(center=(background.get_width()/2, (background.get_height()/9)*num))
    background.blit(text, textpos)
    return (background)

def textedit2(background, line, num):
    font = pygame.font.Font(None, 36)
    text = font.render(line, True, RGB.Black)
    textpos = text.get_rect(center=(background.get_width()/8, (background.get_height()/16)*num))
    background.blit(text, textpos)
    return (background)

def weneedyou(win):
    from pygame import transform
    win.background = pygame.image.load("img/we-need-you.jpg").convert()
    win.background = transform.scale(win.background, win.screen.get_size())
    win.background = textedit2(win.background, 'press enter', 1)
    win.background = textedit2(win.background, 'to start', 2)
    win.background = textedit2(win.background, 'the experiment', 3)
    win.screen.blit(win.background, (0, 0))
    looping = True
    while looping:
        pygame.display.flip()
        event = pygame.event.poll()
        looping = quit(event)
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
            looping = False
    win.background.fill(RGB.Gray)
    win.screen.blit(win.background, (0, 0))
    return

def intro(win, experiment, fileName):
    weneedyou(win)
    fileName += '_' + Dlg2()
    win.background = textedit(win.background, experiment, 1)
    win.background = textedit(win.background, 'For each tries, you need to determine which way the presented image has moved.', 3)
    win.background = textedit(win.background, 'Use the arrow keys (left and right) to make your choice.', 4)
    win.background = textedit(win.background, 'one block takes about 3 min', 5)
    win.background = textedit(win.background, 'press enter if you are ready', 7)
    win.screen.blit(win.background, (0, 0))
    looping = True
    while looping:
        pygame.display.flip()
        event = pygame.event.poll()
        #looping = quit(event)
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
            looping = False
    win.background.fill(RGB.Gray)
    win.screen.blit(win.background, (0, 0))
    return (fileName)

def end(win):
    from pygame import transform
    import time
    win.background = pygame.image.load("img/MCartwork.jpg").convert()
    win.background = transform.scale(win.background, win.screen.get_size())
    win.background = textedit(win.background, 'thanks for your participation', 1)
    win.screen.blit(win.background, (0, 0))
    pygame.display.flip()
    time.sleep(2)
