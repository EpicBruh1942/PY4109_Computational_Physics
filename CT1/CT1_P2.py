import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt
from CT1_P1 import DFT 
from CT1_P1 import inv_DFT

data = np.loadtxt("Q2.dat")

t = data[:,0]
Amp = data[:,1]
Amp_err = data[:,2]
freq_nq = 1/(2*(t[1]-t[0]))
t_size = t.size()
window_size = t_size/10 +1
amp_windows = np.zeros(t_size/window_size)
time_windows = np.zeros(t_size/window_size)
for n in range(amp_windows):
    new_amp = Amp.copy()
    new_amp[t<= t[window_size*n]] = 0
    new_amp[t>= t[window_size*(n+1)]] = 0
    freq, fAmp = DFT(t,new_amp)
    real_amp = np.real(fAmp)
    imag_amp = np.imag(fAmp)
    Power = imag_amp*imag_amp + real_amp*real_amp
    plt.figure()
    plt.plot(freq, Power,)
    plt.xlabel("frequency (Hz)")
    plt.ylabel('Power Amplitude')
    plt.title(f'Plot of Power Spectrum vs Frequency for DFT of signal in Q2 window {n}')
    plt.legend()
    plt.savefig(f'CT1_P2_Power_window={n}.png')  
    print("DONE")


