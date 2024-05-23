import random
from time import time
from TSP_algorithms import PathFinderSimple, PathFinderIterRoulette, PathFinderGreedy
from TSP_utils import CalculatePathLength


def RouletteIterTester(TSP_data, out_fname, max_iters, min_iters=10, repetitions=1):
	"""
	Test the effectiveness of the PathFinderIterRoulette function by running it with different numbers of iterations
	and create a CSV dataset
	
	Args:
		TSP_data: The data for the Traveling Salesman Problem.
		out_fname: The name of the output file to write the results to in CSV format.
		max_iters: The maximum number of iterations to test.
		min_iters: The minimum number of iterations to test (default: 1).
		repetitions: The number of repetitions of a single algorithm to get a mean. (default: 1)
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


def TimeEffectivenessTester(TSP_data, repetitions=100):
	SEPARATOR = '#######################'
	start_id = random.randint(0,100)
	end_id = random.randint(0,100)

	print('\nPathFinderSimple')
	print(SEPARATOR)
	time_start = time()
	for _ in range(repetitions):
		path_simple = PathFinderSimple(TSP_data, start_id, end_id)	
	# time_simple = round((time() - time_start)/repetitions, 3)
	length_simple = CalculatePathLength(TSP_data, path_simple)
	percent_simple = round((length_simple-length_simple)*100/length_simple,2)
	# effectiveness_simple = (length_simple-length_simple) / time_simple
	# print(f'Time: {time_simple}')
	print(f'Time: 0.0s')
	print(f'Path Length: {length_simple}')
	print(f'{percent_simple}% better than PathFinderSimple')
	# print(f'Effectiveness: {effectiveness_simple}')

	print('\nPathFinderGreedy')
	print(SEPARATOR)
	time_start = time()
	for _ in range(repetitions):
		path_greedy = PathFinderGreedy(TSP_data, start_id, end_id)	
	time_greedy = round((time() - time_start)/repetitions, 3)
	length_greedy = CalculatePathLength(TSP_data, path_greedy)
	percent_greedy = round((length_simple-length_greedy)*100/length_simple,2)
	effectiveness_greedy = (length_simple-length_greedy) / time_greedy
	print(f'Time: {time_greedy}s')
	print(f'Path Length: {length_greedy}')
	print(f'{percent_greedy}% better than PathFinderSimple')
	print(f'Effectiveness: {effectiveness_greedy}')

	print('\nPathFinderIterRoulette')
	print(SEPARATOR)
	time_start = time()
	for _ in range(repetitions):
		path_roulette = PathFinderIterRoulette(TSP_data, start_id, end_id, 15)	
	time_roulette = round((time() - time_start)/repetitions, 3)
	length_roulette = CalculatePathLength(TSP_data, path_roulette)
	percent_roulette = round((length_simple-length_roulette)*100/length_simple,2)
	effectiveness_roulette = (length_simple-length_roulette) / time_roulette
	print(f'Time: {time_roulette}s')
	print(f'Path Length: {length_roulette}')
	print(f'{percent_roulette}% better than PathFinderSimple')
	print(f'Effectiveness: {effectiveness_roulette}')
