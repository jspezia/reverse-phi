#/usr/bin/env python
# -*- coding: utf-8 -*-

def toto(num=''):
    print 'toto' + str(num)

def toss():
    """
        Return 1 or -1
    """
    import numpy
    return (((numpy.random.rand()>.5)*2-1))

def mcg(img, term, shift, contrast_toss):
    """
        return a movie with a duration of 2*term:
        movie[:,:,:term] = img
        movie[:,:,term:] = roll(img * contrast, shift)
        if img is a movie, shift act out like frame
    """
    import numpy as np
    movie = np.zeros([img.shape[0], img.shape[1], (2*term)])
    if (img.ndim == 2):
        movie[:, :, :term] = img[:, :, np.newaxis]
        imgN = np.roll(img, shift, 1) * contrast_toss
        movie[:, :, term:] = imgN[:, :, np.newaxis]
    else:
        im1 = img[:, :, ((img.shape[2])/2)]
        movie[:, :, :term] = im1[:, :, np.newaxis]
        im2 = img[:, :, ((img.shape[2])/2 + shift)] * contrast_toss
        movie[:, :, term:] = im2[:, :, np.newaxis]
    return (movie)
