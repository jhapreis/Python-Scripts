#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:12:03 2019

@author: jj-desktop
"""

def linear_regression (X, Y, u_Y):
# f(x) = Ax + B; A = slope and B = linear coefficient
# w, wx, wy, wx², wxy
#   Para resolver a questão da regressão linear de incerteza nas duas variáveis,
# podemos escrever (y +/- u_y) = k·(x +/- u_x) como ( y +/- (u_y + k·u+x) ) = k·x    
    
    w = []
    wx = []
    wy = []
    wx2 = []
    wxy = []
    for i in range ( len (X) ):
        w.append ( 1 / (u_Y[i]**2) )
        wx.append ( w[i]*X[i] )
        wy.append ( w[i]*Y[i] )
        wx2.append ( w[i]*(X[i]**2) )
        wxy.append ( w[i]*X[i]*Y[i] )

    sum_w = sum (w)
#    print (sum_w)
    sum_wx = sum (wx)
    sum_wy = sum (wy)
    sum_wx2 = sum (wx2)
    sum_wxy = sum (wxy)        
    delta = sum_w*sum_wx2 - (sum_wx)**2
#    print (delta)
    
#    global A, u_a, B, u_b
    A = ( sum_w*sum_wxy - sum_wx*sum_wy ) / delta
    if (sum_w / delta) > 0:
        u_a = ( sum_w / delta )**0.5
    elif (sum_w / delta) < 0:
        u_a = ( (-1)*sum_w / delta )**0.5
    B = ( sum_wy*sum_wx2 - sum_wxy*sum_wx ) / delta
    if (sum_wx2 / delta) > 0:
        u_b = ( sum_wx2 / delta )**0.5
    elif (sum_wx2 / delta) < 0:
        u_b = ( (-1)*sum_wx2 / delta )**0.5
#    u_b = ( sum_wx2 / delta )**0.5

#    print ('pimba')
    return ( [A, u_a, B, u_b] )
    
#print ( linear_regression( data['x'], data['y'] ) )
#print (A)

#for i in range ( len(n) ):
#    if n == 1:

x = [1, 2, 3]
y = [2, 4, 6]
u_y = [0.0000000000000001, 0.0000000000000001, 0.0000000000000001]

print ( linear_regression (x, y, u_y) )