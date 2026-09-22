## Problem Set 1 Problem 1:
## Q4: Using FFT to isolate the two main signal components in FOAqr.dat
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt
# Load Data and perform FFT
data = np.loadtxt("FOAqr.dat")
t = data[:,0]
flux = data[:,1]
dt = np.median(np.diff(t))
Famp = fft.rfft(flux)
freq = fft.rfftfreq(len(flux), d=dt)

### Low pass filter
F_low = Famp.copy()
#isolate signal component 1
F_low[freq>= 20] = 0
#inverse fft performed on only signal component 1 periods
flux_low_signal = fft.irfft(F_low, n=len(flux))

### High Pass filter
F_high = Famp.copy()
#isolate signal component 2
F_high[freq>= 80] = 0
F_high[freq<=50] = 0
#inverse fft performed only on signal component 2 periods
flux_high_signal = fft.irfft(F_high, n=len(flux))


###PLOTTING
# Figure 1: FFT spectrum with shaded signal regions
fig1, ax = plt.subplots(figsize=(10, 5))
ax.plot(freq, np.abs(Famp), color="k", lw=0.8)
#showing the two signals to be filtered with shading
ax.axvspan(0, 20, color="tab:blue", alpha=0.2, label="Signal 1 (0 - 20 per day)")
ax.axvspan(50, 80, color="tab:red", alpha=0.2, label="Signal 2 (50 - 80 per day)")

ymax = Famp.max()
ax.text(12, 2.5 * ymax, "Signal Component 1", ha="center", va="top",
        color="tab:blue", fontsize=12, fontweight="bold")
ax.text(65, 2.5 * ymax, "Signal Component 2", ha="center", va="top",
        color="tab:red", fontsize=12, fontweight="bold")
#labels and scaling
ax.set_xlim(0, 100)
ax.set_xlabel("Frequency (cycles per day)")
ax.set_ylabel("FFT Amplitude")
ax.set_title("Binary star system FFT Spectra")
ax.legend(loc="upper right")
fig1.tight_layout()
fig1.savefig("PS1P1Q4_Spectra.png", dpi=200)

# Figure2: filtered signals vs time
fig2, axs = plt.subplots(2, 1, sharex=True, figsize=(10, 7))
#Low pass signal
axs[0].plot(t, flux_low_signal, color="tab:blue", lw=0.8)
axs[0].set_ylabel("Flux")
axs[0].set_title("Signal 1: low-pass (f < 20 per day)")
# High pass signal
axs[1].plot(t, flux_high_signal, color="tab:red", lw=0.5)
axs[1].set_ylabel("Flux")
axs[1].set_title("Signal 2: band-pass (50 < f < 80 per day)")
axs[1].set_xlabel("Time (days)")
fig2.tight_layout()
fig2.savefig("PS1P1Q4_Filtered_Signals.png", dpi=200)

plt.show()