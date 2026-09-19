import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("FOAqr.dat")
t = data[:,0]
f = data[:,1]
dt = np.diff(t)
print(t[0], "    ", f[0])
if np.max(dt) == np.min(dt):
    print("Uniform with difference of ", dt)
else:
    print("Not Uniform and ranges from ", np.max(dt), " and ", np.min(dt))