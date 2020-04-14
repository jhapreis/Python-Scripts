#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 13:30:36 2018

@author: j
"""
import numpy as np
import matplotlib.pyplot as plt

##Grounding Resistance Simulation

rho = 500
L = 2
D = 10*0.0254

Rt_1 = ( rho / (2*np.pi*L) ) * ( np.log(8*L / D) - 1 )

print ('Rt_1 =', Rt_1)

print ('Rt_2 =', Rt_1 / 2)

print ('Rt_3 =', Rt_1 / 3)

print ('Rt_4 =', Rt_1 / 4)