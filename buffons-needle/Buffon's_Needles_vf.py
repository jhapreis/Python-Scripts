#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 18:10:23 2018

@author: j
"""
import numpy as np
import matplotlib.pyplot as plt
from random import randint

#print ('pi =', np.pi)

#%%userInput

userInput = input ( ' Pick a number: ')
number = float (userInput)

#print (number)

#%%Defining the needles number

N = randint(0, number)
print ('N =', N)

#%%pi valeu measuring

pi = 2*number / N #if N --> infinite, then the value tends to pi

print('pi =', pi)