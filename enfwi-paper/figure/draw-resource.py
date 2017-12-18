#!/usr/bin/env python3

"""
plot the computational cost of three methods
"""

import matplotlib.pyplot as plt
import numpy as np

axis_tick_font_size = 16
axis_label_font_size = 19
title_font_size = 19
legend_font_size = 9

samples, enfwi, fwi, essfwi = np.loadtxt(fname='./speedup.txt', delimiter=',', unpack=True)

f = plt.figure(1)
plt.plot(samples, enfwi, 'ro-', linewidth=2, label='EnFWI')
plt.plot(samples, fwi, 'bs-', linewidth=2, label='FWI')
plt.plot(samples, essfwi, 'g^-', linewidth=2, label='EssFWI')
plt.axis([0, 21, 0, 45])
plt.xlabel('number of model samples', fontsize=axis_label_font_size)
plt.ylabel('computational cost (normalized)', fontsize=axis_label_font_size)
plt.title('Computational cost of FWI, EssFWI and EnFWI', fontsize=title_font_size)
plt.legend(loc='best', fontsize=legend_font_size)
# plt.show()

f.savefig('speedup.png')

