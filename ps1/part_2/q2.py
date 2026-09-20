import numpy as np
import matplotlib.pyplot as plt
rngseed = np.random.default_rng(67)
class photon:
    def __init__(self,zmax,tmax):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.theta = 0.0
        self.phi = 0.0
        self.zmax = zmax
        self.tmax = tmax
    def evolve_photon(self):
        rng = rngseed.random()
        t = -np.log(1-rng)
        L = t /self.tmax
        self.x = self.x + L*np.sin(self.theta)*np.cos(self.phi)
        self.y = self.y + L*np.sin(self.theta)*np.sin(self.phi)
        self.z = self.z + L*np.cos(self.theta)
    def scatter(self):
        rng1 = rngseed.random()
        rng2 = rngseed.random()
        self.theta = np.arccos(2*rng1-1)
        self.phi = 2*np.pi*rng2
    def run(self):
        while True:
            self.evolve_photon()
            if self.z >self.zmax or self.z <0:
                break
            self.scatter()
        if self.z >= self.zmax:
            return True , self.theta
        else:
            return False, self.theta


zmax = 1.0
tmax = 10.0
N = 100000
mu_bins = 20
theta_results = []
for i in range(N):
    top_emission, theta = photon(zmax, tmax).run()
    if top_emission == True:
        theta_results.append(theta)
print(f"{len(theta_results)} photons emitted from top")
mu_results = np.cos(theta_results)
edges = np.linspace(0, 1, mu_bins + 1)
Ni = np.histogram(mu_results, bins=edges)[0]
N_o = len(theta_results)
mu_i = 0.5 * (edges[1:] + edges[:-1])  

I_f = Ni * mu_bins / (2 * N_o * mu_i)


ang_c, I_c = np.loadtxt("Chandrasekhar1960.dat", unpack=True)
theta_i = np.degrees(np.arccos(mu_i))

I_f_err = np.sqrt(Ni) * mu_bins / (2 * N_o * mu_i)
plt.errorbar(theta_i, I_f, yerr=I_f_err, fmt='o', label=f"Monte Carlo ({N_o} photons)")
plt.plot(ang_c, I_c, 'r-', label="Chandrasekhar (1960)")
plt.xlabel(r"Angle from normal $\theta$ (deg)")
plt.ylabel(r"$I/F$")
plt.legend()
plt.show()