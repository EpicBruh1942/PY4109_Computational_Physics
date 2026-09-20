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
theta_results = []
for i in range(N):
    top_emission, theta = photon(zmax, tmax).run()
    if top_emission == True:
        theta_results.append(theta)
print(f"{len(theta_results)} photons emitted from top")

plt.hist(np.degrees(theta_results), bins=20)
plt.xlabel(r"$\theta$ at exit")
plt.show()