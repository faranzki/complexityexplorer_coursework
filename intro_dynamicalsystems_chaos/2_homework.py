import matplotlib.pyplot as plt
import math

initial_values = [10, 20, 30]
dt_values = [0.1, 0.5, 1, 1.5, 2]
t_max = 30

for dt in dt_values:
	orbits = [[]]
	analytical_solutions = [[]]
	for value in initial_values:
		orbit = []
		analytical_solution = []
		i = 0
		x = value
		T = value
		while i != t_max:
			orbit.append(x)
			diff = 0.2 * (20 - x)
			x = x + diff * dt
			analytical_solution.append(T)
			T = 20 - (20 - T) * math.exp(-0.2 * dt)
			i = i + 1			
		orbits.append(orbit)
		analytical_solutions.append(analytical_solution)


	for x in range(0, len(orbits)):
		plt.plot(orbits[x])
	for x in range(0, len(analytical_solutions)):
		plt.plot(analytical_solutions[x], '--')
	plt.show()