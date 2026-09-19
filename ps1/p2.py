from p1 import Sample_and_DFT
import numpy as np
import matplotlib.pyplot as plt

def func(t):
    return np.cos(2*np.pi*2*t) + np.sin(2*np.pi*4*t)
f1, y1 = Sample_and_DFT(func, 0,4,0.5)
f2, y2 = Sample_and_DFT(func, 0,4,0.1)
f3, y3 = Sample_and_DFT(func, 0,20,0.1)
y1, y2, y3 = np.abs(y1), np.abs(y2), np.abs(y3)
plt.figure()
plt.plot(f1, y1, marker='o')
plt.xlabel('f')
plt.ylabel('Y(f)')
plt.axvline(x=2.0, color='red', linestyle='--', label='K' \
'nown Period of cos(2π2t) + sin(2π4t)')
plt.axvline(x=4.0, color='red', linestyle='--', label='K' \
'nown Period of cos(2π2t) + sin(2π4t)')
plt.title('Fourier transform of cos(2π2t) + sin(2π4t) for t = 4 and dt = 0.5')
plt.legend()
plt.savefig('PS1P2_DFT_1.png') 

plt.figure()
plt.plot(f2, y2, marker='o')
plt.xlabel('f')
plt.ylabel('Y(f)')
plt.axvline(x=2.0, color='red', linestyle='--', label='K' \
'nown Period of cos(2π2t) + sin(2π4t)')
plt.axvline(x=4.0, color='red', linestyle='--', label='K' \
'nown Period of cos(2π2t) + sin(2π4t)')
plt.title('Fourier transform of cos(2π2t) + sin(2π4t) for t = 4 and dt = 0.1')
plt.legend()
plt.savefig('PS1P2_DFT_2.png')  

plt.figure()
plt.plot(f3, y3, marker='o')
plt.xlabel('f')
plt.ylabel('Y(f)')
plt.axvline(x=2.0, color='red', linestyle='--', label='K' \
'nown Period of cos(2π2t) + sin(2π4t)')
plt.axvline(x=4.0, color='red', linestyle='--', label='K' \
'nown Period of cos(2π2t) + sin(2π4t)')
plt.title('Fourier transform of cos(2π2t) + sin(2π4t) for t = 20 and dt = 0.1')
plt.legend()
plt.savefig('PS1P2_DFT_3.png')  