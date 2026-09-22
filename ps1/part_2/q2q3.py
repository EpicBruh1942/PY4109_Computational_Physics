## Problem Set 1 Problem 2:
## Q2: Monte Carlo code which simulates isotropic scattering of photons through a
## uniform slab
import numpy as np
import matplotlib.pyplot as plt
#setting rng seed to 67 for reproducability
rngseed = np.random.default_rng(67)
# creating the photon class so the position and movement direction 
# of a single photon can be logged
class photon:
    #zmax is the height of the slab it must escape
    #tmax is the maximum travel time before scattering
    def __init__(self,zmax,tmax):
        #photons start at origin
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        #photons go straight up initially
        self.theta = 0.0
        self.phi = 0.0
        #set the initial tmax and zmax
        self.zmax = zmax
        self.tmax = tmax
    def evolve_photon(self):
        #setting the photon to travel for a random time between
        # 0 and tmax 
        rng = rngseed.random()
        t = -np.log(1-rng)
        L = t /self.tmax
        #updating the distance after traveling t seconds
        # the direction of travel is based on theta and phi
        self.x = self.x + L*np.sin(self.theta)*np.cos(self.phi)
        self.y = self.y + L*np.sin(self.theta)*np.sin(self.phi)
        self.z = self.z + L*np.cos(self.theta)
    def scatter(self):
        #set the new theta and phi randomly from the equations
        #derived in q1
        rng1 = rngseed.random()
        rng2 = rngseed.random()
        self.theta = np.arccos(2*rng1-1)
        self.phi = 2*np.pi*rng2
    def run(self):
        #runs a loop of evolve->scatter until the photon leaves
        #the box and then returns theta and a bool for if it left the top
        while True:
            #set the photon moving
            self.evolve_photon()
            if self.z >self.zmax or self.z <0:
                #break the loop if it leaves the block
                break
            #scatter to change direction
            self.scatter()
        #return true if the photon escaped the top of the block
        if self.z >= self.zmax:
            return True , self.theta
        else:
            return False, self.theta

#set params
zmax = 1.0
tmax = 10.0
N = 100000
mu_bins = 20
theta_results = []
#run N simulations and make an array of all the 
#thetas for photons that left the box
for i in range(N):
    top_emission, theta = photon(zmax, tmax).run()
    if top_emission == True:
        theta_results.append(theta)
print(f"{len(theta_results)} photons emitted from top")
# getting variables for the Flux calculation
mu_results = np.cos(theta_results)
edges = np.linspace(0, 1, mu_bins + 1)
Ni = np.histogram(mu_results, bins=edges)[0]
N_o = len(theta_results)
mu_i = 0.5 * (edges[1:] + edges[:-1])  
#calculating the flux and the angle in degrees
I_f = Ni * mu_bins / (2 * N_o * mu_i)
theta_i = np.degrees(np.arccos(mu_i))
#import the chandrasekhar results
ang_c, I_c = np.loadtxt("Chandrasekhar1960.dat", unpack=True)
### Q3: Determine appropriate errors for each bin
#🦖 Gaussian error 
I_f_err = I_f/np.sqrt(Ni)

plt.errorbar(theta_i, I_f, yerr=I_f_err, fmt='o', label=f"Monte Carlo ({N_o} photons)")
plt.plot(ang_c, I_c, 'r-', label="Chandrasekhar (1960)")
plt.xlabel(r"Angle from normal $\theta$ (deg)")
plt.ylabel(r"$I/F$")
plt.legend()
plt.savefig("PS1P2q2q3.png", dpi=200)