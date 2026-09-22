## Problem Set 1 Problem 1:
## Q3: Verifcation of whether t values are uniformly spaced (Required for FFT)
import numpy as np
import matplotlib.pyplot as plt
# Load data from file provided
data = np.loadtxt("FOAqr.dat")
t = data[:,0]
f = data[:,1]
#array of all differences between time values
dt = np.diff(t)
# variation between the spacing
ddt = np.max(dt) - np.min(dt)
# print average spacing and the maximum variation
print("Average Spacing is ", dt.mean())
print("Variation is  ", ddt)