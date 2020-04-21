#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:15:45 2019

@author: jj
"""

import numpy as np

n = int ( input ('insert the nunber you wanna know the divisors: ', ) )
lista = []

print ()

for i in range (1, n+1, 1):
    divisão = n / i
    quociente = n // i
    resto = n % i
    if resto == 0:
#        print ( i )
        lista.append (i)
#        print (lista)

#for idx, item in enumerate(lista):
#        item = item.split()
#        item = ''.join(item)
#        lista[idx] = int(item)

print (lista)
#print ( len (lista) )

count = len (lista)

if  count > 2:
    print ('your number is not prime and the number of divisors is equal to', count)
elif count == 1:
    print ('1 is not a prime number ¯\_(ツ)_/¯')
else:  
    print ('ok, we do have a prime number')