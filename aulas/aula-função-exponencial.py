from math import e

x = 1 
for i in range (1, 1000):
    y = (1 + 1/x)**x
    x = x + 1
    print ('x =', x, ';', 'y =', y, ';', 'erro =', e - y)