import numpy as np
import matplotlib.pyplot as plt

# Length of the box is taken to be L
L = 1

# Fixing the start and end positions of the box and making 1000 equal spaces
x = np.linspace(0, L, 1000)

# Wavefunction define
def psi(n, x):
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Probability density function
def probability_density(n, x):
    return psi(n, x)**2

# Quantum states to visualize
levels = [1, 2, 3]

# Creating the figure
plt.figure(figsize=(10, 6))

# Plotting probability densities
for n in levels:
    plt.plot(x, probability_density(n, x), label=f'n = {n}')

# Graph labels
plt.title("Probability Density in an Infinite Potential Well")
plt.xlabel("Position x")
plt.ylabel(r"$|\psi(x)|^2$")

plt.legend()
plt.grid()
plt.show()
