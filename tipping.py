from fitting_functions import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
data = np.loadtxt("tips.CSV", delimiter=",",dtype=str, skiprows=1)
bill = data[:, 0].astype(float)
tip = data[:, 1].astype(float)
PctTip = data[:,6].astype(float)
params_x, _ = curve_fit(linear, bill, tip)
m,b =  params_x
print("plotting Bill Vs. Tip")
print(f"the equation of the Bill Vs. Tip plot is : y = {m:.3f}x + {b:.3f}")
plt.figure()
plt.scatter(bill,tip)
plt.plot(bill, linear(bill,m,b))
plt.xlabel("Bill")
plt.ylabel("Tip")
plt.title("Bill Vs. Tip")
params_x, _ = curve_fit(linear, bill, PctTip)
m,b =  params_x
print("plotting Bill Vs. PctTip")
print(f"the equation of the Bill Vs. PctTip plot is : y = {m*100:.2f}%x + {b:.2f}")
plt.figure()
plt.scatter(bill,PctTip)
plt.plot(bill, linear(bill,m,b))
plt.xlabel("Bill")
plt.ylabel("PctTip %")
plt.title("Bill Vs. PctTip")
plt.show()
##output for Bill Vs. Tip equation: "the equation of the Ball Vs. Tip plot is : y = 0.182x + -0.292"
#output for Bill Vs. PctTip equation: "the equation of the Ball Vs. PctTip plot is : y = 4.88%x + 15.51"
