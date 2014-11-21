from tools import *
from pygame.locals import *
import pygame
from libpy import RGBcolor as RGB


def textedit(background, line, num):
    font = pygame.font.Font(None, 36)
    text = font.render(line, True, RGB.Black)
    textpos = text.get_rect(center=(background.get_width()/2, (background.get_height()/8)*num))
    background.blit(text, textpos)
    return (background)

def intro(win, experiment):
    print 'toto'
    win.background = textedit(win.background, experiment, 1)
    win.background = textedit(win.background, 'For each tries, you need to determine which way the presented image has moved.', 3)
    win.background = textedit(win.background, 'Use the arrow keys (left and right) to make your choice.', 4)
    win.background = textedit(win.background, 'press enter to start the experience', 6)
    win.screen.blit(win.background, (0, 0))
    looping = True
    print 'toto01'
    while looping:
        pygame.display.flip()
        event = pygame.event.poll()
        looping = quit(event)
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
            looping = False
    win.background.fill(RGB.Gray)
    win.screen.blit(win.background, (0, 0))
    print 'toto02'
    return

def end(win):
    from pygame import transform
    win.background = pygame.image.load("img/MCartwork.jpg").convert()
    win.background = transform.scale(win.background, win.screen.get_size())
    win.background = textedit(win.background, 'thanks for your participation', 1)
    win.screen.blit(win.background, (0, 0))
    looping = True
    while looping:
        pygame.display.flip()
        event = pygame.event.poll()
        looping = quit(event)
    return

