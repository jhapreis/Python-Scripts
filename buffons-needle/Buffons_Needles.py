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

#N = randint(0, number)
#print ('N =', N)
random_array = np.random.randint ( 0, number, ( 30, 30) )

#%%pi valeu measuring

pi = 2*number / random_array #if N --> infinite, then the value tends to pi

#print('pi =', pi)

#%%filtering pi

myRange = [ 1, 10 ]
myArr = pi
myArrFiltered = [x for a.all(x) in myArr if myRange[0] <= x <= myRange [1] ]