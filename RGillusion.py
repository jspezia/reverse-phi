import libpy as lb
import numpy as np
import sys, os
import MotionClouds as mc

h = 400
w = 200
f = 64

fx, fy, ft = mc.get_grids(h, w, f)
color = mc.envelope_color(fx, fy, ft)
env = color * mc.envelope_speed(fx, fy, ft)
env = mc.envelope_gabor(fx, fy, ft)
env = mc.random_cloud(env)
env = mc.rectif(env, contrast=1.)
tomat = env
env = env * 255
stimulus = np.zeros([h, w, f, 3]).astype(int)

i = 0
while (i != f):
	if (i % 2 == 0):
		stimulus[:, :, i, 0] = env[:, :, i]
		stimulus[:, :, i, 1] = 0 # 128 #env[:, :, i]
		stimulus[:, :, i, 2] = 0 # 255 - env[:, :, i]
	else:
		#stimulus[:, :, i, 0] = 255 - env[:, :, i]
		stimulus[:, :, i, 1] = 255 - env[:, :, i]
		stimulus[:, :, i, 0] = 0 #128 #env[:, :, i]
		stimulus[:, :, i, 2] = 0 #env[:, :, i]
#		stimulus[:, :, i, :] = 255 - env[:, :, i, np.newaxis]
	i += 1

lb.show_stimulus(stimulus, 'stimulus', exit=False, wait=0.0)
#lb.saveMovie(stimulus, 'allreverseGR', vext='.gif')
