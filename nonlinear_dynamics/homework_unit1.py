import matplotlib.pyplot as plt

x_init = [0.2, 0.200001]
r = 3.72
n = 5000

orbits = [[]]

for x in x_init:
	orbit = []
	seed = x
	i = 1
	new_input = x
	orbit.append(new_input)
	while i != n:
		result = r * new_input * (1 - new_input)
		orbit.append(result)
		i = i + 1
		new_input = result
	orbits.append(orbit)

difference = []

for i in range(0,len(orbits[1])):
	diff = orbits[1][i] - orbits[2][i]
	difference.append(diff)

print difference[-1]
average = (1/n) * sum(difference) #doesn't work - problem is that (1/n) is approximated to 0
print average

plt.plot(difference, 'ro')
plt.show()