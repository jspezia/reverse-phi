import pygame
from pygame.locals import *
from pygame import surfarray
import sys, os

def quit(event):
    _continue = True
    if event.type == QUIT:
        _continue = False
    if (event.type == KEYDOWN) and (event.key == K_ESCAPE):
        _continue = False
    if _continue == False:
        pygame.quit()
        sys.exit()
    return(_continue)

def show_stimulus(stimulus, name='toto', resizable=True):
    """
    stimulus is a 4 dimension numpy array: [height, weight, frame, RGB]
    """
    h = stimulus.shape[0]
    w = stimulus.shape[1]
    f = stimulus.shape[2]
    surfarray.use_arraytype('numpy')
    pygame.init()
    pygame.display.set_caption(name)
    if (resizable == True): screen = pygame.display.set_mode((h, w), RESIZABLE)
    else: screen = pygame.display.set_mode((h, w))
    surface = pygame.Surface((h, w))
    looping = True
    i = 0
    while looping:
        if (i == f): i = 0
        surfarray.blit_array(surface, stimulus[:, :, i, :])
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        event = pygame.event.poll()
        looping = quit(event)
        i += 1

def remove_frames(tmpdir, files):
    for fname in files: os.remove(fname)
    if not(tmpdir == None): os.rmdir(tmpdir)

def saveSurface(pixels, filename):
    try:
        surf = pygame.surfarray.make_surface(pixels)
    except IndexError:
        (width, height, colours) = pixels.shape
        surf = pygame.display.set_mode((width, height))
        pygame.surfarray.blit_array(surf, pixels)
    pygame.image.save(surf, filename)

def saveFrame(stimulus, filename='exemple', figpath='movie_frame'):
    if not(os.path.isdir(figpath)): os.mkdir(figpath)
    for i in range(stimulus.shape[2]):
        filename = figpath + 'frame' + str(i) + '.jpg'
        saveSurface(stimulus[:, :, i, :], filename)

def saveMovie(stimulus, filename, vext='.webm', fps=50, verbose=False):
    import tempfile

    if verbose: verb_ = ''
    else: verb_ = ' 2>/dev/null'
    tmpdir = tempfile.mkdtemp()
    files = []
    f = stimulus.shape[2]
    frame = 0
    for frame in range(f):
        fname = os.path.join(tmpdir, 'frame%03d.png' % frame)
        files.append(fname)
        saveSurface(stimulus[:, :, frame, :], fname)
    if (vext == '.webm'):
        options = '-f webm -pix_fmt yuv420p -vcodec libvpx -qmax 12 -g ' + str(fps) + ' -r ' + str(fps) + ' -y '
        cmd = 'ffmpeg -i '  + tmpdir + '/frame%03d.png ' + options + filename + '.webm' + verb_
    else:
        options = '-delay 1 -loop 0 '
        cmd = 'convert '  + tmpdir + '/frame*.png  ' + options + filename + vext + verb_
    os.system(cmd)
    remove_frames(tmpdir, files)
