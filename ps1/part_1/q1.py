## Problem Set 1 Problem 1:
## Calculates a Discrete Fourier Transform of cos(2π2t)
import matplotlib.pyplot as plt
import numpy as np
# Function takes in time array and corresponding amplitude
# array of signal and returns decomposed signal in form of 
# frequency array (nu) and amplitude (f) of corresponding frequency
def DFT( t, y):
    N = len(t)
    m = np.arange(N)
    nu = m/max(t)
    f = np.zeros(N, dtype=complex)
    for n in range(N):
        f[n] = np.sum(y*np.exp(-2*np.pi* 1j*m*(n/N)))
    return nu,f

def func(t):
    return np.cos(2*np.pi*2*t)

def Sample_and_DFT(ft, t0, t1, dt):
    t = np.arange(t0,t1,dt)
    y = ft(t)
    return DFT(t,y)

freq, y = Sample_and_DFT(func, 0, 10, 0.1)
y = np.abs(y)
t = np.linspace(-10, 10, 500)
#Plot of y(t) Vs t 
plt.figure()
plt.plot(t, func(t))
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Plot of cos(2π2t) vs t')
plt.savefig('PS1P1Q1_cos.png') 
#Plot of Y(f) Vs f 
plt.figure()
plt.plot(freq, y, marker='o')
plt.xlabel('f')
plt.ylabel('Y(f)')
plt.axvline(x=2.0, color='red', linestyle='--', label='Known Period of cos(2π2t)')
plt.title('Fourier transform of cos(2π2t)')
plt.legend()
plt.savefig('PS1P1Q1_cos_DFT.png')  
print("DONE")