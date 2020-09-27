# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

import numpy as np
import matplotlib.pyplot as plt

def V_c(t, tau, Vp):
    V_c = Vp * np.e**( -t / tau)
    return V_c

V = 3 #3 V
taus =[ 1*(10**-3), 10*(10**-3), 100*(10**-3), 1, 10 ]

t = np.linspace(0,0.1, 1000)
print(t, '\n')


V_capacitores = [ V_c(t, tau, V) for tau in taus ]

[ plt.plot( t , i ) for i in V_capacitores ]
plt.show()
