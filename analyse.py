import numpy as np
np.set_printoptions(precision=3, suppress=True)
import pylab
import matplotlib.pyplot as plt

import glob
from psychopy import misc
fig = plt.figure()
ax = fig.add_subplot(111)
for fn in glob.glob('results/*npy'):
    data = misc.fromFile(fn.replace('npy', 'pickle'))
    print data
    results = np.load(fn)
    print 'experiment ', fn, ', # trials=', results.shape[1]
    ax.scatter(results[2, :], results[0, :])
#_ = ax.axis([0., 1., -1.1, 1.1])
_ = ax.set_xlabel('shift')
_ = ax.set_ylabel('perceived direction')

plt.hist(results[2,:])

alpha = .3
fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
data = []
for fn in glob.glob('results/*npy'):
    results = np.load(fn)
    # phi motion
    ind_phi = results[1, :]==1
    for i_fig, color in zip(range(1,4), ['r', 'g', 'b']):
        ind_fig = results[4, ind_phi] == i_fig
        ax1.scatter(results[2, ind_phi][ind_fig], results[0, ind_phi][ind_fig] * (.8 + .1*i_fig), c=color, alpha=alpha)
    ax1.vlines([0], ymin=-1, ymax=1)
    # reverse phi motion
    ind_rphi = results[1, :]==-1
    for i_fig, color, label in zip(range(1,4), ['r', 'g', 'b'], ['binary', 'MC', 'natural']):
        ind_fig = results[4, ind_rphi] == i_fig
        ax2.scatter(results[2, ind_rphi][ind_fig], results[0, ind_rphi][ind_fig] * (.8 + .1*i_fig), c=color, alpha=alpha, label=label)
    ax2.vlines([0], ymin=-1, ymax=1)
for ax in [ax1, ax2]:
    ax.axis([-2*results[2, :].std(), 2*results[2, :].std(), -1.15, 1.15])
    _ = ax.set_xlabel('shift')
    _ = ax.set_ylabel('perceived direction')
_ = ax2.set_ylabel('perceived direction')
_ = ax2.legend(loc='right')
