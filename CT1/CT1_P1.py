import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
#Q1 real and imaginary DFT 
def DFT( t, y):
    N = len(t)
    m = np.arange(N)
    nu = m/max(t)
    f = np.zeros(N, dtype=complex)
    for n in range(N):
        f[n] = np.sum(y*np.exp(2*np.pi* 1j*m*(n/N)))
    return nu,f

def inv_DFT(nu,f):
    N = len(nu)
    n = np.arange(N)
    y = np.zeros(N)
    for m in range(N):
        y[m] = (1/N)*np.sum(-f*np.exp(2*np.pi* 1j*m*(n/N)))
    return y


data = np.loadtxt("Q1.dat")

t = data[:,0]
Amp = data[:,1]
Amp_err = data[:,2]
freq, fAmp = DFT(t,Amp)
real_amp = np.real(fAmp)
imag_amp = np.imag(fAmp)

plt.figure()
plt.plot(freq, real_amp)
plt.xlabel('frequency (Hz)')
plt.ylabel('Real amplitude')
plt.title('Plot of Real Amplitude vs Frequency for DFT of signal in Q1')
plt.savefig('CT1_P1Q1_real.png') 
#Plot of Y(f) Vs f 
plt.figure()
plt.plot(freq, imag_amp,)
plt.xlabel("frequency (Hz)")
plt.ylabel('Imaginary amplitude')
plt.title('Plot of Imaginary Amplitude vs Frequency for DFT of signal in Q1')
plt.legend()
plt.savefig('CT1_P1_Q1_imaginary.png')  
print("DONE")

#Q2 finding nyquoist freq 
dt = data[1,0] - data[0,0]
freq_Nq = 1/(2*dt)
print(f"Nyquist Freq = {freq_Nq}")
#Q3 Power spectrum
Power = imag_amp*imag_amp + real_amp*real_amp
plt.figure()
plt.plot(freq, Power,)
plt.xlabel("frequency (Hz)")
plt.ylabel('Power Amplitude')
plt.title('Plot of Power Spectrum vs Frequency for DFT of signal in Q1')
plt.legend()
plt.savefig('CT1_P1_Q1_Power.png')  
print("DONE")
#Q4 4 Highest peaks
Power_sacrifice = Power.copy()
Power_sacrifice[freq >=freq_Nq] = 0
highest_amp = np.zeros(4)
highest_amp_freq = np.zeros(4)
for i in range(4):
    highest_amp[i] = np.max(Power_sacrifice)
    a = 0
    while highest_amp[i] != Power_sacrifice[a]:
        a+= 1 
    highest_amp_freq[i] = freq[a]
    Power_sacrifice[a] = 0
print(highest_amp_freq)
#Q5 Filtering
P_high = fAmp.copy()
P_high[freq<= np.max(highest_amp_freq)] = 0
Amp_filtered = inv_DFT(freq, P_high)
plt.figure()
plt.plot(t, Amp_filtered,)
plt.xlabel("time")
plt.ylabel('Amplitude')
plt.title('Plot of Filtered Amplitude vs time for signal in Q1')
plt.legend()
plt.savefig('CT1_P1_Q1_Filtered_not_rand.png')  
amp_high_rand = fAmp.copy()
amp_high_rand = np.random.shuffle(amp_high_rand)
print(amp_high_rand)
Amp_filtered_random = inv_DFT(freq, amp_high_rand)
plt.figure()
plt.plot(t, Amp_filtered_random)
plt.xlabel("time")
plt.ylabel('Amplitude')
plt.title('Plot of randomised Filtered Amplitude vs time for signal in Q1')
plt.legend()
plt.savefig('CT1_P1_Q1_Filtered_rand.png') 