# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

import numpy as np
import matplotlib.pyplot as plt

print('\n \n=============================================================================')
print('            GRADIENT DESCENT TEST: LINEAR REGRESSION')
print('  Make the linear regression by the equation y = A·x + B')
print('using the gradient descent algorithm')
print('============================================================================= \n \n')


# =============================================================================
# 
# =============================================================================

# y = x + 4
# A = 1 ;  B = 4
# data_x = [0, 1, 2, 3]
# data_y = [4, 5, 6, 7]
# learning_rate = 0.01
# step_limit_a, step_limit_b = 0.0001, 0.0001


data_x = [0, 1, 2, 3]
data_y = [5, 4, 6, 6.5]
learning_rate = 0.01
step_limit_a, step_limit_b = 0.0001, 0.0001


####start by making only for the intercep parameter and for knewn values



# =============================================================================
# Sum of squared residuals: delta = SUM (observed_value - predicted_value)²
# =============================================================================
# observed_value = data_y[i]
# predicted_value = y(x) = x + B
####we'll use that delta_sum calculation a lot...
def delta_sum(slope, intercept, data_on_x, data_on_y):
    aux = []
    for i in range ( len(data_x) ):
        aux.append(   ( data_on_y[i] - (slope*data_on_x[i] + intercept) )**2   )
    # print(delta)
    delta_sum = sum(aux)
    # print(delta_sum)
    return(delta_sum)



# =============================================================================
# Gradient function: take the partial derivatives of the delta-sum function
# =============================================================================
# delta-sum(b) = SUM [  data_on_y[i] - (slope*data_on_x[i] + intercept) )**2  ]
# take the derivative with respect to the parameters
# gradient_delta-sum = ( -2*SUM{ data_on_x[i] * [data_on_y[i] - (slope*data_on_x[i] + intercept)] },
#                        -2*SUM{                data_on_y[i] - (slope*data_on_x[i] + intercept) }
def gradient_delta_sum(slope, intercept, data_on_x, data_on_y):
    aux = [  [], []  ]
    for i in range ( len(data_on_x) ):
        aux[0].append(  data_on_x[i]*( data_on_y[i] - (slope*data_on_x[i] + intercept) )  )
        aux[1].append(                   data_on_y[i] - (slope*data_on_x[i] + intercept)  )
    gradient_delta_sum = [ -2*sum(aux[0]), -2*sum(aux[1]) ]
    return(gradient_delta_sum)



# =============================================================================
# Step size (depends on the value of the gradient)
# =============================================================================
def size_of_the_step(delta_slope):
    size_of_the_step = delta_slope*learning_rate
    #the learning_rate variable is globally defined previously
    return(size_of_the_step)








# =============================================================================
# Initial values
# =============================================================================
A = 0.1
B = 1
step_size = [ size_of_the_step(  gradient_delta_sum(A, B, data_x, data_y)[0]  ),
              size_of_the_step(  gradient_delta_sum(A, B, data_x, data_y)[1]  ) ]
# print(step_size, '\n')


# if (  step_size[0] < 0 or step_size[1] < 0 ):
#     print( 'NEGATIVE VALUES DETECTED!!! \n step_size = {}'.format(step_size) )

# =============================================================================
# 'While loop' to run over step_size and the intercept value
# =============================================================================
counter = 0
# print( abs(step_size) > 0.001 ) 
while (   ( abs(step_size[0]) > step_limit_a or abs(step_size[1]) > step_limit_b )  and  counter < 1000   ):
    print(step_size, counter, A, B)
    # print( abs(step_size[0]), abs(step_size[1]) )
    
    
    step_size = [ size_of_the_step(  gradient_delta_sum(A, B, data_x, data_y)[0]  ),
                  size_of_the_step(  gradient_delta_sum(A, B, data_x, data_y)[1]  ) ]
    # A -= step_size[0]
    # B -= step_size[1]
    if abs(step_size[0]) > step_limit_a:
        A = A - step_size[0]              
    if abs(step_size[1]) > step_limit_b:
        B = B - step_size[1]
    counter += 1

    
    plt.scatter( A, delta_sum(A,B,data_x,data_y) )
    
# print(counter)

plt.show()

# =============================================================================
# Results
# =============================================================================
if counter >= 1000:
    print( 'WE FINISHED AFTER TOO MANY ATTEMPTS! I GIVE UP!!! \n Here is your result: A = {}, B = {}'.format(A, B) )
elif ( abs(step_size[0]) <= -0.1 or abs(step_size[1]) <= -0.1 ):
    print( 'SUCCES!!! (hope). \n Here is your result: A = {}, B = {}. \n Found after {} attempts.'.format(A, B, counter) )


print('\n', A,B)
    




# =============================================================================
# Plot
# =============================================================================

plt.scatter(data_x, data_y)

x = np.array(range(-100,100))
y = A*x + B
plt.plot(x, y)

plt.axis([-2,4,3,8])
plt.show()



####by now, the limit values are the most important part, and the number of iterations as well
