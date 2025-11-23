from fitting_functions import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
data = np.loadtxt("tips.CSV", delimiter=",",dtype=str, skiprows=1)
t = data[:, 0].astype(float)
x = data[:, 1].astype(float)
h = data[:, 2].astype(float)
print(t)
print(x)
print(h)
