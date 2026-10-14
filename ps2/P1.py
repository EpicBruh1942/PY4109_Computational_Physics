# Ising model - Problem Set 2
import numpy as np
import matplotlib.pyplot as plt

rngseed = np.random.default_rng(67)
#all constants are dimensionless
J = 1
K = 1
#20x20 grid
N = 20


def get_neighbours(spins, i, j):
    #periodic boundary conditions using %N
    up = spins[(i - 1) % N, j]
    down = spins[(i + 1) % N, j]
    left = spins[i, (j - 1) % N]
    right = spins[i, (j + 1) % N]
    return up + down + left + right


def Emacro(spins, H=0):
    #only doing down and right interactions to avoid double counting
    # Emacro from Ei = −2J ∑si*sj
    e = 0
    for i in range(N):
        for j in range(N):
            down = spins[(i + 1) % N, j]
            right = spins[i, (j + 1) % N]
            e -= J * spins[i, j] * (down + right)
            e -= H * spins[i, j]
    return e


def heat_bath(spins, i, j, T, H=0):
    #energy change if the spin flips / metropolis
    Espin = 2 * spins[i, j] * (J * get_neighbours(spins, i, j) + H)

    if Espin <= 0:
        spins[i, j] *= -1
    elif rngseed.random() < np.exp(-Espin / (K * T)):
        spins[i, j] *= -1


def one_MC(spins, T, H=0):
    #trying to flip every spin once
    for i in range(N):
        for j in range(N):
            heat_bath(spins, i, j, T, H)


def magnetisation(spins):
    #M = 1/N ∑si
    return np.sum(spins) / (N * N)


def question_1():
    temperatures = [1, 2, 2.22, 2.29, 3, 5]
    times = 1200

    plt.figure(figsize=(10, 5))
    for T in temperatures:
        #start with random spins at each temperature
        spins = rngseed.choice([-1, 1], size=(N, N))
        m_values = []
        #do 1200 montecarlo heat bath loops and find the magnetism
        #  for each
        for t in range(times):
            one_MC(spins, T)
            m_values.append(magnetisation(spins))

        plt.plot(range(1, times + 1), m_values, label=f"T = {T}", linewidth=1)
    #plot magnetism over time
    plt.xlabel("Monte Carlo time (sweeps)")
    plt.ylabel("Magnetisation per spin")
    plt.title("Magnetisation over time")
    plt.legend()
    plt.tight_layout()
    plt.savefig("ising_part1.png", dpi=200)


def question_2():
    #initialise arrays
    temperatures = np.arange(1, 5, 0.03)
    m_values = []
    e_values = []
    c_values = []

    for T in temperatures:
        spins = rngseed.choice([-1, 1], size=(N, N))

        #let the lattice be primarily decided by thermodynamics
        #  (not by the initial random config) by letting it run for
        # 100 runs
        for t in range(200):
            one_MC(spins, T)
        #get all magnetisation and Emacro vals for each temp
        m_samples = []
        e_samples = []
        for t in range(200):
            one_MC(spins, T)
            m_samples.append(abs(magnetisation(spins)))
            e_samples.append(Emacro(spins))
        #get mean values for each temp
        m_values.append(np.mean(m_samples))
        e_values.append(np.mean(e_samples) / (N * N))
        #calculate the heat capacity from C = (ΔE)^2/(k(T^2))
        dE = (np.mean(np.array(e_samples) ** 2) - np.mean(e_samples) ** 2)
        c_values.append(dE / (K * (T ** 2) * (N **2)))
    #average magnetisation per spin vs temp
    plt.figure(figsize=(8, 9))
    plt.subplot(3, 1, 1)
    plt.plot(temperatures, m_values)
    plt.ylabel("Mean |M| per spin")
    #average energy per spin vs temp
    plt.subplot(3, 1, 2)
    plt.plot(temperatures, e_values)
    plt.ylabel("Mean energy per spin")
    #heat capacity per spin vs temp
    plt.subplot(3, 1, 3)
    plt.plot(temperatures, c_values)
    plt.xlabel("Temperature")
    plt.ylabel("Heat capacity per spin")

    plt.tight_layout()
    plt.savefig("ising_part2.png", dpi=200)


def question_3():
    fields = np.linspace(-6, 6, 121)

    for T in [0.25, 5]:
        #start with all spins down and increase H
        spins = -np.ones((N, N), dtype=int)
        m_increasing = []
        for H in fields:
            for sweep in range(100):
                one_MC(spins, T, H)
            m_increasing.append(magnetisation(spins))

        #start with all spins up and decrease H
        spins = np.ones((N, N), dtype=int)
        m_decreasing = []
        fields_decreasing = fields[::-1]
        for H in fields_decreasing:
            for sweep in range(100):
                one_MC(spins, T, H)
            m_decreasing.append(magnetisation(spins))
        #plot graphs for both temps with each direction on each graph
        plt.figure(figsize=(8, 5))
        plt.plot(fields, m_increasing, label="H increasing")
        plt.plot(fields_decreasing, m_decreasing, label="H decreasing")
        plt.xlabel("External field H")
        plt.ylabel("Magnetisation per spin")
        plt.title(f"Magnetisation against field at T = {T}")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"ising_part3_T{T}.png", dpi=200)

#run questions only if this .py file is being interpreted directly
# to allow for the functions to be imported without running full simulaion
if __name__ == "__main__":
    question_1()
    question_2()
    question_3()
    plt.show()
