import random
import math


def pick_random_points(min_x, max_x, min_y, max_y, number_of_points):
	"""
	Generate a list of random points between the given minimum and maximum values.

	Args:
		min (float): The minimum value for the random points.
		max (float): The maximum value for the random points.
		number_of_points (int): The number of random points to generate.

	Returns:
		list (float): A list of random points.

	"""
	points = []
	for _ in range(number_of_points):
		x = random.uniform(min_x, max_x)
		y = random.uniform(min_y, max_y)
		points.append((x,y))
	return points


def montecarlo_circles():
	RADIUS = 1
	INTGR_X_RNG = (-RADIUS, RADIUS)
	INTGR_Y_RNG = (-RADIUS, RADIUS)
	rectngl = (abs(INTGR_X_RNG[0]) + abs(INTGR_X_RNG[1]))*(abs(INTGR_Y_RNG[0]) + abs(INTGR_Y_RNG[1]))
	points = pick_random_points(INTGR_X_RNG[0], INTGR_X_RNG[1], INTGR_Y_RNG[0], INTGR_Y_RNG[1], 10000)
	hits = 0
	shots = 0
	for point in points:
		if (point[0]**2+point[0]**2) <= RADIUS**2:
			hits += 1
		shots += 1
	return rectngl*(hits/shots)



def montecarlo_sine():
	INTGR_X_RNG = (0,2)
	INTGR_Y_RNG = (0,1)
	rectngl = (abs(INTGR_X_RNG[0]) + abs(INTGR_X_RNG[1]))*(abs(INTGR_Y_RNG[0]) + abs(INTGR_Y_RNG[1]))
	points = pick_random_points(INTGR_X_RNG[0], INTGR_X_RNG[1], INTGR_Y_RNG[0], INTGR_Y_RNG[1], 10000)
	hits = 0
	shots = 0
	for point in points:
		if abs(math.sin(point[0])) >= abs(point[1]):
			hits += 1
		shots += 1
	return rectngl*(hits/shots)
	



def main():
	print(montecarlo_sine())
	print(montecarlo_circles())
	


if __name__ == "__main__":
	main()
