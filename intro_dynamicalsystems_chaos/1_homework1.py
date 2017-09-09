import numpy as np
import matplotlib.pyplot as plt

n = 10
seeds = np.linspace(0,1,11)
orbits = [[]]

for s in seeds:
	orbit = []
	seed = s
	i = 0
	new_input = seed
	while i != n:
		orbit.append(new_input)
		result = 2.5 * new_input * (1 - new_input)
		orbit.append(result)
		new_input = result
		i = i + 1
	orbits.append(orbit)

fig1 = plt.figure(2)
for x in range(0, len(orbits)):
	plt.plot(orbits[x])
fig1.savefig('orbits.png')