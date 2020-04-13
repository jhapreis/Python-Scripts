import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression
import uncertainties as un
from uncertainties import ufloat

lista = np.array([ ufloat(2,0.2) , ufloat(3,0.3)]).reshape((-1, 1))
print (lista)
