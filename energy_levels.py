import numpy as np
import matplotlib.pyplot as plt

# Constants and their values
hbar = 1.054*10**-34
m = 1
L = 1

# Quantum numbers i.e. allowed quantum states 1,2,3,4,5
n_values = np.arange(1, 6)

# Energy equation
def energy(n):
    return (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)

# Calculate energies
energies = energy(n_values)

# Creating figure i.e. graph canvas
plt.figure(figsize=(10, 6))

# Plot horizontal energy levels
for n, E in zip(n_values, energies):
    plt.hlines(E, 0, 1, label=f'n = {n}')

# Labels and title
plt.title("Quantized Energy Levels in an Infinite Potential Well")
plt.xlabel("Quantum States")
plt.ylabel("Energy")

plt.grid()

# Show plot
plt.show()
