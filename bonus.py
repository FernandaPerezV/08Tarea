from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapz
import time
start_time = time.time()

def w(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion


def w_normalizado(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion / integral


def avanza_metropolis(w_normalizado, xn, delta):
    r = np.random.uniform(-1., 1.)
    xp = xn + delta * r
    gamma = np.random.uniform(0., 1.)
    if w(xp) / w(xn) > gamma:
        return xp
    else:
        return xn


def xn_mas_1(w, xn, N, delta):
    xn_mas_1 = np.zeros(N)
    xn_mas_1[0] = np.copy(xn)
    for i in range(len(xn_mas_1)-1):
        xn_mas_1[i+1] = avanza_metropolis(w_normalizado, xn_mas_1[i], delta)
    return xn_mas_1

# Se escoge semilla
np.random.seed(212)

d = 3.79
xn = np.linspace(0,5,6)
f_distribucion_w = np.zeros(len(xn), dtype=object)
for i in range(len(xn)):
    f_distribucion_w[i] = xn_mas_1(w, xn[i], 10**7, d)

print("--- %s seconds ---" % (time.time() - start_time))