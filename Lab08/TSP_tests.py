import random
from time import time
from TSP_algorithms import PathFinderSimple, PathFinderIterRoulette
from TSP_utils import CalculatePathLength


def RouletteIterTester(TSP_data, out_fname, max_iters, min_iters=10, repetitions=1):
	"""
	Test the effectiveness of the PathFinderIterRoulette function by running it with different numbers of iterations
	and create a CSV dataset
	
	Parameters:
	- TSP_data: The data for the Traveling Salesman Problem.
	- out_fname: The name of the output file to write the results to in CSV format.
	- max_iters: The maximum number of iterations to test.
	- min_iters: The minimum number of iterations to test (default: 1).
	"""
	start_id = random.randint(0,100)
	end_id = random.randint(0,100)

	# Get the value of the simple pathfinder that will be the base for
	# comparing the effectiveness
	base_len = CalculatePathLength(TSP_data, PathFinderSimple(TSP_data, start_id, end_id))

	with open(out_fname, 'w+') as file:
		file.write('N of iters,Effectiveness\n')

		for iterations in range(min_iters, max_iters+1):
			effectiveness_data = []
			for _ in range(repetitions):
				
				time_start = time()
				new_path = PathFinderIterRoulette(TSP_data, start_id, end_id, iterations)
				time_delta = time() - time_start
				if not time_delta:
					time_delta = 0.0001

				new_path_len = CalculatePathLength(TSP_data, new_path)
				effectiveness = (base_len-new_path_len) / time_delta
				effectiveness_data.append(effectiveness)

			effectiveness_mean = sum(effectiveness_data)/repetitions
			file.write(f'{iterations},{effectiveness_mean}\n')

