import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("FOAqr.dat")
t = data[:,0]
f = data[:,1]
dt = np.diff(t)
ddt = np.max(dt) - np.min(dt)
print(t[0], "    ", f[0])
if np.max(dt) == np.min(dt):
    print("Uniform with difference of ", dt)
else:
    print("Precision is  ", ddt, "\n Which is close enough to floating point precision so can be considered Uniform")
