import matplotlib.pyplot as plt
import math

def generateOrbit(initial_value, n_iterations, r):
	x = initial_value
	orbit = []
	i = 1
	while i != n_iterations:
		orbit.append(x)
		x = r * x * (1 - x)
		i = i + 1
	return orbit

r = 4
n_iterations = 100
initial_condition = 0.2
error = 0.1

orbit_1 = generateOrbit(initial_condition, n_iterations, r)
orbit_2 = generateOrbit(initial_condition + error, n_iterations, r)
orbit_diff = []
i = 0
while i != len(orbit_1):
	diff = orbit_1[i] - orbit_2[i]
	orbit_diff.append(diff)
	i = i + 1
plt.plot(orbit_1, 'k--', label = 'True value')
plt.plot(orbit_2, 'k', label = 'Prediction')
plt.plot(orbit_diff, 'b', label = 'Difference')
plt.legend()
plt.show()