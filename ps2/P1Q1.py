#Ising Model
import numpy as np
import matplotlib.pyplot as plt
#setting rng seed to 67 for reproducability
rngseed = np.random.default_rng(67)
#periodic boundary conditions
def get_neighbours(spins, i, j):
    N = spins.shape[0]

    up    = spins[(i - 1) % N, j]
    down  = spins[(i + 1) % N, j]
    left  = spins[i, (j - 1) % N]
    right = spins[i, (j + 1) % N]

    return up + down + left + right




# Grid size
N = 20

# Random initial spin configuration
spins = rngseed.choice([-1, 1], size=(N, N))

img = plt.imshow(spins, cmap='bwr', vmin=-1, vmax=1)
plt.title("Initial Ising Spin Configuration")
plt.colorbar(label="Spin")

# Plot the initial configuration
while True:
    for j in range(N):
        for i in range(N):
            if get_neighbours(spins,i,j) != 0:
                spins[i][j] = get_neighbours(spins,i, j)
            img.set_data(spins)
            plt.pause(0.005)
plt.show()