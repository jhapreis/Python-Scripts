from uncertainties import ufloat
from uncertainties.umath import *  # sin(), etc.
x = ufloat(1, 0.1)  # x = 1+/-0.1

print (2*x)

print ( sin(2*x) )

print ( (2*x+1000).derivatives[x] )  