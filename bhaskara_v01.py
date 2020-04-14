#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:23:41 2019

@author: jj
"""
import numpy as np

a = float ( input ('a = ', ) )
b = float ( input ('b = ', ) )
c = float ( input ('c = ', ) )

delta = b**2 - 4*a*c

x_1 = ( -b + np.sqrt (delta) ) / (2*a)
x_2 = ( -b - np.sqrt (delta) ) / (2*a)

print()

print ('delta =', delta)
print ('raiz do delta =', np.sqrt(delta) )
print ('x_1 =', x_1)
print ('x_2 =', x_2)

#próximas etapas envolvem debugs em entradas absurdas e 
#explicações de crashs no programa